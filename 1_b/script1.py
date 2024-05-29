import math
import numpy as np
import matplotlib.pyplot as plt


def format_number(value):
    try:
        return f"{float(value):.2f}"
    except ValueError:
        return str(value)


u_values1 = np.array([])

with open('input1.csv') as csvfile:
    for line in csvfile:
        vector = line.strip().split(',')
        u_values1 = np.append(u_values1, [float(i) for i in vector])

mean_u1 = np.mean(u_values1)
delta_u1 = mean_u1 * (0.05 + 0.05 * (10 / mean_u1)) / 100

print('Погрешность прибора:', delta_u1)

delta_arr = np.full(10, delta_u1)
numbs1 = np.arange(1, 11)

res_values1 = np.hstack((numbs1.reshape(-1,1), u_values1.reshape(-1, 1), delta_arr.reshape(-1, 1)))

file_path1 = 'result1.csv'
np.savetxt(file_path1, res_values1, delimiter=',')



u_values2 = np.array([])
d = np.array([])
sq_d = np.array([])

with open('input2.csv') as csvfile:
    for line in csvfile:
        vector = line.strip().split(',')
        u_values2 = np.append(u_values2, [float(i) for i in vector])

mean_u2 = np.mean(u_values2)
delta_u2 = mean_u2 * (0.05 + 0.05 * (10 / mean_u2)) / 100

print('Погрешность прибора:', delta_u2)

for k in range(len(u_values2)):
    d = np.append(d, u_values2[k] - mean_u2)
sq_d = np.square(d)
numbs2 = np.arange(1, 51)

res_values2 = np.hstack((numbs2.reshape(-1,1), u_values2.reshape(-1, 1), d.reshape(-1, 1), sq_d.reshape(-1, 1)))
file_path2 = 'result2.csv'
np.savetxt(file_path2, res_values2, delimiter=',')

r_min = np.min(u_values2)
r_max = np.max(u_values2)
# print(r_min, r_max)

prop_counts = np.array([])
counts, bin_edges = np.histogram(u_values2, bins=13)
for k in range(len(counts)):
    prop_counts = np.append(prop_counts, counts[k] / 50)

# print(counts, bin_edges, prop_counts)
bin_edges = np.delete(bin_edges, -1)

numbs3 = np.arange(1, 14)

res_values3 = np.hstack((numbs3.reshape(-1,1), bin_edges.reshape(-1,1), counts.reshape(-1,1), prop_counts.reshape(-1,1)))

file_path3 = 'result3.csv'
np.savetxt(file_path3, res_values3, delimiter=',')

sigma = math.sqrt(np.sum(sq_d) / (len(u_values2) - 1))
sigma_x = sigma / np.sqrt(len(u_values2))
u2_left = mean_u2 - sigma_x
u2_right = mean_u2 + sigma_x

print('Дисперсия:', sigma)
print('Среднеквадратическая погрешность среднего', sigma_x)
print('Границы интервала:', u2_left, u2_right)

fig1, hist = plt.subplots()
plt.hist(u_values2, bins=6)

fig2, ax = plt.subplots()
ax.scatter(numbs2, u_values2, s=15, color='indigo')

fig1.savefig('plot1.png', dpi=600)
fig2.savefig('plot2.png', dpi=600)

plt.show()

