import numpy as np
from scipy import stats

# Задаем значения роста для каждой группы спортсменов
football_players = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

# Проводим однофакторный дисперсионный анализ
f_value, p_value = stats.f_oneway(football_players, hockey_players, weightlifters)

# Выводим результаты
alpha = 0.05  # Уровень значимости
print("Результаты однофакторного дисперсионного анализа:")
print("F-статистика:", f_value)
print("p-значение:", p_value)
if p_value < alpha:
    print("Существуют статистически значимые различия между средними ростами групп.")
else:
    print("Нет статистически значимых различий между средними ростами групп.")
