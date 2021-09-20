import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
# толщина линии графика
ax.plot(input_values, squares, linewidth=3)
# Заголовок графика и шрифт заголовка
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square ofValue", fontsize=14)
ax.tick_params(axis='both', labelsize=16)

plt.show()
