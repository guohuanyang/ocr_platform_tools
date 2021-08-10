# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         post_extract
# Description:
# Author:       guohuanyang
# Date:         2021/8/9
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import requests

from config.conf import CUR_ENV


class Extractor:

    @staticmethod
    def sync_extract(filepath, ):
        url = CUR_ENV['extract_url']
        filename = filepath.split('/')[-1]
        payload = {'serviceNo': filename}
        files = [
            ('files', open(filepath, 'rb'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(filename, response.status_code)
        return response.json()
