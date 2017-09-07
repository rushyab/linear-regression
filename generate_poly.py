import numpy as np

N = 100
with open('data_poly.csv', 'w') as f:
    X = np.random.uniform(low=0, high=100, size=N)
    X2 = X*X
    Y = 0.1*X2 + X + 3 + np.random.normal(scale=10, size=N)
    for i in range(N):
        f.write("%s,%s\n" % (X[i], Y[i]))

