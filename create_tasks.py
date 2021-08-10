# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         create_tasks
# Description:  
# Author:       guohuanyang
# Date:         2021/8/9
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------

from tools.file_manager import CategoryManager
from tools.task_manager import TaskManager
from config.conf import CARDS


def gen_task_ids():
    task_ids = []
    for card_name, path in CARDS:
        cat = CategoryManager(card_name, path)
        for file_info in cat.file_list:
            task = TaskManager.create_task(file_info.path)
            records = task['records']
            record_id = records[0]['record_id']
            task_ids.append(record_id)
    return task_ids


def gen_tmp_task_ids(root='./tmp'):
    task_ids = []
    cat = CategoryManager('tmp', root)
    for file_info in cat.file_list:
        task = TaskManager.create_task(file_info.path)
        records = task['records']
        record_id = records[0]['record_id']
        task_ids.append(record_id)
        print(record_id)
    return task_ids


def run_create_task():
    task_ids = gen_task_ids()
    task_ids = map(lambda x: str(x), task_ids)
    with open("task_ids.txt", 'w', encoding='utf-8') as f:
        f.write(",".join(task_ids))
    print('create done')


def run_create_tmp_task():
    task_ids = gen_tmp_task_ids()
    task_ids = map(lambda x: str(x), task_ids)
    with open("task_ids.txt", 'w', encoding='utf-8') as f:
        f.write(",".join(task_ids))
    print('create done')


if __name__ == '__main__':
    run_create_tmp_task()
