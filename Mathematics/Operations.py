
class Constant:
    def __init__(self, n):
        self.value = n

    def evaluate(self):
        return self.value

    def to_string(self):
        return str(self.value)


class Operation:
    def __init__(self, args):
        self.args = [Constant(n) if isinstance(n, int) else n for n in args]


class Addition(Operation):
    def evaluate(self):
        return self.args[0].evaluate() + self.args[1].evaluate()

    def to_string(self):
        return "({0} + {1})".format(self.args[0].to_string(), self.args[1].to_string())


class Subtraction(Operation):
    def evaluate(self):
        return self.args[0].evaluate() - self.args[1].evaluate()

    def to_string(self):
        return "({0} - {1})".format(self.args[0].to_string(), self.args[1].to_string())


class Multiplication(Operation):
    def evaluate(self):
        return self.args[0].evaluate() * self.args[1].evaluate()

    def to_string(self):
        return "({0} * {1})".format(self.args[0].to_string(), self.args[1].to_string())


class Division(Operation):
    def evaluate(self):
        if self.args[1].evaluate() == 0:
            return 0
        try:
            return self.args[0].evaluate() / self.args[1].evaluate()
        except:
            return -66606660666

    def to_string(self):
        return "({0} / {1})".format(self.args[0].to_string(), self.args[1].to_string())


class Exponentiation(Operation):
    def evaluate(self):
        if self.args[1].evaluate() > 10000:
            return -66606660666
        try:
            return self.args[0].evaluate() ** self.args[1].evaluate()
        except:
            return -66606660666

    def to_string(self):
        return "({0} ^ {1})".format(self.args[0].to_string(), self.args[1].to_string())



# Shorthands
Add = Addition
Sub = Subtraction
Mult = Multiplication
Div = Division
Exp = Exponentiation

op_set = [Add, Sub, Mult, Div, Exp]




if __name__ == "__main__":
    from itertools import permutations


    perms = permutations(op_set, 2)
    for op_a, op_b in perms:
        test = op_a([op_b([2, 3]), 4])
        print(test.to_string(), " = ", test.evaluate())
