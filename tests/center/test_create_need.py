import pytest
import json
import allure
import requests
from config.config import CONFIG


#创建新的权限组
def test_create_needs(get_token):
    url = f"{CONFIG['base_url']}/am/sys/role/addRole"
    headers = {"Authorization": get_token}
    payload = {

    }