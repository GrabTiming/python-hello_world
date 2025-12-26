# -*- coding: utf-8 -*-
# !/usr/bin/env python
import argparse
"""
@Author : Liang2003
@Time   : 2025/12/25 21:14

命令参数解析

nargs 的不同选项
nargs='+'：接收一个或多个参数值，至少需要一个参数
nargs='*'：接收零个或多个参数值
nargs='?'：接收零个或一个参数值
nargs=N（N为数字）：接收N个参数值


"""



def main():
    parser = argparse.ArgumentParser(description="This is a test program.")
    parser.add_argument("-o", "--output", help="output")
    parser.add_argument("-i", "--input", help="input")
    parser.add_argument("-t", "--time", help="time")
    parser.add_argument("-opf", "--output_path_file", help="output path file")
    # 接受多个值
    parser.add_argument("-n", "--number", nargs='+', help="number list", type=int)
    args = parser.parse_args()
    print(args)
    print(f"Numbers received: {args.number}")



if __name__ == "__main__":
    main()
