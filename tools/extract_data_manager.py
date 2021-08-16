# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         extract_data_manager
# Description:  
# Author:       guohuanyang
# Date:         2021/8/10
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
from config.conf import LAND_TEMPLATE_NAME


class ExtractDataManager:

    def __init__(self, extract_data, record_id):
        self.record_id = str(record_id)
        self.template_name = extract_data.get('template_category') or 'common'
        self.filename = extract_data.get('zip_name', 'common.pdf')
        self.message = extract_data.get('message', '抽取失败')
        self.data_list = extract_data.get(
            'extract_data', {}).get('data', {}).get("List", [])
        self._update_template_name()

    def _update_template_name(self):
        if self.template_name != LAND_TEMPLATE_NAME:
            return
        if len(self.data_list) == 0:
            return
        self.template_name = self.data_list[0].get(
            "模版名称", {}).get("value", LAND_TEMPLATE_NAME)
