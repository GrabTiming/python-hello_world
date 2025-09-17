# coding = utf-8
#!/usr/bin/env python

"""
来个简单练习：统计字符串中单词的数量
"""


def main():
    s = input('请输入英文语句\n')
    s = s.strip()

    word_list =s.split(' ')
    print(word_list)
    print(len(word_list))

if __name__ == "__main__":
    main()