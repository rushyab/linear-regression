import numpy as np

N = 100
with open('data_1d.csv', 'w') as f:
    X = np.random.uniform(low=0, high=100, size=N)
    Y = 2*X + 1 + np.random.normal(scale=5, size=N)
    for i in range(N):
        f.write("%s,%s\n" % (X[i], Y[i]))

