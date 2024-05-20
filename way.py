import numpy as np
import matplotlib.pyplot as plt

# Чтение данных из файла way.txt
y = np.array([])
with open('way.txt') as f:
    for line in f:
        y = np.append(y, ((float(line) * 64) ** 0.5))

# Создание оси x (времени)
x = np.linspace(1, len(y) + 1, num=len(y))

# Построение графика
plt.xlabel(r'Время работы программы, тиков', fontsize=14)
plt.ylabel(r'Средний квадрат перемещения частиц, у.е.$^2$', fontsize=14)
plt.title(r'График зависимости перемещения частиц от времени', fontsize=14)
plt.grid(True)
plt.errorbar(x, y, fmt='o', color='black', capsize=3, label=r'Среднее перемещение частиц')
plt.legend(loc='best', fontsize=12)

# Линейная аппроксимация
p = np.polyfit(x, y, 1)
print("Коэффициенты полинома (наклон, пересечение):", p)
yfit = np.polyval(p, x)
plt.plot(x, yfit, color="firebrick", label='Линейная аппроксимация')
plt.legend()

# Вывод графика
plt.show()

# Вычисление коэффициента диффузии и длины свободного пробега
D = p[0] / 6
print("Коэффициент диффузии D:", D)

# Оценка средней скорости частиц
v_x = np.array([])
with open('maxw.txt') as f:
    for line in f:
        v_x = np.append(v_x, float(line))

v_avg = np.mean(np.abs(v_x))
print("Средняя скорость частиц v_avg:", v_avg)

# Оценка длины свободного пробега
lambda_free_path = 3 * D / v_avg
print("Длина свободного пробега λ:", lambda_free_path)

# Дополнительно: анализ поведения графика при малых значениях времени
small_t = x[:10]  # Рассмотрим первые 20 значений времени
small_y = y[:10]
small_p = np.polyfit(small_t, small_y, 1)
print("Коэффициенты полинома для малых t (наклон, пересечение):", small_p)
small_D = small_p[0] / 6
print("Коэффициент диффузии D для малых t:", small_D)
small_lambda_free_path = 3 * small_D / v_avg
print("Длина свободного пробега λ для малых t:", small_lambda_free_path)
