import matplotlib.pyplot as plt

x_values = range(1, 1634)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=4)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square ofValue", fontsize=14)
ax.tick_params(axis='both', labelsize=16)

ax.axis([0, 2000, 0, 3_000_000])

plt.savefig('squares_plot.png', bbox_inches='tight')  # Создать и сохранить изображение
plt.show()  # Отображение диаграммы
