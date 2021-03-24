def generate_number(N: int, M: int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащими нулями)
    в N-ричной системе исчисления( N <=10 )
    длины M
    :param N:
    :param M:
    :param prefix:
    :return:
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        # print(prefix)
        generate_number(N, M - 1, prefix)

        # print(len(prefix))
        prefix.pop()


generate_number(2, 2)


# либо тоже самое но без цикла for для двоичной системы
def gen_bin(M, prefix=""):
    """

    :param M: длина числа
    :param prefix:
    :return:
    """
    if M == 0:
        print(prefix)
        return
    gen_bin(M - 1, prefix + "0")
    gen_bin(M - 1, prefix + "1")


print(gen_bin(3))


# реализация Генерации всех перестановок

def find(number, A):
    """
    ищет number в А и возвращает True, если такой есть
    False, если такого нет
    :param number:
    :param A:
    :return:
    """
    for x in A:
        if number == x:
            return True
    return False

print()
def generate_permutations(N: int, M: int = -1, prefix=None):
    """
    Генерация всех перестановок в N чисел в M позициях,
    с префиксом prefix
    :param N: количество чисел
    :param M: количество позиций
    :param prefix:
    :return:
    """
    M = N if M == -1 else M  # по умолчанию N чисел в M позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=", ", sep="")
        return
    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()

generate_permutations(3)