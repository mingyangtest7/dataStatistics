from fontTools.misc.cython import returns

from config.config import CONFIG
import requests


import pytest
import requests
import base64
import os



#生成独立验证码1
@pytest.fixture(scope='session')
def vercode_and_verkey_1():
    """获取验证码和verKey，并人工输入验证码"""
    url = f"{CONFIG['base_url']}/am/captcha"

    response = requests.get(url, timeout=5)
    response.raise_for_status()
    result = response.json()

    code_key = result['data']['codeKey']
    img_base64 = result['data']['imgBase64']

    # 保存图片到本地
    # 去掉 data URL 前缀
    header, encoded = img_base64.split(',', 1)
    # 解码 Base64 数据
    img_bytes = base64.b64decode(encoded)
    # 写入本地文件
    with open("C:/Users/86176/PycharmProjects/dataStatistics/data/captcha.png", "wb") as f:
        f.write(img_bytes)

    ver_code = input("请输入验证码：").strip()
    return ver_code, code_key


#生成独立验证码2
@pytest.fixture(scope='session')
def vercode_and_verkey_2():
    """获取验证码和verKey，并人工输入验证码"""
    url = f"{CONFIG['base_url']}/am/captcha"

    response = requests.get(url, timeout=5)
    response.raise_for_status()
    result = response.json()

    code_key = result['data']['codeKey']
    img_base64 = result['data']['imgBase64']

    # 保存图片到本地
    # 去掉 data URL 前缀
    header, encoded = img_base64.split(',', 1)
    # 解码 Base64 数据
    img_bytes = base64.b64decode(encoded)
    # 写入本地文件
    with open("C:/Users/86176/PycharmProjects/dataStatistics/data/captcha.png", "wb") as f:
        f.write(img_bytes)

    ver_code = input("请输入验证码：").strip()
    return ver_code, code_key



                                # """系统设置模块"""
#账号有添加账号权限，登录获取token供后面使用
@pytest.fixture(scope='session')
def get_token(vercode_and_verkey_1):
    verCode, verKey = vercode_and_verkey_1
    payload = {
        "username": "test01",
        "password": "adaspace2024",
        "verCode": verCode,
        "verKey": verKey
    }
    login_url = f"{CONFIG['base_url']}/am/toLogin"
    resp = requests.post(login_url, json=payload)
    data = resp.json()
    code = data['code']
    assert code == "200"

    token = data["data"]
    print("获取到的token:", token)
    return token


#账号无添加账号权限，登录获取token供后面使用
@pytest.fixture(scope='session')
def permision_get_token(vercode_and_verkey_2):
    verCode, verKey = vercode_and_verkey_2
    payload = {
        "username": "test04",
        "password": "adaspace2024",
        "verCode": verCode,
        "verKey": verKey
    }
    login_url = f"{CONFIG['base_url']}/am/toLogin"
    resp = requests.post(login_url, json=payload)
    datas = resp.json()
    print(datas)
    assert  datas["code"] == "200"

    permision_token = datas["data"]
    print("获取到的permision_token:", permision_token)
    return permision_token


#获取创建的需求方账号信息，并返回给后面接口使用
@pytest.fixture()
def add_user_information(get_token):
    add_url = f"{CONFIG['base_url']}/am/sys/user/selectUser"
    headers = {"Authorization":get_token}
    payload = {
        "pageSize":10,
        "pageNo":1
    }
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    data = data['data']['list']
    for item in data:
        if item.get('name') == "2" and item.get('account') == "2":
            user_id = item['id']
            # print(f"生成ID：{user_id}")
            user_name = item['name']
            # print(f"显示名称：{user_name}")
            user_account = item['account']
            # print(f"需求类型：{user_account}")
            return user_id, user_name, user_account


#获取创建的交付方账号信息，并返回给后面接口使用
@pytest.fixture()
def add_user_information1(get_token):
    add_url = f"{CONFIG['base_url']}/am/sys/user/selectUser"
    headers = {"Authorization":get_token}
    payload = {
        "pageSize":10,
        "pageNo":1
    }
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    data = data['data']['list']
    for item in data:
        if item.get('name') == "3" and item.get('account') == "3":
            user_id1 = item['id']
            print(f"生成ID：{user_id1}")
            user_name1 = item['name']
            print(f"显示名称：{user_name1}")
            user_account1 = item['account']
            print(f"需求类型：{user_account1}")
            return user_id1, user_name1, user_account1



#获取创建的其他使用者账号信息，并返回给后面接口使用
@pytest.fixture()
def add_user_information2(get_token):
    add_url = f"{CONFIG['base_url']}/am/sys/user/selectUser"
    headers = {"Authorization":get_token}
    payload = {
        "pageSize":10,
        "pageNo":1
    }
    response = requests.post(add_url, headers=headers, json=payload)
    data = response.json()
    data = data['data']['list']
    for item in data:
        if item.get('name') == "2" and item.get('account') == "2":
            user_id2 = item['id']
            print(user_id2)
            user_name2 = item['name']
            print(user_name2)
            user_account2 = item['account']
            print(user_account2)
            return user_id2, user_name2, user_account2

# """数据管理模块"""