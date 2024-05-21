import math
import numpy as np
import matplotlib.pyplot as plt


lines_to_skip = 1
values = []

h = 0.272
v_0 = 1.050
d_h = 0.001
d_v_0 = 0.005
density_arr = np.array([2.79, 8.5, 7.9, 0.7, 1.18, 11.34]) # г/см^3
diameter_arr = np.full(6, 1)

with open('input.csv') as csvfile:
    for i in range(lines_to_skip):
        next(csvfile)

    for line in csvfile:
        vector = line.strip().split(",")
        values.append([float(i) for i in vector])

values_array = np.array(values)
num_cols = values_array.shape[1]

print(num_cols)

mass = np.array([])
mean_time = np.array([])
d_time = np.array([])
g = np.array([])
f1 = np.array([])
f2 = np.array([])
f3 = np.array([])
d_g = np.array([])

for k in range(num_cols):
    mass = np.append(mass, density_arr[k] * (4 * math.pi * (0.0005 ** 3) * 1000 / 3))
    mean_time = np.append(mean_time, np.mean(values_array[:, k]))
    d_time = np.append(d_time, np.sqrt(np.sum((values_array[:, k] - mean_time[k])**2) / (29*30)))
    g = np.append(g, 2 * (h - v_0 * mean_time[k] / 1000) / ((mean_time[k] / 1000) ** 2))
    f1 = np.append(f1, -4 * h / ((mean_time[k] / 1000) ** 3) + 2 * v_0 / ((mean_time[k] / 1000) ** 2))
    f2 = np.append(f2, 2 / ((mean_time[k] / 1000) ** 2))
    f3 = np.append(f3, -2 / (mean_time[k] / 1000))
    d_g = np.append(d_g, np.sqrt((f1[k] ** 2) * ((d_time[k] / 1000) ** 2) + (1 / 9) * (f2[k] ** 2) * (d_h ** 2) + (1 / 9) * (f3[k] ** 2) * (d_v_0 ** 2)))

mass_mg = mass * (10**6)

numbs = np.arange(1, 31)
names = ['Алюминий', 'Латунь', 'Сталь', 'Дерево', 'Плексиглас', 'Свинец']
res1 = np.hstack((numbs.reshape(-1,1), values_array[:, 0].reshape(-1,1), values_array[:, 1].reshape(-1,1), values_array[:, 2].reshape(-1,1), values_array[:, 3].reshape(-1,1), values_array[:, 4].reshape(-1,1), values_array[:, 5].reshape(-1,1)))
res2 = np.hstack((density_arr.reshape(-1,1), diameter_arr.reshape(-1,1), mass_mg.reshape(-1,1)))
res3 = np.hstack((mean_time.reshape(-1,1)))
res4 = np.hstack((d_time.reshape(-1,1)))
res5 = np.hstack((g.reshape(-1,1)))
res6 = np.hstack((d_g.reshape(-1,1)))

file_path1 = "result1.csv"
np.savetxt(file_path1, res1, delimiter=",")
file_path2 = "result2.csv"
np.savetxt(file_path2, res2, delimiter=",")
file_path3 = "result3.csv"
np.savetxt(file_path3, res3, delimiter=",")
file_path4 = "result4.csv"
np.savetxt(file_path4, res4, delimiter=",")
file_path5 = "result5.csv"
np.savetxt(file_path5, res5, delimiter=",")
file_path6 = "result6.csv"
np.savetxt(file_path6, res6, delimiter=",")

