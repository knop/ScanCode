# coding: utf-8

import config

from scanner import CodeScanner

def main() :
    scanner = CodeScanner()
    for path in config.sources :
        scanner.scan_root_dir(path)
    scanner.scan()
    scanner.print_files()

if __name__ == "__main__" :
    main()
