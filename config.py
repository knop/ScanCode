# coding: utf-8

#需要扫描的目录
sources = ['/Users/xh_chen/Develop/Python',
           '/Users/xh_chen/Develop/here/Here/Classes',
           '/Users/xh_chen/Develop/Meal/src']

#支持的文件扩展名
extends = ['.cs', '.m', '.py', '.java']

regexps = {'.py': ['\\s*def\\b.+(.+)\\s:', '(.*#.*)|(.*\'\'\'.*\'\'\'.*)', '.*\'\'\'.*', '.*\'\'\'.*'],
           '.m': ['[-+]\\s?(.*).*', '.*//.*|(.*/\*.*\*/.*)', '.*/\*.*', '.*\*/.*'],
           '.java': ['\\s*def\\b.+(.+)\\s:', '\\s*#.*|\\s*\'\'\'.*\'\'\'', '\\s*\'\'\'\\w*', '\\s*\\w*\'\'\'']}

#需要过滤的文件名
exclude_files = ['R.java']
