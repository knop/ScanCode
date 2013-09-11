# coding: utf-8

import os
import linecache
import re

import config

class Function :
    '''函数'''
    #初始化
    def __init__(self, name) :
        self.name = name
        self.annotation_count = 0
        self.line = 0

    #打印Function描述信息
    def description(self) :
        print '[f]:', self.name
        print '[l]:', self.line
        print '[a]:', self.annotation_count

class File :
    '''文件'''

    #初始化
    def __init__(self, name, path) :
        self.name = name #测试
        self.path = path
        self.line = 0
        self.functions = []

    #打印File描述信息
    def description(self) :
        print 'file:', self.name
        print 'path:', self.path
        for function in self.functions :
            function.description()

        #获取文件扩展名
    def extend(self) :
        return os.path.splitext(self.name)[1]

    def scan(self) :
        # print 'file->scan', self.name
        linecache.clearcache()
        lines = linecache.getlines(self.path)
        self.line = len(lines)
        patterns = config.regexps[self.extend()]
        is_multi_begin = False
        function = None
        for line in lines :
            match = self._regex_match_(line, patterns[0]) #查找函数
            if match :
                function = Function(match.group().strip())
                self.functions.append(function)
            if function :
                function.line += 1
                if self._regex_match_(line, patterns[1]) : #查找单行注释
                    # print 'isSingleAnnotation', line
                    function.annotation_count += 1
                else :
                    if is_multi_begin :
                        if self._regex_match_(line, patterns[3]) :  #查找多行注释结束
                            # print 'isMultipleAnnotationEnd', line
                            is_multi_begin = False
                        else :
                            pass
                            # print 'isMultipleAnnotation', line
                        function.annotation_count += 1
                    else :
                        is_multi_begin = self._regex_match_(line, patterns[2]) #查找多行注释开始
                        if is_multi_begin :
                            # print 'isMultipleAnnotationBegin', line
                            function.annotation_count += 1

    #匹配正则表达式
    def _regex_match_(self, text, pattern) :
        p = re.compile(pattern)
        m = p.match(text)
        return m
