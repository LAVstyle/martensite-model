import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# данные
x = np.array([0.0, 0.05, 0.1, 0.2, 0.4, 0.6])
y = np.array([0.0, 0.1, 0.15, 0.35, 0.50, 0.60])

# логистическая функция
def logistic(x, k, x0):
    return 1 / (1 + np.exp(-k * (x - x0)))

# аппроксимация
params, _ = curve_fit(logistic, x, y, p0=[10, 0.2])
k, x0 = params

print(f"k = {k:.3f}, x0 = {x0:.3f}")

# гладкий график
x_fit = np.linspace(0, 0.6, 100)
y_fit = logistic(x_fit, k, x0)

# график
plt.scatter(x, y, label="data")
plt.plot(x_fit, y_fit, label="logistic fit")
plt.legend()
plt.xlabel("Strain")
plt.ylabel("Martensite fraction")
plt.grid()

plt.show()