import requests

url = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
response = url.json()

# Wyświetlenie dostępnych walut
available_currencies = [rate['code'] for rate in response[0]['rates']]
print('Available currencies:', available_currencies)

# Wybór waluty do wymiany
while True:
    try:
        currency_to = input('Which currency do you want to exchange to?: ')
        if currency_to not in available_currencies or currency_to == 'PLN':
            raise ValueError('Invalid currency. Please choose a valid foreign currency.')
        
        break
    except ValueError as e:
        print(f'Error: {e}')

# Wybór ilości do wymiany
while True:
    try:
        quantity = float(input('How much PLN do you want to exchange?: '))
        if quantity <= 0:
            raise ValueError('Invalid quantity. Please enter a positive number.')
        
        break
    except ValueError as e:
        print(f'Error: {e}')

# Wyszukiwanie kursu wymiany
rate_to = 0
for rate in response[0]['rates']:
    if currency_to == rate['code']:
        rate_to = float(rate['mid'])
        break

if rate_to == 0:
    print(f'Error: Unable to find exchange rate for {currency_to}.')
else:
    result = quantity / rate_to
    print(f'You will receive {currency_to}: {result:.2f}!')
