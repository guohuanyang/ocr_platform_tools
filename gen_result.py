# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         gen_result
# Description:  
# Author:       guohuanyang
# Date:         2021/8/10
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import datetime
from collections import defaultdict
from tools.extract_data_manager import ExtractDataManager
from tools.excel_manager import ExcelManager
from tools.task_manager import TaskManager
from config.conf import TEMPLATE_NAME_DICT, START, LIMIT


def get_task_ids(task_ids_path='task_ids.txt'):
    with open(task_ids_path, 'r') as f:
        task_ids = f.read().split(',')
    return task_ids


def get_extract_data(task_id):
    res = TaskManager.get_task_result(task_id)
    extract_obj = ExtractDataManager(res, task_id)
    print(task_id, 'done')
    return extract_obj


def gen_excel(excel_filepath, task_ids_path):
    task_ids = get_task_ids(task_ids_path)[START:]
    extract_obj_list = [get_extract_data(task_id) for task_id in task_ids]
    tpl_index = {}
    for template_name, fields_item in TEMPLATE_NAME_DICT.items():
        tpl_index[template_name] = {}
        for index, field_name in enumerate(fields_item):
            tpl_index[template_name][field_name] = index

    result = defaultdict(list)
    for template_name, fields_item in TEMPLATE_NAME_DICT.items():
        result[template_name].append(["record_id", 'filename', 'message']+list(fields_item.keys()))

    for extract_obj in extract_obj_list:
        template_name = extract_obj.template_name
        rows = [extract_obj.record_id, extract_obj.filename, extract_obj.message]
        if template_name not in tpl_index or template_name not in result or template_name == 'common':
            result[template_name].append(rows)
            continue
        for page_data in extract_obj.data_list:
            rows = [extract_obj.record_id, extract_obj.filename, extract_obj.message]
            rows += ['']*20
            for field_name in page_data:
                try:
                    rows[tpl_index[template_name][field_name]+3] = page_data[field_name]['value']
                except Exception as e:
                    print(e)
                    print(extract_obj.record_id, extract_obj.template_name)
                    continue

            result[template_name].append(rows)

    excel_obj = ExcelManager(excel_filepath)
    for template_name in TEMPLATE_NAME_DICT:
        excel_obj.create_sheets(template_name)
        excel_obj.write_excel(template_name, result[template_name])

    excel_obj.save()


if __name__ == '__main__':
    excel_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.xlsx'
    task_path = 'task_ids_国土房权.txt'
    gen_excel('./result/{}'.format(excel_name), task_path)
