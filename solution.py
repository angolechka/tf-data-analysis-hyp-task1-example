import pandas as pd
import numpy as np


chat_id = 266642884 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    successes = np.array([x_success, y_success])
    trials = np.array([x_cnt, y_cnt])
    stat, pval = proportions_ztest(successes, trials, alpha)
    if pval < alpha:
      a = False
    else:
      a = True
 
    return a # Ваш ответ, True или False
