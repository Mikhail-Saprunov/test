from builtins import type

import requests


status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})

print("Статус ответа от сервера на GET запрос список питомцев: ",res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))


import json

# добавление питомца
info = {
"id": 0,
"category": {"id": 2,"name": "Cat"},
"name": "Qwert",
"photoUrls": ["string"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}
res_post_addNewPet = requests.post(f"https://petstore.swagger.io/v2/pet",
                                  headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data = json.dumps(info, ensure_ascii=False))
print(f"Статус ответа от сервера на POST запрос добавление питомца: {res_post_addNewPet.status_code}")