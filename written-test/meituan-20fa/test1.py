"""
    S = expr (or expr)
    expr = bool (and bool)
"""
class Expression:
    def __init__(self, op, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right
    
    def execute(self):
        left = self.left.execute()
        if self.op == 'or' and left:
            return True
        if self.op == "and" and not left:
            return False
        right = self.right.execute()
        return right

class Bool:
    def __init__(self, bool):
        self.bool = bool
    
    def execute(self):
        if self.bool == "true":
            return True
        return False

class Interpreter:
    def tokenize(self, s):
        return s.split()

    def parse(self, tokens):
        self.index = 0
        self.flag = False
        ast = self.parse_or_expression(tokens)
        if self.flag:
            return None
        return ast

    def parse_or_expression(self, tokens):
        left = self.parse_and_expression(tokens)
        if self.flag or self.index >= len(tokens): return left
        if tokens[self.index] == "or":
            self.index += 1
            right = self.parse_or_expression(tokens)
            return Expression("or", left, right)
        self.flag = True
        return left
    
    def parse_and_expression(self, tokens):
        left = self.parse_bool(tokens)
        if self.flag or self.index >= len(tokens): return left
        if tokens[self.index] == 'or':
            return left
        elif tokens[self.index] == 'and':
            self.index += 1
            right = self.parse_and_expression(tokens)
            return Expression('and', left, right)
        self.flag = True
        return left

    def parse_bool(self, tokens):
        if self.index >= len(tokens):
            self.flag = True
            return None
        bool = tokens[self.index]
        if bool not in ('true', 'false'):
            self.flag = True
        self.index += 1
        return Bool(bool)


source = input()
interpreter = Interpreter()
tokens = interpreter.tokenize(source)
expr = interpreter.parse(tokens)

if expr:
    if expr.execute():
        print("true")
    else:
        print("false")
else:
    print("error")


