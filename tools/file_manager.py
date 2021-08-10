# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         file_manager
# Description:  
# Author:       guohuanyang
# Date:         2021/8/9
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import os
from config.conf import ACCEPT_SUFFIX


class FileManager:
    def __init__(self, filepath):
        self.path = filepath
        self.suffix, self.filename = self.gen_file_info()

    def gen_file_info(self):
        suffix = self.path.split('.')[-1]
        filename = self.path.rsplit('/')[-1]
        return suffix, filename


class CategoryManager:
    def __init__(self, name, dir_path):
        self.name = name
        self.path = dir_path
        self.stat_num, self.file_list = self.gen_stat()

    def gen_stat(self):
        file_list = []
        for root, dir_name, files in os.walk(self.path):
            for filepath in files:
                filepath = os.path.join(root, filepath)
                file_obj = FileManager(filepath)
                if file_obj.suffix in ACCEPT_SUFFIX:
                    file_list.append(file_obj)
        return len(file_list), file_list
