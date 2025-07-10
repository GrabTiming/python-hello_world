

class Ice:
    """冰块只有两个属性：冰度和体积"""
    def __init__(self,temperature, volume):
        self.temperature = temperature
        self.volume = volume

class Chocolate:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Milk:
    """牛奶类"""
    def __init__(self,name, price):
        self.name = name
        self.price = price

class Food:
    def __init__(self,name:str,satiety_degree: int):
        self.name = name
        self.satiety_degree = satiety_degree

class Drink:
    """饮料类"""
    def __init__(self,name, temperature, volume):
        pass

class Coke(Drink):
    """可口可乐类"""
    def __init__(self,name, temperature, volume):
        super().__init__(name, temperature, volume)

class Sprite(Drink):
    """雪碧类"""
    def __init__(self,name, temperature, volume):
        super().__init__(name, temperature, volume)

class LemonJuice(Drink):
    """柠檬汁类"""
    def __init__(self,name, temperature, volume):
        super().__init__(name, temperature, volume)
