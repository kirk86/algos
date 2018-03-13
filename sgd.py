import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2017)

# reproducibility
hid_dim = 4
W0 = np.random.random((3, hid_dim)) - 1
W1 = np.random.random((hid_dim, 1)) - 1


# create simple xor network
def xor_network():
    X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    y = np.array([0, 1, 1, 0]).T.reshape(4, 1)
    learning_rate = 0.5
    # stochastic_gradient_descent(1700, X, y, W0, W1, learning_rate)
    # print("=======================================================")
    batch_gradient_descent(1700, X, y, W0, W1, learning_rate)


def batch_gradient_descent(n_epochs, X, y, W0, W1, learning_rate):
    fig = plt.figure()
    for epoch in range(n_epochs):
        # forward pass
        layer1 = 1 / (1 + np.exp(-(X @ W0)))  # 4x4
        layer2 = 1 / (1 + np.exp(-(layer1 @ W1)))  # 4x1
        # error measure
        layer2_error = (layer2 - y) * (layer2 * (1 - layer2))  # 4x1
        layer1_error = (layer2_error @ W1.T) * (layer1 * (1 - layer1))  # 4x4
        # update weights a.k.a backpropagate
        W1 -= (learning_rate * (layer1.T @ layer2_error))  # 4x1
        W0 -= (learning_rate * (X.T @ layer1_error))  # 3x4
        print("prediction output: {}".format(layer2))
        print("true labels {}".format(y))
        plt.plot(np.repeat(epoch, len(W1.ravel())), W1.ravel(), 'bo')
        plt.plot(np.repeat(epoch, len(W0.ravel())), W0.ravel(), 'r+')
    plt.show()


def stochastic_gradient_descent(n_epochs, X, y, W0, W1, learning_rate):
    layer1 = np.zeros((4, 4))
    layer2 = np.zeros((4, 1))
    layer2_error = np.zeros((4, 1))
    layer1_error = np.zeros((4, 4))
    indices = np.arange(X.shape[0])
    # fig = plt.figure()
    for epoch in range(n_epochs):
        # random shuffling of data
        np.random.shuffle(indices)
        X = X[indices]
        y = y[indices]
        for row in indices:
            # forward pass
            layer1[row] = 1 / (1 + np.exp(-(X[row, :] @ W0)))
            layer2[row] = 1 / (1 + np.exp(-(layer1[row] @ W1)))
            # # error measure a.k.a gradient
            layer2_error = (layer2[row] - y) * (layer2[row] * (1 - layer2[row]))
            layer1_error[row] = (layer2_error[row].reshape(1, 1) @ W1.T) * (layer1[row] * (1 - layer1[row]))
            # # update weights a.k.a backpropagate
            W1 -= (learning_rate * (layer1.T @ layer2_error))
            W0 -= (learning_rate * (X.T @ layer1_error))
        print("prediction output: {}".format(layer2))
        print("true labels {}".format(y))
        # plt.plot(np.repeat(epoch, len(W1.ravel())), W1.ravel(), 'bo')
        # plt.plot(np.repeat(epoch, len(W0.ravel())), W0.ravel(), 'r+')
    # plt.show()


# Make a prediction with coefficients
def predict(row, coefficients):
    yhat = coefficients[0]
    for i in range(len(row)-1):
        yhat += coefficients[i + 1] * row[i]
    return yhat


# Estimate linear regression coefficients using stochastic gradient descent
def coefficients_sgd(train, l_rate, n_epoch):
    coef = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            yhat = predict(row, coef)
            error = yhat - row[-1]
            sum_error += error**2
            coef[0] = coef[0] - l_rate * error
            for i in range(len(row)-1):
                coef[i + 1] = coef[i + 1] - l_rate * error * row[i]
                print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return coef


# Calculate coefficients
#dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
#l_rate = 0.001
#n_epoch = 50
#coef = coefficients_sgd(dataset, l_rate, n_epoch)
#print(coef)
# Make a prediction with coefficients


def minibatch_gradient_descent(n_epochs, X, y, W0, W1, learning_rate):
    for epoch in range(n_epochs):
        for batch in [2, 4]:
            # forward pass
            layer1 = 1 / (1 + np.exp(-(X[:batch] @ W0[:batch])))  # 4x4
            layer2 = 1 / (1 + np.exp(-(layer1 @ W1[:batch])))  # 4x1
            # error measure
            layer2_error = (layer2 - y[:batch]) * (layer2 * (1 - layer2))  # 4x1
            layer1_error = (layer2_error @ W1[:batch].T) * (layer1 * (1 - layer1))  # 4x4
            # update weights a.k.a backpropagate
            W1 -= (learning_rate * (layer1.T @ layer2_error))  # 4x1
            W0 -= (learning_rate * (X[:batch].T @ layer1_error))  # 3x4
            print("prediction output: {}".format(layer2))
            print("true labels {}".format(y))
            plt.plot(np.repeat(epoch, len(W1.ravel())), W1.ravel(), 'bo')
            plt.plot(np.repeat(epoch, len(W0.ravel())), W0.ravel(), 'r+')


def nesterov(n_epochs, X, y, W0, W1, learning_rate):
    pass


def adagrad(n_epochs):
    pass


def adadelta(n_epochs):
    pass


def rmsprop(n_epochs):
    pass


def adam(n_epochs):
    pass


def adamax(n_epochs):
    pass


def nadam(n_epochs):
    pass


xor_network()
