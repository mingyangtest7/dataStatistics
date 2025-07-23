import pytest
import json
import allure
import requests
from config.config import CONFIG




#有权限账号添加需求类型为需求方账号
# @pytest.fixture(scope='session')
def test_add_user(get_token):
    add_url = f"{CONFIG['base_url']}/am/sys/user/add"
    headers = {"Authorization":get_token}
    payload = {
        "name":"2",
        "account":"2",
        "roleLdLIST":["1"],
        "requirementType":1

    }
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    response.raise_for_status()
    print(response.json())
    assert data['code'] == '200'
    assert data['msg'] == "success"


# @pytest.fixture(scope='session')
#有权限账号添加需求类型为交付方账号
def test_add_user1(get_token):
    add_url = f"{CONFIG['base_url']}/am/sys/user/add"
    headers = {"Authorization":get_token}
    payload = {
        "name":"3",
        "account":"3",
        "roleLdLIST":["1"],
        "requirementType":2

    }
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    response.raise_for_status()
    print(response.json())
    assert data['code'] == '200'
    assert data['msg'] == "success"


# @pytest.fixture(scope='session')
#有权限账号添加需求类型为其他使用者账号
def test_add_user2(get_token):
    add_url = f"{CONFIG['base_url']}/am/sys/user/add"
    headers = {"Authorization":get_token}
    payload = {
        "name":"4",
        "account":"4",
        "roleLdLIST":["1"],
        "requirementType":3

    }
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    response.raise_for_status()
    print(data)
    assert data['code'] == '200'
    assert data['msg'] == "success"


#无权限账号添加账号
# @pytest.fixture(scope='session')
def test_add_permision_user(permision_get_token):
    add_url = f"{CONFIG['base_url']}/am/sys/user/add"
    headers = {"Authorization":permision_get_token}
    payload = {
        "name":"6",
        "account":"6",
        "roleLdLIST":["1"],
        "requirementType":1

    }
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    response.raise_for_status()
    print(response.json())
    assert data['code'] == '1008'
    assert data['msg'] == '未授权，你没有权限访问此功能'
