import json
def user_list(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise (Exception('bunday fayl topilmadi'))
    else:
        return data

def get_user_list(file):
    name=str(input("name:"))
    data = user_list(file)
    for i in data:
        if i['name'] == name.title():
            return i
    return None
def create_user(file:str):
    data=user_list(file)
    user_name={}
    user_name['name'] =input('name:')
    user_name['age']=input('age:')
    user_name['email']=input('email:')
    user_name['interests']=input('interests:')
    user_name['manzil']=input('manzil:')
    data.append(user_name)
    return data



def update_name(file):
    data=user_list(file)
    new_name=str(input('name:'))
    for i in data:
        if new_name.title()==i['name']:
            new_age=int(input(f"{new_name} yoshini nmaga qanchaga uzgartirasz:"))
            i['age']=new_age+i['age']
            return data
    return (f"{new_name} is not found")

def delete_user(file):
    name = str(input('Name : '))
    data = user_list(file)
    index = -1
    for user in data:
        index += 1
        if user['name'] == name:
            del data[index]

        return None
def qoshish(file):
    data=user_list(file)
    with open(file, 'w') as f:
        json.dump(data,f)
        return data
print(delete_user('data.json'))