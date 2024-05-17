# CRUD
import json
from pprint import pprint
from typing import Union,List,Dict,Tuple,Dict


def user_list(file_path: Optional[str] = None) -> Union[List[Dict[str, Union[str, int]]], str]:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data

    except FileNotFoundError as e:
        return e


def get_user(file_path: str, name: str) -> Optional[Dict[str, Union[str]]]:
    # with open(file_path, 'r') as f:
    #     data = json.load(f)
    #     for user in data:
    #         if user['name'] == name.title():
    #             return user
    data = user_list(file_path)
    if data:
        for user in data:
            if user['name'] == name.title():
                return user
        return None


def create_user(file_path: str):
    data = user_list(file_path)
    user = {}
    user['name'] = input('Enter Name : ')
    user['age'] = int(input('Enter Age : '))
    user['email'] = input('Enter Address : ')
    data.append(user)

    open_and_write_json(file_path, data)

    print('User successfully added ')


def update_user(file_path):
    update_name = input('Enter Name : ').title()
    new_email = input('Enter Email : ').title()
    data = user_list(file_path)
    for user in data:
        if user['name'] == update_name:
            user['email'] = new_email

            open_and_write_json(file_path, data)
            return ('User successfully updated ')
    else:
        return (f'{update_name} not found')


def delete_user(file_path):
    search_name = str(input('Search Name : '))
    data = user_list(file_path)
    index = -1
    for user in data:
        index += 1
        if user['name'] == search_name:
            del data[index]
            open_and_write_json(file_path, data)
            print('User successfully deleted ')


def open_and_write_json(file_path: str, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


print(delete_user('data.json'))

