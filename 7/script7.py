import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


lines_to_skip = 1
values = []

R3 = 12
T = 297
dT = 0.5

with open('input.csv') as csvfile:
    for i in range(lines_to_skip):
        next(csvfile)

    for line in csvfile:
        vector = line.strip().split(",")
        values.append([float(i) for i in vector])

values_array = np.array(values)

u_eb_values = values_array[:, 0]
u_kb_values = values_array[:, 1]

I_k = u_kb_values / R3 * 1000
ln_I_k = np.log(I_k)

half_length = len(u_eb_values) // 2

pars = np.zeros((half_length, 7))
pars[:, 0] = u_eb_values[:half_length]
pars[:, 1] = u_eb_values[half_length:len(u_eb_values)]
pars[:, 2] = ln_I_k[:half_length]
pars[:, 3] = ln_I_k[half_length:]
pars[:, 4] = pars[:, 0] - pars[:, 1]
pars[:, 5] = pars[:, 2] - pars[:, 3]
pars[:, 6] = pars[:, 5] / pars[:, 4]

tg = np.mean(pars[:, 6])
a = math.atan(tg)
print('Среднее значение', tg)
print('Коэффициент Стьюдента', 2.36)

print('Тангенс', tg)
dA = math.sqrt(np.sum((pars[:, 6] - tg)**2)/(len(pars[:, 6])*(len(pars[:, 6])-1)))
print('Стандартная погрешность (среднеарифм)', dA)
dB = math.sqrt((1/9) * ((tg * dT) ** 2) + ((T * dA) ** 2))

print('отношение заряда к пост больцмана', T * tg)
print('Погрешность косвенных измерений', dB)
u_eb_average = sum(u_eb_values) / 16
ln_I_k_average = sum(ln_I_k) / 16
ln_I_0 = ln_I_k_average - tg * u_eb_average
print('дельта тангенс', dA * 2.36)
arr = u_eb_values * tg + ln_I_0
I_0 = math.exp(ln_I_0)

fig, ax = plt.subplots()

ax.scatter(u_eb_values, ln_I_k)
ax.plot(u_eb_values, arr, linewidth=1.2)

ax.set_ylabel(r'$ lnI_{k} $')
ax.set_xlabel(r'$ U_{eb} , V $')

plt.savefig('график1.png', dpi=600)
plt.show()


numbs = np.arange(1, 17)
result_values = np.hstack((numbs.reshape(-1, 1), u_eb_values.reshape(-1, 1), u_kb_values.reshape(-1, 1), I_k.reshape(-1, 1), ln_I_k.reshape(-1, 1)))

file_path = "result1.csv"
np.savetxt(file_path, result_values, delimiter=",")

