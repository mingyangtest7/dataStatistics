from config.config import CONFIG
import requests
import yaml
import json
import allure
import pytest
import sys
import os


# @pytest.mark.parametrize(
#     "username,password,expected_code",
#     [
#         ("test01", "adaspace2024", "200"),
#         ("t", "adaspace2024", "401"),
#         ("test02", "adaspace202", "401"),  # 错误verKey的case在下方单独写
#         ("test03", "adaspace2024", "401"),
#         ("test04", "adaspace2024", "401"),
#     ],
#     ids=[
#         "正确账号_正确密码_正确验证码_正确verKey",
#         "错误账号_正确密码_正确验证码_正确verKey",
#         "正确账号_错误密码_正确验证码_正确verKey",
#         "正确账号_正确密码_错误验证码_正确verKey",
#         "正确账号_正确密码_正确验证码_错误verKey"
#     ]
# )

#读取参数化测试数据
def load_cases():
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, "login_cases.json")
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    cases = [(d["username"], d["password"], d["expected_code"]) for d in data]
    ids = [d["id"] for d in data]
    return cases, ids

cases, ids = load_cases()

@pytest.mark.parametrize(
    "username,password,expected_code",
    cases,
    ids=ids
)


def test_login(username, password, expected_code, vercode_and_verkey):
    verCode, verKey = vercode_and_verkey
    payload = {
        "username": username,
        "password": password,
        "verCode": verCode,
        "verKey": verKey
    }
    login_url = f"{CONFIG['base_url']}/am/toLogin"
    resp = requests.post(login_url, json=payload)
    code = str(resp.json()["code"])
    print("响应状态码:", resp.status_code)
    print("响应内容:", resp.json())
    assert code == expected_code, f"预期业务码 {expected_code}，实际 {code}"

#登录使用错误的verkey
def test_login_wrong_verkey(vercode_and_verkey):
    verCode, _ = vercode_and_verkey
    payload = {
        "username": "test04",
        "password": "adaspace2024",
        "verCode": verCode,
        "verKey": "1"  # 错误verKey
    }
    login_url = f"{CONFIG['base_url']}/am/toLogin"
    resp = requests.post(login_url, json=payload)
    code = str(resp.json()["code"])
    assert code == "401"