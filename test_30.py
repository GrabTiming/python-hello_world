"""
一个学生管理系统
0. 退出
1. 添加学生成绩
2. 查看所有学生成绩
3. 查询特定学生成绩
4. 计算平均成绩

"""

class Student:

    def __init__(self, name:str, score:int):
        self.name = name
        self.score = score

    def add(self,Student):
        self.students.append(Student)

def main():
    students = []
    op = 0
    while True :
        try : 
            op = int(input("请输入: 0 退出; 1 添加学生成绩 2 查看所有学生成绩 3 查询学生成绩 \n"))
        except Exception as e:
            print("输入类型有误，请重新输入\n")
            continue 

        if op == 0:
            break 
        if op == 1:
            name = input("请输入学生姓名：\n")
            score = int(input("请输入学生成绩：\n"))
            student = Student(name, score)
            students.append(student)
        elif op == 2:
            for student in students:
                print(f"{student.name} 的成绩是 {student.score}")
        elif op == 3:
            name = input("请输入学生姓名：\n")
            for student in students:
                if student.name == name:
                    print(f"{student.name} 的成绩是 {student.score}")
                    break




if __name__ == '__main__':
    main()