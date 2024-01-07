import requests

url = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
response = url.json()

# Wyświetlenie dostępnych walut
available_currencies = [rate['code'] for rate in response[0]['rates']]
print('Available currencies:', available_currencies)

currency = input('Which currency are you interested in?: ')
quantity = int(input('How much do you want to exchange?: '))

for rate in response[0]['rates']:
    if currency == rate['code']:
        result = quantity * float(rate['mid'])
        print(f'You will received {currency}: {result} zlote!')
        break

