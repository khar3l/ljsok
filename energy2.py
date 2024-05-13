import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из файлов
ymec = np.loadtxt('mec.txt')
ypot = np.loadtxt('pot.txt')
ykin = np.loadtxt('kin.txt')
x = np.arange(len(ymec))

# Выбор диапазона для увеличенного графика (например, начиная с 50-го тика)
start_tick = 50

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(x[start_tick:], ymec[start_tick:], 'o', color='black', label='Полная механическая энергия')

# Настройка подписей осей и заголовка графика
plt.xlabel('Время работы программы, тиков', fontsize=14)
plt.ylabel('Энергия, у.е.', fontsize=14)
plt.title('График зависимости полной механической энергии от времени (увеличенный)', fontsize=16)

# Включение сетки
plt.grid(True)

# Добавление легенды
plt.legend(loc='best', fontsize=12)

# Отображение графика
plt.show()
