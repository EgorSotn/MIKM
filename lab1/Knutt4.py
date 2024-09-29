import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
a = 0.1   # вероятность рождаемости жертв
b = 0.02  # вероятность смертности жертв при встрече с хищником
c = 0.1   # вероятность убыли хищников при нехватке еды
d = 0.01  # вероятность достаточности еды для размножения хищников

# Начальные условия
V0 = 40   # начальное количество жертв
P0 = 9    # начальное количество хищников
t0 = 0    # начальное время
t_end = 200  # конечное время
h = 0.1   # шаг времени

# Определение функции для системы уравнений
def lotka_volterra(t, V, P):
    dV_dt = (a - b * P) * V
    dP_dt = (-c + d * V) * P
    return dV_dt, dP_dt

# Метод Рунге-Кутты 4-го порядка
def runge_kutta_4(t0, V0, P0, t_end, h):
    t_values = np.arange(t0, t_end, h)
    V_values = []
    P_values = []

    V = V0
    P = P0

    for t in t_values:
        V_values.append(V)
        P_values.append(P)

        # Вычисляем коэффициенты k1, k2, k3, k4
        k1_V, k1_P = lotka_volterra(t, V, P)
        k2_V, k2_P = lotka_volterra(t + 0.5 * h, V + 0.5 * h * k1_V, P + 0.5 * h * k1_P)
        k3_V, k3_P = lotka_volterra(t + 0.5 * h, V + 0.5 * h * k2_V, P + 0.5 * h * k2_P)
        k4_V, k4_P = lotka_volterra(t + h, V + h * k3_V, P + h * k3_P)

        # Обновляем значения V и P
        V += (h / 6) * (k1_V + 2 * k2_V + 2 * k3_V + k4_V)
        P += (h / 6) * (k1_P + 2 * k2_P + 2 * k3_P + k4_P)

    return t_values, V_values, P_values

# Запускаем метод Рунге-Кутты
t_values, V_values, P_values = runge_kutta_4(t0, V0, P0, t_end, h)

# Построение графиков численности хищников и жертв
plt.figure(figsize=(10, 5))
plt.plot(t_values, V_values, label='Жертвы V(t)', color='blue')
plt.plot(t_values, P_values, label='Хищники P(t)', color='red')
plt.xlabel('Время t')
plt.ylabel('Популяция')
plt.title('Динамика численности жертв и хищников')
plt.legend()
plt.grid(True)
plt.show()

# Фазовая диаграмма
plt.figure(figsize=(6, 6))
plt.plot(V_values, P_values, color='green')
plt.xlabel('Жертвы V')
plt.ylabel('Хищники P')
plt.title('Фазовая диаграмма (Жертвы vs Хищники)')
plt.grid(True)
plt.show()
