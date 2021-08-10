# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         extract_data_manager
# Description:  
# Author:       guohuanyang
# Date:         2021/8/10
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------


class ExtractDataManager:

    def __init__(self, extract_data, record_id):
        self.record_id = str(record_id)
        self.template_name = extract_data.get('template_category') or 'common'
        self.filename = extract_data.get('zip_name', 'common.pdf')
        self.message = extract_data.get('message', '抽取失败')
        self.data_list = extract_data.get(
            'extract_data', {}).get('data', {}).get("List", [])
