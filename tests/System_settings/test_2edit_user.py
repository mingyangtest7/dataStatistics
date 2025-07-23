import pytest
import json
import allure
import requests
from config.config import CONFIG



#需求方账号编辑
def test_edit_Demand(get_token,add_user_information):
    user_id, user_name, user_account = add_user_information
    add_url = f"{CONFIG['base_url']}/am/sys/user/edit"
    headers = {"Authorization": get_token}
    payload = {"name":user_name,
               "account":user_account,
               "roleIdList":["1876561188709568513"],
               "requirementType":1,
               "id":user_id
    }

    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    response.raise_for_status()
    if data['code'] == '200':
        print(f"账号 {user_name} 编辑成功")
    assert data['code'] == '200'
    assert data['msg'] == "success"


#需求方账号启用
def test_Enable_Demand(get_token,add_user_information):
    user_id, user_name, _ = add_user_information
    add_url = f"{CONFIG['base_url']}/am/sys/user/updateActiveById"
    headers = {"Authorization": get_token}
    payload = {"id":user_id,"active": 1}
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    if data['code'] == '200':
        print(f"账号 {user_name} 启用成功")
    assert data['code'] == '200'
    assert data['msg'] == "success"
    assert data['data'] == 1


#需求方账号禁用
def test_disable_Demand(get_token,add_user_information):
    user_id, user_name, _ = add_user_information
    add_url = f"{CONFIG['base_url']}/am/sys/user/updateActiveById"
    headers = {"Authorization": get_token}
    payload = {"id":user_id,"active": 0}
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    if data['code'] == '200':
        print(f"账号 {user_name} 禁用成功")
    assert data['code'] == '200'
    assert data['msg'] == "success"
    assert data['data'] == 1


#需求方重置账号密码
def test_resetPWD_Demand(get_token,add_user_information):
    user_id, user_name, _ = add_user_information
    add_url = f"{CONFIG['base_url']}/am/sys/user/resetPwd"
    headers = {"Authorization": get_token}
    payload = {"id":user_id}
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    if data['code'] == '200':
        print(f"{user_name} 密码重置成功")
    assert data['code'] == '200'
    assert data['msg'] == "success"



#交付方账号编辑
def test_edit_delivery(get_token,add_user_information1):
    user_id1, user_name1, user_account1 = add_user_information1
    add_url = f"{CONFIG['base_url']}/am/sys/user/edit"
    headers = {"Authorization": get_token}
    payload = {"name":user_name1,
               "account":user_account1,
               "roleIdList":["1876561188709568513"],
               "requirementType":1,
               "id":user_id1
    }

    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    response.raise_for_status()
    if data['code'] == '200':
        print(f"账号 {user_name1} 编辑成功")
    assert data['code'] == '200'
    assert data['msg'] == "success"


#交付方账号启用
def test_Enable_delivery(get_token,add_user_information1):
    user_id1, user_name1, _ = add_user_information1
    add_url = f"{CONFIG['base_url']}/am/sys/user/updateActiveById"
    headers = {"Authorization": get_token}
    payload = {"id":user_id1,"active": 1}
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    if data['code'] == '200':
        print(f"账号 {user_name1} 启用成功")
    assert data['code'] == '200'
    assert data['msg'] == "success"
    assert data['data'] == 1


#交付方账号禁用
def test_disable_delivery(get_token,add_user_information1):
    user_id1, user_name1, _ = add_user_information1
    add_url = f"{CONFIG['base_url']}/am/sys/user/updateActiveById"
    headers = {"Authorization": get_token}
    payload = {"id":user_id1,"active": 0}
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    if data['code'] == '200':
        print(f"账号 {user_name1} 禁用成功")
    assert data['code'] == '200'
    assert data['msg'] == "success"
    assert data['data'] == 1


#交付方重置账号密码
def test_resetPWD_Demand(get_token,add_user_information):
    user_id1, user_name1, _ = add_user_information
    add_url = f"{CONFIG['base_url']}/am/sys/user/resetPwd"
    headers = {"Authorization": get_token}
    payload = {"id":user_id1}
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    if data['code'] == '200':
        print(f"{user_name1} 密码重置成功")
    assert data['code'] == '200'
    assert data['msg'] == "success"