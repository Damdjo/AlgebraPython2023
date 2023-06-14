import urllib.request
import urllib.parse

upit = "programiranje u pythonu"
encodiran_upit = urllib.parse.quote(upit)
encodiran_upit_utf8 = encodiran_upit.encode("utf-8")

URL_GOOGLE = f"https://duckduckgo.com/?q{encodiran_upit_utf8}"

print(URL_GOOGLE)

request = urllib.request.Request(URL_GOOGLE)
response = urllib.request.urlopen(request)
response_data = response.read().decode()

print(response_data)
