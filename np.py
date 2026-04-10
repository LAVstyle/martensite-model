import numpy as np
import matplotlib.pyplot as plt

t1 = np.linspace(0, 10, 500)
t2 = np.linspace(0, 2*np.pi, 100)
x3 = np.linspace(0, 10, 1000)
y3 = np.exp(-x3)*np.cos(10*x3)

noize = np.random.randn(len(t1))
noizy_signal = np.sin(t1) + noize/5


plt.plot(t1, np.sin(t1) + 0.1, label = "clean")
plt.plot(t2, np.sin(t2*5), label = "0 to 2pi")
plt.plot(t1, noizy_signal, label = 'noizy')
plt.plot(x3, y3, label = 'exp(-x)*cos(10*x)')

plt.legend()
plt.xlabel('t')
plt.ylabel('sin(t)')
plt.title('Sine Wave')

plt.grid()
plt.show()