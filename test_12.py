# 文件IO操作

## 在当前目录下读取一个叫test1.txt的文件
# open函数可以拿到文件的文件流，之后可以读取
f = open("test1.txt","r",encoding='utf-8')

# read操作会记录文件流读到哪，下一次会从未读到的地方开始，如果读完则返回空
## read(x) 表示读多少字节，不填则读完
print(f.read())

## 按行读取 with ~ as f 能够在结束后自动close文件流
with open("test2.txt","r",encoding='utf-8') as f2:
    line = f2.readline()  # 注意readline连换行符也作为读到内容的一部分
    while line != "":
        print(line)
        line = f2.readline()

## 写文件
# 若文件不存在则自动创建
with open("test3.txt","w",encoding='utf-8') as f3:
    f3.write("李白乘舟将欲行\n")
    f3.write("忽闻岸上踏歌声\n")
    f3.write("桃花潭水深千尺\n")
    f3.write("不及汪伦送我情\n")
