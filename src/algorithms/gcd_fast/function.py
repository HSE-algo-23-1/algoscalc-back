import time

ERR_A_NOT_INT_MSG = 'Значение параметра a не является целым числом'
ERR_B_NOT_INT_MSG = 'Значение параметра b не является целым числом'
ERR_BOTH_ZERO_MSG = 'Значения параметров a и b равны нулю'


def gcd(a: int, b: int) -> int:
    """Вычисляет наибольший общий делитель двух целых чисел.
    Медленная итеративная реализация.

    :param a: Целое число a.
    :param b: Целое число b.
    :raise TypeError: Если a или b не являются целыми числами.
    :raise ValueError: Если a и b равны нулю.
    :return: Значение наибольшего общего делителя.
    """
    valid_a, valid_b = isinstance(a, int), isinstance(b, int)
    if not valid_a:
        raise TypeError(ERR_A_NOT_INT_MSG)
    if not valid_b:
        raise TypeError(ERR_B_NOT_INT_MSG)
    if a == b == 0:
        raise ValueError(ERR_BOTH_ZERO_MSG)

    a = abs(a)
    b = abs(b)

    # большее значение сохраняем в а
    if a < b:
        a, b = b, a

    while a > b and b != 0:
        a, b = b, a % b

    return a


def main(a: int, b: int) -> dict[str: int, str: float]:
    """Вычисляет наибольший общий делитель двух целых чисел и
    продолжительность вычисления.

    :param a: Целое число a.
    :param b: Целое число b.
    :raise TypeError: Если a или b не являются целыми числами.
    :raise ValueError: Если a и b равны нулю.
    :return: Словарь со значениями НОД и длительности вычисления.
    """
    start_time = time.time()
    gcd_val = gcd(a, b)
    duration = time.time() - start_time
    return {'gcd': gcd_val, 'duration': duration}


if __name__ == '__main__':
    a = -12
    b = -3
    print('Для небольших чисел НОД вычисляется быстро:')
    print(f'a = {a}, b = {b}, gcd = {gcd(a, b)}')

    a = 1000000000
    b = 2
    print('Вычисление НОД с указанными параметрами займет некоторое время...')
    print(main(a, b))
