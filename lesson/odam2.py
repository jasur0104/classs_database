import json
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
