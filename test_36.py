"""
关于python *号的用法
"""

def main():
    a = [1,2,3,4]
    b = [2,3,4,5]

    print(a)
    print(*a)
    print(b)
    print(*b)
    print(sum(a))
if __name__ == "__main__":
    main()