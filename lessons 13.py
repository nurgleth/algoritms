# стек или очередь Lifo

"""
Модуль описывающий структуру данных стек
>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
"""

_stack = []  # подчеркнули что это внутренняя переменная не изменяемая


def push(x):
    """
    >>> size = len(_stack)
    >>> push(5)
    >>> len(_stack) - size
    1
    >>> _stack[-1]
    5
    """
    _stack.append(x)


def pop():
    x = _stack.pop()
    return x


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)


# проверка корректности скобочной последовательности
def is_braces_sequence_correst(s: str):
    """
    Проверяет корректность сокобочной последовотельности из круглых
    и квадратных скобок () []
    >>> is_braces_sequence_correst("(([()]))[]")
    True
    >>> is_braces_sequence_correst("([)]")
    False
    >>> is_braces_sequence_correst("]")
    False
    >>> is_braces_sequence_correst("(")
    False
    """
    for brace in s:
        if brace not in "()[]":  # проверяем передали ли нам скобки
            continue
        if brace in "([":
            push(brace)  # описанна выше
        else:
            assert brace in ")]", "Ожидалась скобка закрфвается:" + str(brace)
            if len(_stack) == 0:
                return False
            left = _stack.pop()
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return len(_stack) == 0




if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
_stack2 = []
def pols_natacia(l: list):
    for i in range(l):
        if i != int or i not in "*/+-":
            continue
        if i == int:
            _stack2.append(i)
        else:
            _stack2.append(i)

    return _stack2[0], _stack2[-1],_stack2[1]



