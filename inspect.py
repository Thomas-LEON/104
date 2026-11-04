

import inspect
import re
import requests
import urllib3
import llm

urllib3.disable_warnings()

print("=" * 65)
print("🕵️ INSPECTION DE LLMChat & DU PORTAIL CIB")
print("=" * 65)

# 1. Afficher le code de LLMChat et les URLs de llm.py
print("\n1️⃣  Code de la classe LLMChat dans ton llm.py :")
print("-" * 65)
print(inspect.getsource(llm.LLMChat))
print("-" * 65)

# 2. Afficher toutes les constantes / URLs en haut de llm.py
llm_src = inspect.getsource(llm)
print("\n2️⃣  Toutes les URLs et routes définies dans llm.py :")
for i, line in enumerate(llm_src.splitlines(), 1):
    if any(k in line.lower() for k in ("http", "url", "endpoint", "generate", "model", "api/")):
        print(f"  L{i:03d}: {line}")

# 3. Interroger le serveur CIB pour découvrir les routes et modèles actifs
print("\n3️⃣  Scan des endpoints sur le serveur CIB...")
cert, headers = llm.get_auth_context()

urls = list(dict.fromkeys(re.findall(r'https?://[^\s"\'<>]+', llm_src)))
for u in urls:
    base = u.rstrip(".,;)}]'\"/")
    # On remonte à la racine du domaine/API
    for endpoint in [
        "",
        "/models",
        "/api/models",
        "/v1/models",
        "/config",
        "/api/config",
        "/settings",
        "/api/settings",
        "/assistants",
        "/api/assistants",
        "/conversations",
        "/api/conversations",
        "/health",
        "/docs",
        "/openapi.json",
    ]:
        test_url = base + endpoint
        try:
            r = requests.get(test_url, headers=headers, verify=cert, timeout=6)
            ct = r.headers.get("Content-Type", "")
            print(f"  🌐 GET {test_url} -> Status {r.status_code} ({ct.split(';')[0]})")
            if r.status_code == 200 and "json" in ct.lower():
                preview = r.text[:400].replace("\n", " ")
                print(f"     📦 Réponse JSON : {preview}")
        except Exception as e:
            pass
