import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000) # создание значений абсцисс
print(len(t))
clean = np.exp(-t) * np.cos(5*t) # чистые значения ординат
noise = 0.3 * np.random.randn(len(t)) # создание случайного шума

signal = clean + noise

df = pd.DataFrame({
    'time': t, # значения оси абсцисс
    'signal': signal, # значения ординат с шумом
    'clean': clean # значения ординат без шума
})

filtered = df[df['signal'] > 0]


print(df.head()) # таблица всех значений
print(df["signal"].mean()) # среднеее значение
print(df["signal"].std()) # сред.квадр.отклонение
print(df['signal'].max()) # макс.значение

for w in [5, 20, 50]:
    smoothed = np.convolve(signal, np.ones(w)/w, mode='same')
    df['smoothed'] = df['signal'].rolling(w).mean()
    plt.plot(df['time'],df['smoothed'], label=f'window={w}')

plt.plot(df['time'], df['signal'], alpha=0.5, label = 'noisy')
plt.plot(df['time'],df['clean'], label = 'clean')
# plt.plot(df['time'], df['smoothed'], label = 'smoothed')

plt.grid()
plt.legend()
plt.show()