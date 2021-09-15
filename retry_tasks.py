# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         retry_tasks
# Description:  
# Author:       guohuanyang
# Date:         2021/8/13
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
from time import sleep
from tools.task_manager import TaskManager


def get_task_ids(task_ids_path='retry_ids.txt'):
    with open(task_ids_path, 'r', encoding='utf-8') as f:
        task_ids = f.read().split(',')
    return task_ids


def run_retry_task(filename):
    task_ids = get_task_ids(filename)
    task_ids = list(set(task_ids))
    # task_ids = [1386]
    task_ids = map(lambda x: str(x), task_ids)
    for task_id in task_ids:
        res = TaskManager.retry_task(task_id)
        sleep(4)
        print(task_id, res['message'])


if __name__ == '__main__':
    run_retry_task('v1-1.txt')
    # run_retry_task('task_ids.txt')
    # run_retry_task('task_ids_1.txt')
