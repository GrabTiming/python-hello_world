from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Student:
    name: str
    age: int
    grade: str
    rank: int

    def to_dict(self) -> Dict[str, Any]:
        """返回学生信息的字典表示。"""
        return {"name": self.name, "age": self.age, "grade": self.grade, "rank": self.rank}


def __main():
    student = Student(name="Alice", age=20, grade="A", rank=1)
    print(student.to_dict())

if __name__ == "__main__":
    __main()