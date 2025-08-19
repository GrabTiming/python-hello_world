

def main():
    a = "Hello"
    b = "Hello"

    print(a,id(a))
    print(b,id(b))
    print( a is b)

if __name__ == '__main__':
    main()