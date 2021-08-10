# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         login
# Description:  
# Author:       guohuanyang
# Date:         2021/8/10
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------


import requests
import json
from config.conf import CUR_ENV

url = CUR_ENV['login_url']


def login():
    payload = json.dumps({
      "username": "mEpuV/2B5zSKJYlZ5zlipaI4REcBui7C/p+q0gyKxjM=",
      "password": "mEpuV/2B5zSKJYlZ5zlipaI4REcBui7C/p+q0gyKxjM="
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200
    return response.json()
