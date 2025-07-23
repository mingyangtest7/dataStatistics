# import requests
# from config.config import CONFIG
# import pytest
#
#
#
# @pytest.fixture()
# def get_token(vercode_and_verkey):
#     verCode, verKey = vercode_and_verkey
#     payload = {
#         "username": "test04",
#         "password": "adaspace2024",
#         "verCode": verCode,
#         "verKey": verKey
#     }
#     login_url = f"{CONFIG['base_url']}/am/toLogin"
#     resp = requests.post(login_url, json=payload)
#     data = resp.json()
#     code = data['code']
#     assert code == "200"
#
#     token = data["data"]
#     print("获取到的token:", token)
#     return token










