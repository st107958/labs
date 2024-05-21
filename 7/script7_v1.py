import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


lines_to_skip = 1
values = []

R3 = 12
T = 297

with open('input1.csv') as csvfile:
    for i in range(lines_to_skip):
        next(csvfile)

    for line in csvfile:
        vector = line.strip().split(",")
        values.append([float(i) for i in vector])

values_array = np.array(values)

u_eb_values = values_array[:,0]
u_kb_values = values_array[:,1]

I_k = u_kb_values / R3
ln_I_k = np.log10(I_k)

half_length = len(u_eb_values) // 2

pars = np.zeros((half_length, 7))
pars[:, 0] = u_eb_values[:half_length]
pars[:, 1] = u_eb_values[half_length:len(u_eb_values)]
pars[:, 2] = ln_I_k[:half_length]
pars[:, 3] = ln_I_k[half_length:]
pars[:, 4] = pars[:, 0] - pars[:, 1]
pars[:, 5] = pars[:, 2] - pars[:, 3]
pars[:, 6] = pars[:, 5] / pars[:, 4]

k = np.mean(pars[:, 6])
a = math.atan(k)
dK = 1.9*(np.std(pars[:, 6]))/(math.sqrt(8))
dT = 0.5
dB = math.sqrt((1/9) * ((k/0.434*dT)**2) + ((T/0.434 * dK) ** 2))
x_average = sum(u_eb_values)/16
y_average = sum(ln_I_k)/16
ln_I_0 = y_average - k * x_average

arr = u_eb_values*k + ln_I_0

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

