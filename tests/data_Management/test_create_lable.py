import pytest
import json
import allure
import requests
from config.config import CONFIG


#更新地址位置标签
def test_create_location(get_token):
    url = f"{CONFIG['base_url']}/am/bus/tag/updateById"
    headers = {"Authorization": get_token}
    payload = {
        "type": 2,
        "name": "测试添加11",
        "id": "1876898472914948097"
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    if data["code"] == 200:
        print("地理位置标签修改成功")

    assert  data["code"] == 200
    assert  data["data"] == "修改成功"
    assert  data["msg"] == "success"
