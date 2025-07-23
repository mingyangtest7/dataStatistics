import pytest
import json
import allure
import requests
from config.config import CONFIG


#需求方账号删除
def test_delete_user(get_token,add_user_information):
    user_id, _, _ = add_user_information
    add_url = f"{CONFIG['base_url']}/am/sys/user/delete?id={user_id}"
    headers = {"Authorization": get_token}
    response = requests.get(add_url, headers=headers)
    data = response.json()
    response.raise_for_status()
    print(data)
    assert data['code'] == '200'
    assert data['msg'] == "success"
    assert data['data'] == True


#交付方账号删除
def test_delete_user1(get_token,add_user_information1):
    user_id1, _, _ = add_user_information1
    add_url = f"{CONFIG['base_url']}/am/sys/user/delete?id={user_id1}"
    headers = {"Authorization": get_token}
    response = requests.get(add_url, headers=headers)
    data = response.json()
    response.raise_for_status()
    print(data)
    assert data['code'] == '200'
    assert data['msg'] == "success"
    assert data['data'] == True