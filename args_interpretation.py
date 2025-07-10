"""
Python方法参数说明的多种方式示例
"""
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass


# 1. 类型注解（Type Hints）- 最推荐的方式
def greet_user(name: str, age: int = 18, is_vip: bool = False) -> str:
    """
    问候用户

    Args:
        name (str): 用户姓名
        age (int, optional): 用户年龄，默认为18
        is_vip (bool, optional): 是否为VIP用户，默认为False

    Returns:
        str: 问候语

    Raises:
        ValueError: 当姓名为空时抛出异常

    Example:
        >>> greet_user("张三", 25, True)
        'Hello VIP 张三, you are 25 years old!'
    """
    if not name:
        raise ValueError("姓名不能为空")

    prefix = "Hello VIP" if is_vip else "Hello"
    return f"{prefix} {name}, you are {age} years old!"


# 2. 复杂参数类型注解
def process_user_data(
        user_info: Dict[str, Any],
        tags: Optional[List[str]] = None,
        settings: Optional[Dict[str, Union[str, int, bool]]] = None
) -> Dict[str, Any]:
    """
    处理用户数据

    Args:
        user_info: 用户信息字典，必须包含 'name' 和 'email' 键
        tags: 用户标签列表，可选
        settings: 用户设置字典，可选

    Returns:
        处理后的用户数据字典
    """
    result = user_info.copy()
    if tags:
        result['tags'] = tags
    if settings:
        result['settings'] = settings
    return result


# 3. 使用dataclass来定义参数结构
@dataclass
class UserProfile:
    """用户档案数据类"""
    name: str
    email: str
    age: Optional[int] = None
    is_active: bool = True


def create_user_profile(profile: UserProfile) -> Dict[str, Any]:
    """
    创建用户档案

    Args:
        profile: 用户档案对象

    Returns:
        用户档案字典
    """
    return {
        'name': profile.name,
        'email': profile.email,
        'age': profile.age,
        'is_active': profile.is_active
    }


# 4. 使用*args和**kwargs
def flexible_function(*args: str, **kwargs: Any) -> str:
    """
    灵活参数函数

    Args:
        *args: 位置参数，必须是字符串
        **kwargs: 关键字参数，可以是任意类型

    Returns:
        处理结果的字符串
    """
    args_str = ", ".join(args)
    kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    return f"Args: {args_str}, Kwargs: {kwargs_str}"


# 5. 使用Callable类型注解
from typing import Callable


def apply_operation(
        data: List[int],
        operation: Callable[[int], int]
) -> List[int]:
    """
    对数据列表应用操作函数

    Args:
        data: 整数列表
        operation: 操作函数，接受一个整数参数并返回一个整数

    Returns:
        应用操作后的新列表
    """
    return [operation(item) for item in data]


# 6. 使用Literal类型（Python 3.8+）
from typing import Literal


def set_user_status(
        user_id: int,
        status: Literal["active", "inactive", "pending"]
) -> Dict[str, Any]:
    """
    设置用户状态

    Args:
        user_id: 用户ID
        status: 用户状态，只能是 "active", "inactive" 或 "pending"

    Returns:
        更新结果
    """
    return {
        'user_id': user_id,
        'status': status,
        'updated': True
    }


# 7. 使用Union类型（或|操作符，Python 3.10+）
def process_data(data: Union[str, bytes, List[str]]) -> str:
    """
    处理不同类型的数据

    Args:
        data: 可以是字符串、字节或字符串列表

    Returns:
        处理后的字符串
    """
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, bytes):
        return data.decode('utf-8').upper()
    elif isinstance(data, list):
        return ", ".join(data).upper()
    else:
        raise TypeError("不支持的数据类型")


# 使用示例
if __name__ == "__main__":
    # 测试各种函数
    print(greet_user("李四", 30, True))

    user_data = {"name": "王五", "email": "wangwu@example.com"}
    result = process_user_data(user_data, tags=["VIP", "Premium"])
    print(result)

    profile = UserProfile("赵六", "zhaoliu@example.com", 28)
    print(create_user_profile(profile))

    print(flexible_function("a", "b", "c", x=1, y=2))


    # 测试操作函数
    def square(x: int) -> int:
        return x ** 2


    numbers = [1, 2, 3, 4, 5]
    squared = apply_operation(numbers, square)
    print(squared)

    print(set_user_status(123, "active"))
    print(process_data(["hello", "world"]))