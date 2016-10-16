from __future__ import unicode_literals, print_function
from pypeg2 import *

########################################################################################################################
# ARITHMETIC
########################################################################################################################

number = re.compile(r"\d+")


class ArithmeticExpression(List):
    pass


class Value(List):
    grammar = [
        number,
        name(),
        ("(", ArithmeticExpression, ")")
    ]


class Sum(List):
    grammar = "+"


class Difference(List):
    grammar = "-"


class Multiplication(List):
    grammar = "*"


class Division(List):
    grammar = "/"


class Priority1(List):
    grammar = Value, maybe_some([Multiplication, Division], Value)


class Priority2(List):
    grammar = Priority1, maybe_some([Sum, Difference], Priority1)


ArithmeticExpression.grammar = Priority2

########################################################################################################################
