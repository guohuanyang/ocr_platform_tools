# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         task_manager
# Description:  
# Author:       guohuanyang
# Date:         2021/8/10
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import requests
from config.conf import CUR_ENV
from tools.login import login
auth_token = {
    "token": ""
}


class TaskManager:
    @staticmethod
    def create_task(filepath, template_name=''):
        if not auth_token["token"]:
            res = login()
            token = res['access_token']
            auth_token["token"] = token
        url = CUR_ENV['create_task_url']

        payload = {
            'template_name': template_name,
            'callback_url': 'http://touhang.com/'}
        files = [
            ('file', open(filepath, 'rb'))
        ]
        headers = {
            'Authorization': "Bearer " + auth_token["token"]
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        assert response.status_code == 200
        return response.json()

    @staticmethod
    def get_task_result(task_id):
        if not auth_token["token"]:
            res = login()
            token = res['access_token']
            auth_token["token"] = token
        url = CUR_ENV['task_detail_url'].format(task_id)

        payload = {}
        files = {}
        headers = {
            'Authorization': "Bearer " + auth_token["token"]
        }

        response = requests.request("GET", url, headers=headers, data=payload, files=files)

        assert response.status_code == 200
        return response.json()

    @staticmethod
    def retry_task(task_id):
        if not auth_token["token"]:
            res = login()
            token = res['access_token']
            auth_token["token"] = token
        url = CUR_ENV['task_retry_url'].format(task_id)

        payload = {}
        headers = {
            'Authorization': "Bearer " + auth_token["token"]
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        assert response.status_code == 200
        return response.json()
