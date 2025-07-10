"""
统计一个目录下有多少个文件（如果有子目录的话也继续往下统计）
"""
import os

def main():
    dir = "./dirTest"
    res = 0
    for root, dirs, files in os.walk(dir):
        res += len(files)
    print("total count is %s", res)
    pass

if __name__ == '__main__':
    main()