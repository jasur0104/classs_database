import json
print("1-0dam malumotlari")
#0-index buyicha elementlarni ajratib olindi 1- odam ning malumotlarini olabmoz
with open('d_json.json','r') as f:
    data = json.load(f)
print(data[0])
with open('d_json.json','r') as file:
    user=json.load(file)
print(user[0]['friends'][1])
print(user[0]['friends'][2])
print(user[0]['friends'][1]['name'])
print(user[0]['friends'][1]['id'])
print(user[0]['friends'][2]['id'])
print(user[0]['friends'][2]['name'])

