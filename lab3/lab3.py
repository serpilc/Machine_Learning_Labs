import numpy as np
import matplotlib.pyplot as plt
import csv

age_list = []
exp_list = []
pow_list = []
sal_list = []
with open("team.csv") as f:
    csv_list = list(csv.reader(f))

for row in csv_list:
    if row != csv_list[0]:
        age_list.append(int(row[4]))
        exp_list.append(int(row[6]))
        pow_list.append(float(row[7]))
        sal_list.append(int(row[8]))



x0 = np.ones(len(age_list), dtype=int)
X = np.array([x0, age_list, exp_list, pow_list]).T
print(X)

a1 = X.T

a2 = np.dot(a1, a1.T)
a3 = np.linalg.inv(a2)
a4 = np.dot(a3, a1)
B = np.dot(a4, sal_list)

Y = np.dot(X, B)
U = (Y-sal_list)



plt.scatter(Y, U)
plt.hlines(y=0, xmin=0, xmax=20000)
plt.show()
