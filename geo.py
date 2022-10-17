import requests


# Получаем Геоданные - расположение карт
BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'

postcode = 'G42 9AY'
street='Санкт-Петербург, Верности 24'
street = '24, Верности'
street = 'Мебельная улица, 49/92'

housenumber = '24 Верности'
streetname = 'Санкт-Петербург'

streetname = 'Мира 1'
housenumber = 'Мебельная улица, 49/92'.replace(' ', '+')
# housenumber = 'наб. реки Екатерингофки, 19'.replace(' ', '+')

city = 'Санкт-Петербург'
# city = 'Ленинградская'

county= 'Ленинградская'


street = f"{housenumber}"         # &{streetname}"     # &{city}"

# response = requests.get(f"{BASE_URL}&street={street}&city={city}")
# response = requests.get(f"{BASE_URL}&street={street}&county={county}")
response = requests.get(f"{BASE_URL}&street={street}&county={county}")      #    &city={city}")
response = requests.get(f"{BASE_URL}&street={street}&city={city}")

print(f"{BASE_URL}&street={street}&city={city}")
print(f"{BASE_URL}&street={street}&county={county}")

print(response.json())
