import llm

# 1. On regarde les lignes 1 à 100 et 295 à 320 de llm.py (les URLs et la fonction get_models)
with open(llm.__file__, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.read().splitlines()

print("=== URLS (Lignes 1-90) ===")
for i, l in enumerate(lines[:90], 1):
    if "URL" in l or "http" in l or "def " in l:
        print(f"L{i:03d}: {l}")

print("\n=== FONCTION MODELS (Lignes 295-320) ===")
for i, l in enumerate(lines[294:320], 295):
    print(f"L{i:03d}: {l}")

# 2. On récupère l'auth et on appelle directement l'URL des modèles de llm.py
auth_context = llm.get_auth_context()
cert, headers = auth_context

# Cherche la fonction dans llm.py qui correspond à la ligne 305-315 (ex: get_models / list_models / fetch_models)
models = []
for fn_name in dir(llm):
    if "model" in fn_name.lower() and callable(getattr(llm, fn_name)):
        print(f"\n🔎 Fonction trouvée dans llm.py : llm.{fn_name}()")
        try:
            res = getattr(llm, fn_name)(cert, headers)
            if isinstance(res, list):
                models = res
                break
        except TypeError:
            try:
                res = getattr(llm, fn_name)(auth_context)
                if isinstance(res, list):
                    models = res
                    break
            except Exception as e:
                print(f"   ({e})")

if models:
    print(f"\n✅ {len(models)} MODÈLES ACTIFS TROUVÉS SUR LE SERVEUR CIB :")
    for m in models:
        print(f"   🤖 id = '{m.get('id')}'  |  title = '{m.get('title')}'")

    # 3. On teste le premier modèle officiel de la liste !
    first_id = models[0]["id"]
    print(f"\n⏳ Test de chat.say() avec le vrai modèle : '{first_id}'...")
    try:
        chat = llm.LLMChat(model_id=first_id, auth_context=auth_context)
        print("🎉 RÉPONSE DU LLM :", chat.say("Dis juste OK"))
    except Exception as e:
        print("❌ ERREUR COMPLÈTE :\n", e)
