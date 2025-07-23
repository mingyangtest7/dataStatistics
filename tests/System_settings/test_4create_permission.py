import pytest
import json
import allure
import requests
from config.config import CONFIG

#创建新的权限组
def test_create_permission(get_token):
    url = f"{CONFIG['base_url']}/am/sys/user/edit"
    headers = {"Authorization": get_token}
    payload = {
        "name":"权限测试一号",
        "permissionIDList":["1002","1003","1004","1005","1006",4008,4009,2010,2011,2003,2004,2009,2007,3013,3006,2008,2012,4001,4004,4024,2013,4006,4007,2005,3001,3003,3004,3011,3012,4016,4015,4014,4010,4011,4012,4013,2006],
        "note":""
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    if data["code"] == 200:
        print(f"权限创建成功")
    assert data["code"] == 200
    assert data["msg"] == "success"




#获取新创建权限的id
def test_get_id(get_token):
    url = f"{CONFIG['base_url']}/am/sys/role/listByParam"
    headers = {"Authorization": get_token}
    payload = {
        "pageNo": 1,
        "pageSize": 10000
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    data = data["data"]
    for item in data:
        if item["name"] == "权限测试一号":
            id = item["id"]
            return id




def test_delete_permission(get_token):
    id = test_get_id(get_token)
    url = f"{CONFIG['base_url']}/am/sys/role/deleteRole?roleId={id}"
    headers = {"Authorization": get_token}
    response = requests.get(url, headers=headers)



1943215315234111490
