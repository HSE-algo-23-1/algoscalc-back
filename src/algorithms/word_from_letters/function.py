import time

from pymorphy3 import MorphAnalyzer


LENGTH_LIMIT = 7
"""Предельная длина строки"""
WORDS = 'words'
"""Ключ для словаря с результатом работы функции main"""


def generate_permutations(letters_str: str) -> list[str]:
    """Генерирует все варианты перестановок символов указанной строки
    :param letters_str: входящая строка
    :return: список перестановок символов входящей строки, где каждая
    перестановка строка, содержащая указанные символы
    """
    __validate(letters_str)

    if len(letters_str) < 1:
        return ['']
    if len(letters_str) == 1:
        return [letters_str]

    letters_list = list(letters_str.lower())
    letters_list = __generate_permutations_iter(letters_list)
    # объединение вложенных списков в строки
    return ["".join(lst) for lst in letters_list]


def __validate(letters_str: str) -> None:
    """Вспомогательная функция для валидации строки
    :param letters_str: входящая строка
    :raise TypeError: если параметр не является строкой
    :raise ValueError: если входящая строка содержит пробел или ее длина
    превышает максимально возможное значение
    """
    if not isinstance(letters_str, str):
        raise TypeError('Переданный параметр не является строкой')
    if len(letters_str) > LENGTH_LIMIT:
        raise ValueError(f'Длина введенной строки превышает '
                         f'{LENGTH_LIMIT} символов')
    if ' ' in letters_str:
        raise ValueError('Введенная строка содержит пробел')


def __generate_permutations_iter(letters_list: list[str]) -> list[list[str]]:
    """Вспомогательная функция для генерации перестановок элементов
    итеративным методом
    :param letters_list: список из строковых символов
    :return: список перестановок, где каждая перестановка список элементов
    списка
    """
    permutations_list = [[letters_list.pop()]]  # список со всеми перестановками

    while letters_list:  # пока множество содержит элементы для перестановок
        # список, содержащий перестановки всех элементов в одной итерации
        permutations_iteration_list = []
        # текущий элемент, с которым будут генерироваться перестановки
        current_item = letters_list.pop()
        # обход вложенных списков перестановок с добавлением нового элемента
        for permutation in permutations_list:
            permutation.append(current_item)
            # добавление главной перестановки в итерационный список
            permutations_iteration_list.append(permutation)

            # переставление нового элемента местами на различные позиции
            for pos in range(len(permutation)-1):
                # создание списка для перестановки элементов
                pmt_lst = [item for item in permutation]
                # если элементы одинаковы, то перестановка не имеет смысла -
                # пропускаем итерацию
                if pmt_lst[-1] == pmt_lst[pos]:
                    continue
                # перестановка двух элементов
                pmt_lst[-1], pmt_lst[pos] = pmt_lst[pos], pmt_lst[-1]
                # если сгенерированная перестановка уже содержится в
                # итерационном списке перестановок или в общем списке
                # - пропускаем итерацию цикла
                if pmt_lst in permutations_iteration_list or \
                        pmt_lst in permutations_list:
                    continue
                # добавление получившийся перестановки во временный список
                permutations_iteration_list.append(pmt_lst)
        # добавление всех итерационных перестановок в общий список
        permutations_list = permutations_iteration_list

    return permutations_list


def main(letters: str) -> dict[str, list[str]]:
    """Генерирует слова, составленные из символов входящей строки. Из символов
    генерируются все возможные перестановки, которые проверяются через словарь
    с помощью библиотеки pymorphy3
    :param letters: входящая строка
    :raise TypeError: если параметр не является строкой
    :raise ValueError: если входящая строка содержит пробел или ее длина
    превышает максимально возможное значение
    :return: словарь, содержащий в качестве значения список существующих слов
    """
    morph = MorphAnalyzer()
    exist_words = []  # список существующих слов
    # получение списка со всеми перестановками
    permutations_letters = generate_permutations(letters)

    for word in permutations_letters:  # перебор перестановок
        if morph.word_is_known(word):  # если перестановка - существующее слово
            exist_words.append(word)  # добавление в список существующих слов

    return {WORDS: exist_words}


if __name__ == '__main__':
    letters = 'abc'
    print(generate_permutations(letters))

    start_time = time.time()
    letters = 'Поледар'
    print(main(letters))
    print(f'duration: {time.time() - start_time} seconds')
