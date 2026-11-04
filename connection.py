

import os
import sys
import re
import inspect
import subprocess
import requests
import urllib3

urllib3.disable_warnings()


def ok(msg):
    print(f"  ✅ {msg}")


def warn(msg):
    print(f"  ⚠️  {msg}")


def fail(step, reason, fix=""):
    print(f"\n❌ ÉCHEC À L'ÉTAPE [{step}]")
    print(f"   👉 Cause    : {reason}")
    if fix:
        print(f"   🛠️  Solution : {fix}")
    sys.exit(1)


print("=" * 65)
print("🔍 DIAGNOSTIC CONNEXION & DÉCOUVERTE DES MODÈLES LLM CIB")
print("=" * 65)

# ─── ÉTAPE 1 : Import de llm.py ─────────────────────────────
print("\n1️⃣  Chargement du module llm.py...")
try:
    import llm
    ok(f"llm.py chargé depuis : {llm.__file__}")
except Exception as e:
    fail("1 - Import llm.py", str(e), "Vérifie que ce script est dans le même dossier que llm.py.")

# ─── ÉTAPE 2 : Vérification Chrome vs ChromeDriver ──────────
print("\n2️⃣  Vérification Chrome & ChromeDriver...")
driver_path = os.path.join(os.path.dirname(os.path.abspath(llm.__file__)), "chromedriver.exe")
driver_ver = None

if not os.path.isfile(driver_path):
    warn(f"chromedriver.exe non trouvé à côté de llm.py ({driver_path})")
else:
    try:
        out = subprocess.check_output([driver_path, "--version"], text=True, stderr=subprocess.STDOUT).strip()
        driver_ver = out.split()[1] if len(out.split()) > 1 else out
        ok(f"Version ChromeDriver : {driver_ver}")
    except Exception as e:
        fail(
            "2 - Exécution ChromeDriver",
            f"Impossible de lancer chromedriver.exe ({e})",
            "Débloque le fichier dans Propriétés -> Débloquer.",
        )

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
]
chrome_exe = next((p for p in chrome_paths if os.path.isfile(p)), None)
if chrome_exe:
    try:
        cmd = f'(Get-Item "{chrome_exe}").VersionInfo.ProductVersion'
        chrome_ver = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True).strip()
        ok(f"Version Google Chrome : {chrome_ver}")
        if driver_ver:
            if chrome_ver.split(".")[0] != driver_ver.split(".")[0]:
                fail(
                    "2 - Incompatibilité de version",
                    f"Chrome est en version {chrome_ver} mais ChromeDriver est en version {driver_ver}",
                    f"Télécharge : https://storage.googleapis.com/chrome-for-testing-public/{chrome_ver}/win64/chromedriver-win64.zip",
                )
            else:
                ok(f"Versions compatibles (Majeure {chrome_ver.split('.')[0]})")
    except Exception:
        pass

# ─── ÉTAPE 3 : Authentification SSO (get_auth_context) ──────
print("\n3️⃣  Test d'authentification (get_auth_context)...")
try:
    cert, headers = llm.get_auth_context()
    ok(f"Certificat : {cert}")
    ok(f"Headers récupérés (clés : {list(headers.keys())})")
except Exception as e:
    err_lines = [
        line.strip()
        for line in str(e).splitlines()
        if line.strip()
        and not line.strip().startswith("Stacktrace")
        and "0x7ff" not in line
        and "(No symbol)" not in line
    ]
    clean_err = " | ".join(err_lines[:3]) if err_lines else str(e).splitlines()[0]
    fail(
        "3 - Récupération Token / Selenium",
        clean_err,
        "Ferme toutes les fenêtres Chrome ouvertes (taskkill /F /IM chrome.exe /T) et réessaie.",
    )

# ─── ÉTAPE 4 : Découverte dynamique des modèles disponibles ─
print("\n4️⃣  Découverte automatique des modèles sur le serveur CIB...")
llm_source = inspect.getsource(llm)
urls = list(dict.fromkeys(re.findall(r'https?://[^\s"\'<>]+', llm_source)))

for attr in dir(llm):
    if any(k in attr.lower() for k in ("model", "url", "endpoint", "base")):
        val = getattr(llm, attr)
        if not callable(val) and not attr.startswith("__"):
            print(f"  📌 Config détectée dans llm.{attr} = {val}")

discovered_models = []
working_models_url = None

for u in urls:
    u_clean = u.rstrip(".,;)}]'\"")
    if any(skip in u_clean.lower() for skip in ("login", "auth", "token", "oauth", "sso", "chrome", "google")):
        continue

    base = u_clean.split("/chat")[0].split("/completions")[0].rstrip("/")
    candidates = [
        f"{base}/models",
        f"{base}/v1/models",
        f"{base}/api/models",
        f"{base}/api/v1/models",
    ]
    for candidate in dict.fromkeys(candidates):
        try:
            r = requests.get(candidate, headers=headers, verify=cert, timeout=10)
            if r.status_code == 200:
                data = r.json()
                if isinstance(data, dict) and "data" in data and isinstance(data["data"], list):
                    discovered_models = [
                        m.get("id") or m.get("name") or m.get("model")
                        for m in data["data"]
                        if isinstance(m, dict)
                    ]
                elif isinstance(data, dict) and "models" in data and isinstance(data["models"], list):
                    discovered_models = [
                        m.get("id") or m.get("name") if isinstance(m, dict) else str(m)
                        for m in data["models"]
                    ]
                elif isinstance(data, list):
                    discovered_models = [
                        m.get("id") or m.get("name") if isinstance(m, dict) else str(m)
                        for m in data
                    ]
                discovered_models = [m for m in discovered_models if m]
                if discovered_models:
                    working_models_url = candidate
                    break
        except Exception:
            pass
    if discovered_models:
        break

if discovered_models:
    ok(f"{len(discovered_models)} modèle(s) trouvé(s) en direct sur {working_models_url} :")
    for m in discovered_models:
        print(f"     🤖 {m}")
else:
    warn("Impossible de lister les modèles via /models automatiquement.")
    print(f"  🔎 URLs trouvées dans llm.py : {urls}")
    # Fallback : on regarde si des modèles sont écrits en dur dans llm.py
    fallback_models = getattr(llm, "MODELS", None) or getattr(llm, "DEFAULT_MODEL", None)
    if fallback_models:
        discovered_models = [fallback_models] if isinstance(fallback_models, str) else list(fallback_models)

# ─── ÉTAPE 5 : Test d'appel réel au LLM CIB ─────────────────
print("\n5️⃣  Test d'envoi d'un message au LLM CIB...")

# Inspecter la signature de LLMChat.__init__ pour passer les bons arguments
init_sig = inspect.signature(llm.LLMChat.__init__)
init_params = [p for p in init_sig.parameters.keys() if p != "self"]
print(f"  ℹ️  Signature de LLMChat.__init__ : ({', '.join(init_params)})")

models_to_try = discovered_models if discovered_models else ["gpt-oss-120b", "mistral-medium-3.5-ITG", "gemma-4-26b"]

success_model = None
for test_model in models_to_try:
    try:
        print(f"  ⏳ Essai avec le modèle : {test_model}...")
        # Construction dynamique des kwargs selon ce que LLMChat accepte
        kwargs = {}
        if "model" in init_params:
            kwargs["model"] = test_model
        elif "model_name" in init_params:
            kwargs["model_name"] = test_model
        if "cert" in init_params:
            kwargs["cert"] = cert
        if "headers" in init_params:
            kwargs["headers"] = headers

        chat = llm.LLMChat(**kwargs) if kwargs else llm.LLMChat(test_model, cert, headers)

        # Détection automatique de la méthode d'envoi (ask, chat, send, invoke, etc.)
        reply = None
        for method_name in ("ask", "chat", "send", "complete", "generate", "invoke"):
            if hasattr(chat, method_name) and callable(getattr(chat, method_name)):
                reply = getattr(chat, method_name)("Réponds uniquement le mot : OK")
                break
        else:
            if callable(chat):
                reply = chat("Réponds uniquement le mot : OK")

        ok(f"Réponse reçue de [{test_model}] : {str(reply).strip()[:120]}")
        success_model = test_model
        break
    except Exception as e:
        clean_err = str(e).splitlines()[0] if str(e) else repr(e)
        warn(f"Échec sur [{test_model}] : {clean_err}")

if not success_model:
    fail(
        "5 - Appel API LLM",
        "Aucun modèle n'a répondu avec succès.",
        "Regarde la liste des modèles et la signature LLMChat affichées ci-dessus.",
    )

print("\n" + "=" * 65)
print(f"🎉 TOUT EST OPÉRATIONNEL ! Modèle validé : {success_model}")
if discovered_models:
    print(f"📋 Liste exacte à utiliser pour MODELS = {discovered_models}")
print("=" * 65)
