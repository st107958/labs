import math
import numpy as np
import matplotlib.pyplot as plt


lines_to_skip = 1
values =[]

with open('input.csv') as csvfile:
    for i in range(lines_to_skip):
        next(csvfile)

    for line in csvfile:
        vector = line.strip().split(",")
        values.append([float(i) for i in vector])

values_array = np.array(values)

l_values = values_array[:, 0]
uv_values = values_array[:, 1]
ug_values = values_array[:, 2]
um_values = values_array[:, 3]

result_values = np.hstack((l_values.reshape(-1, 1), uv_values.reshape(-1, 1), ug_values.reshape(-1, 1), um_values.reshape(-1, 1)))

s_y = np.array([])
s_x = np.array([])
s_m = np.array([])

for k in range(len(l_values)):
    s_y = np.append(s_y, l_values[k]/(uv_values[k]*(math.sqrt(2))*2))
    s_x = np.append(s_x, l_values[k] / (ug_values[k] * (math.sqrt(2)) * 2))
    s_m = np.append(s_m, l_values[k] / (um_values[k] * (math.sqrt(2)) * 2))


s_y_mean = np.mean(s_y)
s_x_mean = np.mean(s_x)
dy = np.sqrt(np.sum((s_y - s_y_mean)**2) / 20)
dx = np.sqrt(np.sum((s_x - s_x_mean)**2) / 20)
s_m_mean = np.mean(s_m)
k_m = s_m_mean/s_y_mean

print('Среднее S_y = ', s_y_mean)
print('Среднее S_x = ', s_x_mean)
print('Отклонение S_y = ', dy)
print('Отклонение S_x = ', dx)
print('Среднее значение максимальной чувствительности осциллографа = ', s_m_mean)
print('Максимальный коэффициент усиления осциллографического усилителя = ', k_m)

wave_len = np.array([10, 20, 30, 40])

result_values1 = np.hstack((wave_len.reshape(-1, 1), uv_values.reshape(-1,1), s_y.reshape(-1, 1)))
result_values2 = np.hstack((wave_len.reshape(-1, 1), ug_values.reshape(-1,1), s_x.reshape(-1, 1)))
result_values3 = np.hstack((wave_len.reshape(-1, 1), um_values.reshape(-1,1), s_m.reshape(-1, 1)))

file_path1 = "result1.csv"
file_path2 = "result2.csv"
file_path3 = "result3.csv"
np.savetxt(file_path1, result_values1, delimiter=",")
np.savetxt(file_path2, result_values2, delimiter=",")
np.savetxt(file_path3, result_values3, delimiter=",")

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.scatter(uv_values, s_y)
ax2.scatter(ug_values, s_x)

ax1.set_ylabel(r'$ S_y , mm / V $')
ax2.set_ylabel(r'$ S_x , mm / V $')
ax2.set_xlabel(r'$ U_{eff} , V $')
ax1.set_xlabel(r'$ U_{eff} , V $')

fig1.savefig('график1.png', dpi=600)
fig2.savefig('график2.png', dpi=600)

plt.show()

print(values_array)

