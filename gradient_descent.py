import numpy as np
import matplotlib.pyplot as plt

N = 10
D = 3
X = np.zeros((N, D))
X[:,0] = 1   # bias term
X[:5,1] = 1  # assign first 5 values as 1
X[5:,2] = 1	 # assign last 5 values as 1
Y = np.array([0]*5 + [1]*5)

# print X so you know what it looks like
print("X:", X)

# won't work! X.T.dot(X) is a singular matrix
# w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))

# Gradient descent: w = w - learning_rate*(d(cost)/dw)
# cost function in matrix form: (Y- Yhat)**2 = (Y - Xw).T (Y - Xw)
# solving further: Y.T Y - Y.T (Xw) - (Xw).T Y + (Xw).T (Xw)
# diffrentiate cost function w.r.t w:
# d(cost)/dw = - 2 X.T Y + 2 X.T (Xw) = 2 X.T (Yhat - Y)
# can drop 2, as it gets absorbed by learning rate

# let's try gradient descent
costs = [] # keep track of squared error cost
w = np.random.randn(D) / np.sqrt(D) # randomly initialize w
learning_rate = 0.001
for t in range(1000):
  # update w
  Yhat = X.dot(w)
  delta = Yhat - Y
  w = w - learning_rate*X.T.dot(delta)

  # find and store the cost
  mse = delta.dot(delta) / N
  costs.append(mse)

# plot the costs
plt.plot(costs)
plt.show()

print("final w:", w)

# plot prediction vs target
plt.plot(Yhat, label='prediction')
plt.plot(Y, label='target')
plt.legend()
plt.show()