# coding = utf-8
#!/usr/bin/env python
"""关于深浅拷贝"""
import copy

if __name__ == "__main__":
    person = ['张三', [18,24,46]]

    person2 = list(person)
    person2[0] = '李四'
    person2[1][0] = 19

    # 通过对比发现，person和person2的第二个元素都发生了变化，因为只是浅拷贝，对于成员变量中的对象类型，只是复制了引用，并没有进行复制
    print(person)
    print(person2)

    # 深拷贝 注意，对于不可变类型（比如str，元组）并不存在拷贝的说法，因为不可变，所以引用同一个地方也不会有问题。
    person3 = ['王五',[1,2,3]]
    person4 = copy.deepcopy(person)

    person4[1][0] = 4
    print(person3)
    print(person4)