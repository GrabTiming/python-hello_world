# coding = utf-8
#!/usr/bin/env python

"""
关于set的操作
"""

def main():
    st1 = set([1,2,3,4,5])
    st2 = set([2,4,5,6,7,8])

    st3 = st1 | st2
    print(st3)

    st4 = st1 & st2
    print(st4)

    st5 = st1 - st2
    print(st5)

    st1.add(6)
    print(st1)

    st1.remove(6)
    print(st1)


if __name__ == '__main__':
    main()
