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

#1-index buyicha elementlarni ajratib olindi 2- odamning malumotlarini olabmiz
print("2-odam malumotlari")
with open('d_json.json','r') as a:
    name=json.load(a)
print(name[1])
with open('d_json.json','r') as b:
    name=json.load(b)
print(name[1]['_id'])
print(name[1]['index'])
print(name[1]['guid'])
print(name[1]['picture'])
print(name[1]['eyeColor'])
print(name[1]['company'])
print(name[1]['email'])
print(name[1]['address'])
print(name[1]['about'])
print(name[1]['registered'])
print(name[1]['isActive'])
print(name[1]['balance'])
print(name[1]['age'])
print(name[1]['name'])
print(name[1]['gender'])
print(name[1]['phone'])
print(name[1]['tags'])
print(name[1]['tags'][2])
print(name[1]['tags'][3])

#3-odam malumotlari
print("3-odam malumotlari")
with open('d_json.json','r') as a:
    name=json.load(a)
print(name[1])
with open('d_json.json','r') as b:
    name=json.load(b)
print(name[2]['_id'])
print(name[2]['index'])
print(name[2]['guid'])
print(name[2]['picture'])
print(name[2]['eyeColor'])
print(name[2]['company'])
print(name[2]['email'])
print(name[2]['address'])
print(name[2]['about'])
print(name[2]['registered'])
print(name[2]['isActive'])
print(name[2]['balance'])
print(name[2]['age'])
print(name[2]['name'])
print(name[2]['gender'])
print(name[2]['phone'])
print(name[2]['tags'])
print(name[2]['tags'][2])
print(name[2]['tags'][3])




