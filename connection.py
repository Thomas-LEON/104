import os
import sys
import subprocess
import json


def ok(msg):
    print(f"  ✅ {msg}")


def warn(msg):
    print(f"  ⚠️  {msg}")


def fail(step, reason, fix=""):
    print(f"\n ÉCHEC À L'ÉTAPE [{step}]")
    print(f"   Cause   : {reason}")
    if fix:
        print(f"   Solution : {fix}")
    sys.exit(1)


print("=" * 60)
print(" DIAGNOSTIC CONNEXION ")
print("=" * 60)

# ─── ÉTAPE 1 : Import de llm.py ─────────────────────────────
print("\n 1- Chargement du module llm.py...")
try:
    import llm
    ok(f"llm.py chargé depuis : {llm.__file__}")
except Exception as e:
    fail("1 - Import llm.py", str(e), "Vérifie que ce script est dans le même dossier que llm.py.")

# ─── ÉTAPE 2 : Vérification Chrome vs ChromeDriver ──────────
print("\n 2- Vérification Chrome & ChromeDriver...")
driver_path = os.path.join(os.path.dirname(os.path.abspath(llm.__file__)), "chromedriver.exe")

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
            "Windows Defender ou SmartScreen bloque peut-être le nouveau chromedriver.exe (Clic droit dessus -> Propriétés -> Débloquer).",
        )

# Détection version Chrome installée
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
        if os.path.isfile(driver_path):
            if chrome_ver.split(".")[0] != driver_ver.split(".")[0]:
                fail(
                    "2 - Incompatibilité de version",
                    f"Chrome est en version {chrome_ver.split('.')[0]} mais ChromeDriver est en version {driver_ver.split('.')[0]}",
                    f"Télécharge le ChromeDriver version {chrome_ver.split('.')[0]} exactement.",
                )
            else:
                ok(f"Versions compatibles (Majeure {chrome_ver.split('.')[0]})")
    except Exception:
        pass

# ─── ÉTAPE 3 : Test d'ouverture minimale de Chrome (Selenium) ─
print("\n 3 - Test d'authentification (get_auth_context)...")
try:
    cert, headers = llm.get_auth_context()
    ok(f"Certificat : {cert}")
    ok(f"Headers récupérés (clés : {list(headers.keys())})")
except Exception as e:
    # On nettoie le gros Stacktrace C++ de chromedriver pour ne garder que la première ligne utile
    err_lines = [line.strip() for line in str(e).splitlines() if line.strip() and not line.strip().startswith("Stacktrace") and "0x7ff" not in line and "(No symbol)" not in line]
    clean_err = " | ".join(err_lines[:3]) if err_lines else str(e).splitlines()[0]

    fix_hint = "Ferme toutes les fenêtres Chrome ouvertes (taskkill /F /IM chrome.exe /T) et réessaie."
    if "user data directory is already in use" in clean_err.lower() or "devtoolsactiveport" in clean_err.lower():
        fix_hint = "Ton profil Chrome est verrouillé ou Chrome bloque le lancement. Ferme Chrome complètement."
    elif "version" in clean_err.lower():
        fix_hint = "La version de chromedriver.exe ne correspond pas à celle de Chrome."

    fail("3 - Récupération Token / Selenium", clean_err, fix_hint)

# ─── ÉTAPE 4 : Test d'appel réel au LLM CIB ─────────────────
print("\n 4 - Test d'envoi d'un message au LLM CIB...")
test_model = "gpt-oss-120b"
try:
    chat = llm.LLMChat(model=test_model, cert=cert, headers=headers)
    # Selon la méthode de ta classe LLMChat (ask, send, chat, ou __call__)
    if hasattr(chat, "ask"):
        reply = chat.ask("Réponds uniquement le mot : OK")
    elif hasattr(chat, "chat"):
        reply = chat.chat("Réponds uniquement le mot : OK")
    elif hasattr(chat, "send"):
        reply = chat.send("Réponds uniquement le mot : OK")
    elif callable(chat):
        reply = chat("Réponds uniquement le mot : OK")
    else:
        methods = [m for m in dir(chat) if not m.startswith("_")]
        ok(f"Objet LLMChat initialisé ! Méthodes dispo : {methods}")
        reply = None

    if reply is not None:
        ok(f"Réponse de {test_model} : {str(reply).strip()[:100]}")
except Exception as e:
    clean_err = str(e).splitlines()[0] if str(e) else repr(e)
    fail("4 - Appel API LLM", clean_err, "Vérifie ta connexion VPN / réseau interne CIB ou le nom du modèle.")

print("\n" + "=" * 60)
print(" TOUT EST OPÉRATIONNEL ! Tu peux lancer ton agent.")
print("=" * 60)
