import json

text_json = ""

try:
    with open("m3/datoteke/user_p02.json", "r") as fr:
        text_json = fr.read()
except Exception as e:
    print(f"Greška: {e}")

dict_json = json.loads(text_json)

print(dict_json)
print()

dict_json_direkt = {}
try:
    with open("m3/datoteke/user_p02.json", "r") as fr:
        dict_json_direkt = json.load(fr)
except Exception as e:
    print(f"Greška: {e}")

print(dict_json_direkt)
