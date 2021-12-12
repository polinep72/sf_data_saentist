"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_min=1
    predict_max=101
    
    while True:
        count += 1
        predict_number = (predict_max+predict_min)//2 # расчитываем среднее значение между мин и мах значениями
        if number>predict_number: # сравниваем загаданное значение компьютером со средним значением и если оно больше... 
            predict_min = predict_number # то прсиваваем миимальному значению среднее значене.  
        elif number<predict_number: # сравниваем загаданное значение компьютером со средним значением и если оно меньше...
            predict_mmax = predict_number # то прсиваваем максимальному значению среднее значене.
        else: # загаданное значение и среднее значение равны.
            break
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
