import numpy as np


# create simple xor network
def simple_network():
    X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    y = np.array([0, 1, 1, 0]).T.reshape(4, 1)
    learning_rate, hid_dim = 0.5, 4
    W0 = np.random.random((3, hid_dim)) - 1
    W1 = np.random.random((hid_dim, 1)) - 1
    # batch_gradient_descent(1700, X, y, W0, W1, learning_rate, hid_dim)
    stochastic_gradient_descent(1700, X, y, W0, W1, learning_rate, hid_dim)


def batch_gradient_descent(n_epochs, X, y, W0, W1, learning_rate, hid_dim):
    for epoch in range(n_epochs):
        # forward pass
        layer1 = 1 / (1 + np.exp(-(X @ W0)))  # 4x4
        layer2 = 1 / (1 + np.exp(-(layer1 @ W1)))  # 4x1
        # error measure
        layer2_delta = (layer2 - y) * (layer2 * (1 - layer2))  # 4x1
        layer1_delta = (layer2_delta @ W1.T) * (layer1 * (1 - layer1))  # 4x4
        # update weights a.k.a backpropagate
        W1 -= (learning_rate * (layer1.T @ layer2_delta))  # 4x1
        W0 -= (learning_rate * (X.T @ layer1_delta))  # 3x4
        print("prediction output: {}".format(layer2))


def stochastic_gradient_descent(n_epochs, X, y, W0, W1, learning_rate, hid_dim):
    layer1 = np.zeros_like(X @ W0)
    layer2 = np.zeros_like(layer1 @ W1)
    layer2_delta = np.zeros((4, 1))
    layer1_delta = np.zeros((4, 4))
    for epoch in range(n_epochs):
        # random shuffling of data
        indices = np.arange(X.shape[0])
        np.random.shuffle(indices)
        for indx in range(X.shape[0]):
            # forward pass
            layer1[indx] = 1 / (1 + np.exp(-(X[indices][indx, :] @ W0)))
            layer2[indx] = 1 / (1 + np.exp(-(layer1[indx] @ W1)))
            # # error measure a.k.a gradient
            layer2_delta = (layer2[indx] - y[indices]) * (layer2[indx] * (1 - layer2[indx]))
            layer1_delta[indx] = (layer2_delta[indx].reshape(1, 1) @ W1.T) * (layer1[indx] * (1 - layer1[indx]))
            # # update weights a.k.a backpropagate
            W1 -= (learning_rate * (layer1.T @ layer2_delta))
            W0 -= (learning_rate * (X.T @ layer1_delta))
        print("prediction output: {}".format(layer2))
        print("true labels {}".format(y[indices]))


def minibatch_gradient_descent(n_epochs):
    pass


def nesterov(n_epochs):
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
