import requests

URL = "https://www.duckduckgo.com"

response = requests.get(URL)

#print(response.status_code)
print()
#print(response.content)
print()
#print(response.headers)
print()
print(response.text)