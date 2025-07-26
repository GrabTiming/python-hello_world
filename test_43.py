


def main():
    """
        列表copy不能之间用 = 复制
    :return:
    """
    a = [1,2,3,4,5]
    b = a
    c = list(a)
    a.append(1)

    print(a)
    print(b)
    print(c)

    # a 与 b 指向的是 同一个对象
    print(a is b)


if __name__ == "__main__":
    main()