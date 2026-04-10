import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# данные
x = np.array([0.0, 0.05, 0.1, 0.2, 0.4, 0.6])
y = np.array([0.0, 0.1, 0.15, 0.35, 0.50, 0.60])

# функция Аврами
def avrami(x, k, n):
    return 1 - np.exp(-k * x**n)

params, _ = curve_fit(avrami, x, y, p0=[5, 2])
k, n = params

print(f"k = {k:.3f}, n = {n:.3f}")

# график
x_fit = np.linspace(0, 0.6, 100)
y_fit = avrami(x_fit, k, n)

plt.scatter(x, y, label="data")
plt.plot(x_fit, y_fit, label="Avrami fit")
plt.legend()
plt.grid()
plt.show()