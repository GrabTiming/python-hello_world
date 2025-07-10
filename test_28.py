"""
错误处理
"""

def main():
    try:
        x = 10/0
    except ZeroDivisionError as e:
        print("已被除零异常截获" ,e)
    except Exception as e:
        print("普通异常",e)

if __name__ == '__main__':
    main()