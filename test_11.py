# 面向对象练习
## 写一个学生类，需要包含学生姓名、学生各个科目的分数
## 然后要有两个方法，一个是设置学生某一科的分数，另一个是打印学生的全部科目的分数

class Student:
    def __init__(self, name):
        self.name = name
        self.projects = {"数学": 0,"英语": 0 , "语文": 0}

    def setProjectScore(self, project,score):
        self.projects[project] = score
    def printProjects(self):
        for project in self.projects:
            print(f"{project}: {self.projects[project]}分")

student1 = Student("Mike")

student1.setProjectScore("语文", 105)
student1.setProjectScore("数学",120)
student1.printProjects()