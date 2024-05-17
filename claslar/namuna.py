import json
data=[1,2,3,4,5,6,7,8,9]
with open('data.json', 'w') as f:
    json.dump(data, f)