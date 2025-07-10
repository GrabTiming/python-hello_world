# 字典操作

scoreDict = {}

scoreDict["Mike"] = 100
scoreDict["Jim"] = 90
scoreDict["Amy"] = 80

# 获取字典元素数量
print(len(scoreDict))
print(scoreDict)

# 删除元素
del scoreDict["Jim"]
print(scoreDict)

# 判断元素是否存在字典中,不能通过查询没有的值，会报错
if "Bob" in scoreDict:
    print(scoreDict["Bob"])
else :
    print("No Data")
# 以下这种才是常见的字典使用方法
print(scoreDict.get("Bob",-1))
