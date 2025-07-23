import pytest
import json
import allure
import requests
from config.config import CONFIG



#需求方账号编辑
def test_edit_user(get_token,add_user_information):
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
    print(data)
    assert data['code'] == '200'
    assert data['msg'] == "success"


#交付方账号编辑
def test_edit_user1(get_token,add_user_information1):
    user_id1, user_name1, user_account1 = add_user_information
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
    print(data)
    assert data['code'] == '200'
    assert data['msg'] == "success"