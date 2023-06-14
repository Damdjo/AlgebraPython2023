import json

user = {
            "id": 1,
            "firstName": "Petar",
            "lastName": "Peric",
            "username": "pperic",
            "email": "pperic@email.adresa",
            "address": {
                "street": "Ilica 256",
                "city": "Zagreb",
                "zipcode": "10000"
            },
            "phone": "+385 1 8031 564",
            "website": "web.adresa",
            "company": {
                "name": "Medvednica d.o.o.",
                "catchPhrase": "Razvoj specijaliziranih Python aplikacija",
                "bs": "Najbolja poslovna rjesenja"
            }
        }

try:
    with open("m3/datoteke/user_p01.json", "w") as fw:
        json.dump(user,fw)
except Exception as e:
    print(f"Greška: {e}")

try:
    with open("m3/datoteke/user_p02.json", "w") as fw:
        json.dump(user,fw, indent=4)
except Exception as e:
    print(f"Greška: {e}")

