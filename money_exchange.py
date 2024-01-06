import requests

url = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
response = url.json()
print(response[0]['rates'])
