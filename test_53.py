# coding = utf-8
import unittest
from enum import Enum, auto

"""
递归写法，四则运算，解析的那里也包含了一些状态机的思想了，但是没想好怎么设计
"""


class State(Enum):
    START = auto()
    NUMBER = auto()
    OPERATOR = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    END = auto()

class Token(object):
    """单位词项"""
    NUMBER = auto()
    OPERATOR = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()

    def __init__(self, token_type :int ,value :str):
        """

        :param token_type: token类型
        :param value: 实际值
        """
        self.token_type = token_type
        self.value = value

class FormatError(Exception):
    """格式错误"""
    def __init__(self,msg: str = ""):
        self.msg = msg if msg else "格式解析错误"

    def __str__(self):
        return self.msg

class LexicalParser(object):
    """分词器，对一个运算式子分词处理"""

    def __init__(self):
        self.expression = ""
        self.tokens = []
        self.state = State.START
        self.current_number = ""
        self.pos = 0

    def set_expression(self,expression:str):
        self.expression = expression
        self.tokens = []
        self.state = State.START
        self.current_number = ""
        self.pos = 0

    def next(self):
        """跳到下一位置"""
        if self.pos < len(self.expression):
            self.pos += 1
            return self.pos
        else:
            return -1

    def add(self, token :Token):
        self.tokens.append(token)

    def is_operator(self,c:str):
        return c in "+-*/"

    def parse(self):
        self.expression = self.expression.replace(" " ,"")
        while self.pos < len(self.expression):
            c = self.expression[self.pos]
            self.next()
            if self.state == State.START:
                if c.isdigit() or c == '.': # 考虑小数
                    self.current_number = self.current_number + c
                    self.state = State.NUMBER
                elif c == '(':
                    self.state = State.LEFT_PAREN
                    self.tokens.append(Token(Token.LEFT_PAREN ,'('))
                elif c == '-':
                    self.state = State.OPERATOR
                    self.add(Token(Token.OPERATOR,'-'))
                else:
                    raise FormatError()
            elif self.state == State.NUMBER: # 数字
                if c.isdigit() or c == '.':
                    self.current_number = self.current_number + c
                elif c in "+-*/":
                    self.add(Token(Token.NUMBER, self.current_number))
                    self.current_number = ""
                    self.state = State.OPERATOR
                    self.add(Token(Token.OPERATOR ,c))
                elif c == ')':
                    self.add(Token(Token.NUMBER, self.current_number))
                    self.current_number = ""
                    self.state = State.RIGHT_PAREN
                    self.add(Token(Token.RIGHT_PAREN ,c))
                else:
                    raise FormatError()
            elif self.state == State.RIGHT_PAREN:  # 右括号
                if not self.is_operator(c) :
                    raise FormatError()
                self.state = State.OPERATOR
                self.add(Token(Token.OPERATOR ,c))
            elif self.state == State.OPERATOR: # 操作符
                if self.is_operator(c):
                    raise FormatError()
                if c.isdigit() :
                    self.state = State.NUMBER
                    self.current_number = self.current_number + c
                elif c == '(':
                    self.state = State.LEFT_PAREN
                    self.add(Token(Token.LEFT_PAREN ,c))
                else:
                    raise FormatError()
            elif self.state == State.LEFT_PAREN: # 左括号
                if c == '-':
                    self.state = State.OPERATOR
                    self.add(Token(Token.OPERATOR ,c))
                elif c.isdigit():
                    self.current_number = self.current_number + c
                    self.state = State.NUMBER
                elif c == ')':
                    self.state = State.RIGHT_PAREN
                    self.add(Token(Token.RIGHT_PAREN ,c))
                elif c == '(':
                    self.state = State.LEFT_PAREN
                    self.add(Token(Token.LEFT_PAREN ,c))
            else:
                raise FormatError()
        if self.current_number:
            self.add(Token(Token.NUMBER ,self.current_number))

class FormulaCalculator(object):
    """四则运算计算器"""
    def __init__(self, tokens :list[Token]=None):
        self.tokens = tokens
        if self.tokens:
            self.print_tokens()
            self.current_token = self.tokens[0]
            self.pos = 0

    def set_tokens(self,tokens :list[Token]):
        self.tokens = tokens
        if self.tokens:
            self.print_tokens()
            self.current_token = self.tokens[0]
            self.pos = 0

    def print_tokens(self):
        type_names = {
            Token.NUMBER: "NUMBER",
            Token.OPERATOR: "OPERATOR",
            Token.LEFT_PAREN: "LEFT_PAREN",
            Token.RIGHT_PAREN: "RIGHT_PAREN"
        }
        for token in self.tokens:
            token_type_name = type_names.get(token.token_type, "UNKNOWN")
            print(f"Token类型: {token_type_name}, 值: {token.value}")

    def next(self,expected_type:int):
        if self.pos < len(self.tokens) and self.tokens[self.pos].token_type == expected_type:
            self.pos += 1
            self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        else:
            raise FormatError()

    def factor(self) -> float:
        """这里是对于一个简单的完整式子做计算，比如说括号内的算式"""
        token = self.current_token
        try:
            if token.token_type == Token.NUMBER:
                result = float(token.value)
                self.next(Token.NUMBER)
                return result
            elif token.token_type == Token.LEFT_PAREN:
                self.next(token.LEFT_PAREN)
                result = self.expr()
                self.next(token.RIGHT_PAREN)
                return result
            else:
                raise FormatError(f"因子格式错误,{token.value}")
        except Exception as e:
            raise FormatError()


    def term(self) -> float:
        """处理乘除运算"""
        result = self.factor()
        while self.current_token and self.current_token.value in "*/":
            op = self.current_token.value
            self.next(Token.OPERATOR)
            right = self.factor()
            result = result * right if op == '*' else result / right
        return result

    def expr(self) -> float:
        """处理加减运算"""
        result = self.term()
        while self.current_token and self.current_token.value in "+-":
            op = self.current_token.value
            self.next(Token.OPERATOR)
            right = self.term()
            result = result + right if op == "+" else result - right
        return result

    def calculate(self) -> float :
        if not self.tokens:
            return 0
        return self.expr()

class Test(unittest.TestCase):

    def test_basic_addition(self):
        expression = "1+1+4"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 6)

    def test_multiplication(self):
        expression = "1*2"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 2)

    def test_complex_expression(self):
        expression = "1+2*3+4*5"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 27)

    def test_parentheses_expression(self):
        expression = "(1+2)*3"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 9)

    def test_negative_numbers(self):
        expression = "-5+3"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, -2)

    def test_division(self):
        expression = "10/2"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 5)

    def test_decimal_numbers(self):
        expression = "1.5+2.5"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 4.0)

    def test_complex_parentheses(self):
        expression = "((1+2)*3)+(4*5)"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 29)

    def test_subtraction(self):
        expression = "10-3-2"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 5)

    def test_mixed_operations_with_parentheses(self):
        expression = "(10-5)*2+1"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 11)

    def test_nested_parentheses(self):
        expression = "2*((3+2)*2)"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 20)

    def test_division_with_decimals(self):
        expression = "7/2"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 3.5)

    def test_complex_expression_with_negatives(self):
        """格式不合法"""
        expression = "-3+4*-2"
        parser = LexicalParser()
        parser.set_expression(expression)
        with self.assertRaises(FormatError):
            parser.parse()

    def test_zero_multiplication(self):
        expression = "0*100"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 0)

    def test_empty_expression(self):
        expression = ""
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 0)

    def test_single_number(self):
        expression = "42"
        parser = LexicalParser()
        parser.set_expression(expression)
        parser.parse()
        calculator = FormulaCalculator()
        calculator.set_tokens(parser.tokens)
        result = calculator.calculate()
        self.assertEqual(result, 42)

    def test_format_error_invalid_character(self):
        expression = "1+2&3"
        parser = LexicalParser()
        parser.set_expression(expression)
        with self.assertRaises(FormatError):
            parser.parse()

    def test_format_error_consecutive_operators(self):
        expression = "1++2"
        parser = LexicalParser()
        parser.set_expression(expression)
        with self.assertRaises(FormatError):
            parser.parse()
