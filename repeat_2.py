import numpy as np
import matplotlib.pyplot as plt

t_values = np.linspace(0, 10, 500)
clean = np.exp(-0.7*t_values)*np.cos(10*t_values)

noise = 0.05 * np.random.randn(len(t_values))
noisy = clean + noise

#window = 5
#smoothed = np.convolve(noisy, np.ones(window)/window, mode='same')

for w in [3, 10, 30]:
    smoothed = np.convolve(noisy, np.ones(w)/w, mode='same')
    plt.plot(t_values, smoothed, label=f'window={w}')


#plt.plot(t_values, noisy, alpha=0.5, label="noisy")
#plt.plot(t_values, smoothed, label="smoothed")
#plt.plot(t_values, clean, label="clean")
plt.plot(t_values, clean, label='clean', linewidth=2)


plt.legend()
plt.grid()
plt.show()