import numpy as np
import matplotlib.pyplot as plt

t_values = np.linspace(0, 10, 500)
y_values = np.exp(-0.7*t_values)*np.cos(10*t_values)

noise = 0.05 * np.random.randn(len(t_values))
noisy = y_values + noise

plt.plot(t_values, y_values, label = "clean")
plt.plot(t_values, noisy, label = 'noisy')
plt.plot(t_values, noisy - y_values, label = 'noice only')

plt.xlabel('t')
plt.ylabel('value')
plt.title('Sine')

plt.show()