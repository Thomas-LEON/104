

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

if os.path.isfile(driver_path):
    out = subprocess.check_output([driver_path, "--version"], text=True, stderr=subprocess.STDOUT).strip()
    driver_ver = out.split()[1] if len(out.split()) > 1 else out
    ok(f"Version ChromeDriver : {driver_ver}")

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
]
chrome_exe = next((p for p in chrome_paths if os.path.isfile(p)), None)
if chrome_exe:
    cmd = f'(Get-Item "{chrome_exe}").VersionInfo.ProductVersion'
    chrome_ver = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True).strip()
    ok(f"Version Google Chrome : {chrome_ver}")

# ─── ÉTAPE 3 : Authentification SSO (get_auth_context) ──────
print("\n3️⃣  Test d'authentification (get_auth_context)...")
try:
    auth_context = llm.get_auth_context()
    cert, headers = auth_context
    ok(f"Certificat : {cert}")
    ok(f"Headers récupérés (clés : {list(headers.keys())})")
except Exception as e:
    clean_err = str(e).splitlines()[0] if str(e) else repr(e)
    fail("3 - Récupération Token / Selenium", clean_err)

# ─── ÉTAPE 4 : Inspection de llm.py pour trouver les modèles ─
print("\n4️⃣  Recherche des modèles dans llm.py et sur l'API CIB...")
llm_source = inspect.getsource(llm)

# On cherche toutes les constantes ou listes de modèles dans llm.py
for line in llm_source.splitlines():
    if any(k in line.lower() for k in ("model", "gpt", "mistral", "gemma", "llama", "claude", "qwen", "deepseek")):
        stripped = line.strip()
        if not stripped.startswith("#") and len(stripped) < 140:
            print(f"  📄 Dans llm.py : {stripped}")

# Liste des modèles à tester (ceux de llm.py s'ils existent + ceux d'agent_core.py)
models_to_try = []
if hasattr(llm, "MODELS") and isinstance(llm.MODELS, (list, tuple, dict)):
    models_to_try.extend(list(llm.MODELS.keys()) if isinstance(llm.MODELS, dict) else list(llm.MODELS))
if hasattr(llm, "DEFAULT_MODEL") and isinstance(llm.DEFAULT_MODEL, str):
    models_to_try.append(llm.DEFAULT_MODEL)

for m in ["gpt-oss-120b", "mistral-medium-3.5-ITG", "gemma-4-26b"]:
    if m not in models_to_try:
        models_to_try.append(m)

# ─── ÉTAPE 5 : Test d'appel réel avec LLMChat.say() ─────────
print("\n5️⃣  Test d'envoi d'un message au LLM CIB avec chat.say()...")

working_models = []
for test_model in models_to_try:
    try:
        print(f"  ⏳ Test du modèle [{test_model}]...")
        chat = llm.LLMChat(
            model_id=test_model,
            auth_context=auth_context,
            high_reasoning_effort=False,
            web_search=False,
        )
        reply = chat.say("Réponds uniquement le mot : OK")
        ok(f"SUCCÈS [{test_model}] -> Réponse : {str(reply).strip()[:100]}")
        working_models.append(test_model)
    except Exception as e:
        clean_err = str(e).splitlines()[0] if str(e) else repr(e)
        warn(f"Échec [{test_model}] : {clean_err}")

if not working_models:
    fail(
        "5 - Appel API LLM",
        "Aucun des modèles testés n'a répondu.",
        "Regarde les lignes '📄 Dans llm.py' affichées à l'étape 4 ci-dessus pour voir les nouveaux noms de modèles.",
    )

print("\n" + "=" * 65)
print(f"🎉 CONNEXION 100% OPÉRATIONNELLE !")
print(f"✅ Modèles fonctionnels : {working_models}")
print("=" * 65)
