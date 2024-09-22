"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    min_value = 1
    max_value = 101
    predict_number = round((min_value+max_value) / 2)  # предполагаемое число
    
    while number != predict_number:
        count += 1
        if predict_number < number:
            min_value = predict_number + 1
        elif predict_number > number:
            max_value = predict_number - 1
        else:
            break
        predict_number = round((min_value+max_value) / 2)  # предполагаемое число
    return count


def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    min_score = min(count_ls)
    max_score = max(count_ls)
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    print(f'Минимальное количество попыток: {min_score}')
    print(f'Максимальное количество попыток: {max_score}')
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)