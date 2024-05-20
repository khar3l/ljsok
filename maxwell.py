import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Чтение данных из файла
y = np.array([])
with open('maxw.txt') as f:
    for line in f:
        y = np.append(y, float(line))

v_x = y
N = len(v_x)

# Расчет температуры системы
T = np.sum(v_x**2) / N

# Вывод температуры
print("Температура системы:", T)

# Плотность вероятности (KDE) для эмпирических данных
kde = gaussian_kde(v_x)
v_x_range = np.linspace(min(v_x), max(v_x), 1000)
kde_values = kde(v_x_range)

# Построение теоретического распределения Максвелла-Больцмана
m = 1.0  # масса частицы (условная единица)
k_B = 1.0  # постоянная Больцмана (условная единица)
f_vx = np.sqrt(m / (2 * np.pi * k_B * T)) * np.exp(-m * v_x_range**2 / (2 * k_B * T))

# Построение графиков
plt.plot(v_x_range, kde_values, color='green', label='Эмпирическое распределение (KDE)')
plt.plot(v_x_range, f_vx, color='red', label='Теоретическое распределение Максвелла-Больцмана')

plt.title(r'Распределение проекции скоростей частиц на ось X', fontsize=14)
plt.xlabel(r'$v_x$', fontsize=12)
plt.ylabel(r'Плотность вероятности', fontsize=12)
plt.legend()
plt.show()
