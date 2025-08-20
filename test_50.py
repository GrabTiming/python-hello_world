"""
给出一个算式字符串，要求计算正确的结果出来
给出的算式是基础的加减乘除运算，并且支持括号优先级，然后不能出现类似2(1+2)的形式，要以2*(1+2)的形式出现

解题思路：
层层递进，有简易到困难
1. 考虑同级运算
2. 考虑多级运算
3. 考虑带括号的情况
4. 考虑负数情况

"""
import unittest
from numbers import Number


class AtomicFormula:
    """原子式"""

    def __init__(self,factor1:Number,factor2:Number,operation:str):
        self.factor1 = factor1
        self.factor2 = factor2
        self.operation = operation


class Calculator:

    @classmethod
    def calculate1(cls,formula:str):
        """第一版：只考虑同级运算，没有负数，没有括号
        比如说 "123 + 456"
        """
        result = 0
        num = 0
        last_op = '+'
        formula = formula + '+' # 用于处理最后一个数
        for c in formula:
            if c == ' ':
                continue
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if last_op in ['+','-']:
                    op = 1 if last_op == '+' else -1
                    result += num * op
                elif last_op == '*':
                    result = result * num
                else :
                    result /= 1.0*num
                last_op = c
                num = 0
        return result

    @classmethod
    def calculate2(cls,formula:str):
        """第二版：考虑多级运算的情况,不算括号"""
        op_stack = ['+']
        num_stack = [0]
        num = 0
        formula = formula
        for c in formula:
            if c == ' ':
                continue
            if c.isdigit():
                num = num * 10 + int(c)
            else :
                if c in ['+','-']:
                    # 在这一版中，加减是最低优先级的，所以前面的运算不会被当前影响
                    last_op = op_stack.pop()
                    last_num = num_stack.pop()
                    if last_op == '+':
                        num += last_num
                    elif last_op == '-':
                        num = last_num - num
                    elif last_op == '*':
                        num *= last_num
                    else:
                        num =  float(last_num)/num
                else:
                    last_op = op_stack[-1]
                    if last_op == '*':
                        last_num = num_stack.pop()
                        op_stack.pop()
                        num = last_num*num
                    elif last_op == '/':
                        last_num = num_stack.pop()
                        op_stack.pop()
                        num = last_num/float(num)

                op_stack.append(c)
                num_stack.append(num)
                num = 0
                print(f"op: {op_stack}, num: {num_stack}")
        num_stack.append(num)
        while len(num_stack) > 1:
            print(f"op: {op_stack}, num: {num_stack}")
            f1 = num_stack.pop()
            f2 = num_stack.pop()
            op = op_stack.pop()
            if op == '+':
                result = f2 + f1
            elif op == '-':
                result = f2 - f1
            elif op == '*':
                result = f2 * f1
            else:
                result = f2 / f1
            num_stack.append(result)
        return num_stack[0]

    def calculate3(self,formula:str):
        """再在上面的版本中加入对括号的处理
        # todo 如何解决左边是个完整的括号然后右边接运算符的情况
        方法：如果运算符左边是')' 做特殊处理，只压运算符不压 num
        """
        op_stack = ['+']
        num_stack = [0]
        num = 0
        right_flag = False
        for c in formula:
            if c == ' ':
                continue
            if c.isdigit():
                right_flag = False
                num = num * 10 + int(c)
            else :
                if c == '(':
                    op_stack.append(c)
                elif c == ')':
                    num_stack.append(num)
                    num = 0
                    while len(op_stack) > 0 :
                        last_op = op_stack.pop()
                        if last_op == '(':
                            break
                        f1 = num_stack.pop()
                        f2 = num_stack.pop()
                        if last_op == '+':
                            num_stack.append(f2 + f1)
                        elif last_op == '-':
                            num_stack.append(f2 - f1)
                        elif last_op == '*':
                            num_stack.append(f2 * f1)
                        else:
                            num_stack.append(f2*1.0 / f1)
                        print(f"op: {op_stack}, num: {num_stack}")
                    right_flag = True
                else:

                    last_op = op_stack[-1] if len(op_stack) > 0 else None
                    if last_op in ['+','-','*','/']:
                        # todo 要考虑，将之前的优先级比当前运算符高的运算都做了
                        if last_op in ['+', '-']:
                            if c not in ['*','/']:
                                last_num = num_stack.pop()
                                num = last_num + num * (1 if last_op == '+' else -1)
                        else:
                            last_num = num_stack.pop()
                            if last_op == '*':
                                num = last_num * num
                            else:
                                num = last_num*1.0 / num
                    op_stack.append(c)
                    if not right_flag :
                        num_stack.append(num)
                        num = 0
                    right_flag = False
            print(f"op: {op_stack}, num: {num_stack}")
        if not right_flag:
            num_stack.append(num)

        while len(num_stack) > 1:
            print(f"op: {op_stack}, num: {num_stack}")
            f1 = num_stack.pop()
            f2 = num_stack.pop()
            op = op_stack.pop()
            if op == '+':
                result = f2 + f1
            elif op == '-':
                result = f2 - f1
            elif op == '*':
                result = f2 * f1
            else:
                result = f2 / f1
            num_stack.append(result)
        return num_stack[0]

class Test(unittest.TestCase):
    __calculator = Calculator()

    def test1(self):
        formula1 = '123 + 456'
        formula2 = '10 * 11'
        formula3 = '1 + 2 - 3'
        self.assertEqual(self.__calculator.calculate1(formula1), 579)
        self.assertEqual( self.__calculator.calculate1(formula2), 110)
        self.assertEqual( self.__calculator.calculate1(formula3), 0)

    def test2(self):
        formula1 = '1 + 2 * 3'
        self.assertEqual(self.__calculator.calculate2(formula1), 7)
        formula2 = '2*3/3'
        self.assertEqual(self.__calculator.calculate2(formula2), 2)
        formula3 = '3/2*2 + 1*3*2/3 - 3*2'
        self.assertEqual(self.__calculator.calculate2(formula3), -1)
        formula4 = '2+3*5'
        self.assertEqual(self.__calculator.calculate2(formula4), 17)

    def test3(self):
        formula1 = '1 + (1 + 2 )'
        self.assertEqual(self.__calculator.calculate3(formula1), 4)
        formula2 = '2* (2*3)'
        self.assertEqual(self.__calculator.calculate3(formula2), 12)
        formula3 = '3*(2+3*6)'
        self.assertEqual(self.__calculator.calculate3(formula3), 60)
        formula4 = '(2+3)*6'
        self.assertEqual(self.__calculator.calculate3(formula4), 30)
        formula5 = '3*(2+3)-6'
        self.assertEqual(self.__calculator.calculate3(formula5), 9)