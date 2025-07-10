"""
设计一个简单的银行账户管理系统
1.
账户类（BankAccount）：
每个账户有 账号（account_number）、户主姓名（owner_name） 和 余额（balance） 三个属性。
提供 存款（deposit）、取款（withdraw） 和 显示余额（show_balance） 的方法。
取款时检查余额是否足够，如果不足，提示“余额不足”。
每次操作后，打印当前余额。

2. 银行类（Bank）（可选进阶）：
管理多个账户（使用字典存储，键是 account_number，值是 BankAccount 对象）。
提供 开户（create_account）、查询账户（find_account） 和 转账（transfer） 功能。
转账时要检查双方账户是否存在，以及转出账户余额是否足够。
"""

class BankAccount:
    def __init__(self,account_number:str,owner_name:str,balance:float):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def __str__(self):
        return f"账户编号：{self.account_number}\n账户名：{self.owner_name}\n余额：{self.balance}"

    def deposit(self,amount:float):
        self.balance += amount
        print(f"存款成功，当前余额为{self.balance}")

    def withdraw(self,amount:float) -> float:
        withdraw_amount = min(amount, self.balance)
        self.balance -= withdraw_amount
        print(f"取款{withdraw_amount}，当前余额为{self.balance}")
        return withdraw_amount

class Bank:

    accounts = []

    def __init(self):
        pass
    @classmethod
    def create_account(cls,account:BankAccount):
        cls.accounts.append(account)

    @classmethod
    def find_account(cls,account_number:str) -> object:
        for account in cls.accounts:
            if account.account_number == account_number:
                return account
        return None

def main():
    account1 = BankAccount("1234567890","张三",1000)
    account2 = BankAccount("1234567891","李四",2000)
    account3 = BankAccount("1234567892","王五",3000)
    account4 = BankAccount("1234567893","赵六",4000)
    account5 = BankAccount("1234567894","孙七",5000)

    account1.deposit(110.1)
    account1.withdraw(210.1)

    Bank.create_account(account1)
    Bank.create_account(account2)
    Bank.create_account(account3)
    Bank.create_account(account4)
    Bank.create_account(account5)

    print(Bank.find_account("1234567894"))

if __name__ == "__main__":
    main()