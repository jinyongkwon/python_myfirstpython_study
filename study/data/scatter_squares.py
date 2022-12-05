import matplotlib.pyplot as plt

x_values = [1, 5, 3, 2, 4]
y_values = [1, 4, 9, 16, 25]
print(x_values)
print(y_values)

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=20)
ax.plot(x_values, y_values, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()
