# coding: utf-8

import os

import config

from tf_struct import File

class CodeScanner :
    '''扫描代码中的注释.'''
    
    def __init__(self) :
        self.files = []

    #遍历指定根目录下符合条件的文件
    def scan_root_dir(self, rootDir) :
        list_dirs = os.walk(rootDir)
        for root, dirs, files in list_dirs:
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file = File(file_name, file_path)
                if self._is_right_file_(file) :
                    print file.name
                    self.files.append(file)

    #打印符合规则的文件路径
    def print_files(self) :
        for file in self.files :
            file.description()
            print '------------------------'

    #统计函数和注释个数
    def scan(self) :
        for file in self.files :
            file.scan()

    #判断文件是否符合配置文件中的规则
    def _is_right_file_(self, file) :
        if file.name not in config.exclude_files :
            if file.extend() in config.extends :
                return True
        return False
