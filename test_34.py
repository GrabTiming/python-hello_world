"""
 实现 ShoppingCart 购物车
 可以增加物品，删除物品，统计总价
"""
from subprocess import check_output
from typing import Dict


class Product:

    def __init__(self,name: str,price: float):
        self.name = name
        self.price = price

    # 要作为字典的key，需要实现eq和hash魔法方法
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name,self.price))

class ShoppingCart:

    def __init__(self):
        self.product_list = Dict[Product,int] = {}

    def add_item(self,product_name: str,price: float,count: int=1):
        product = Product(product_name,price)
        if product in self.product_list :
            self.product_list[product] += count
        else :
            self.product_list[product] = count

    def remove_item(self,product_name: str,count: int):
        need_remove = []
        for product,quantity in self.product_list.items():
            if product.name == product_name:
                if quantity <= count :
                    need_remove.append(product)
                else :
                    self.product_list[product] -= count

        for product in need_remove :
            del self.product_list[product]



def main():
    cart = ShoppingCart()
    cart.add_item("Apple", 2.5, 3)
    cart.add_item("Banana", 1.0)
    cart.remove_item("Apple", 1)
    print(cart.calculate_total())  # 输出总价
    cart.show_cart()  # 显示剩余商品

if __name__ == '__main__':
    main()