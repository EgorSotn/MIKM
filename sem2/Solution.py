import numpy as np

# Задача 1: Метод наименьших квадратов
def least_squares(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x**2)

    # Формулы для a и b
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - a * sum_x) / n

    return a, b

# Данные
x = np.array([0, 1, 2, 4, 5])
y = np.array([2.1, 2.4, 2.6, 2.8, 3])

# Решение первой задачи
a, b = least_squares(x, y)
print(f"Уравнение тренда: y = {a:.4f}x + {b:.4f}")

# Задача 2: Метод простых итераций
def iteration_method(epsilon=0.1, max_iter=100):
    # Начальные приближения
    x1, x2, x3 = 0, 0, 0
    x1_new, x2_new, x3_new = x1, x2, x3

    iter_count = 0
    while iter_count < max_iter:
        iter_count += 1

        # Итерационные формулы
        x1_new = (-x2 + x3) / 4
        x2_new = (x1 + x3 - 1) / 5
        x3_new = (x1 - x2) / 4

        # Проверяем условие остановки
        if max(abs(x1_new - x1), abs(x2_new - x2), abs(x3_new - x3)) < epsilon:
            break

        x1, x2, x3 = x1_new, x2_new, x3_new

    return x1_new, x2_new, x3_new, iter_count

# Решение второй задачи
x1_res, x2_res, x3_res, iterations = iteration_method()
print(f"Решение системы: x1 = {x1_res:.4f}, x2 = {x2_res:.4f}, x3 = {x3_res:.4f}")
print(f"Количество итераций: {iterations}")
