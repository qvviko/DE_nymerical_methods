import matplotlib.pyplot as plt


def my_func(x, y):
    return x * y * y - 3 * x * y


def euler(func, x0, y0, X, N_steps):
    x = [float(x0)]
    y = [float(y0)]
    h = (X - x0) / N_steps
    for i in range(N_steps):
        x.append(x[i] + h)
        y.append(y[i] + h * func(x[i], y[i]))
    return x, y


def improved_euler(func, x0, y0, X, N_steps):
    x = [x0]
    y = [y0]
    h = (X - x0) / N_steps
    for i in range(N_steps):
        x.append(x[i] + h)
        m1 = func(x[i], y[i])
        m2 = func(x[i + 1], y[i] + h * m1)
        y.append(y[i] + h * (m1 + m2) / 2)
    return x, y


def runge_kutta(func, x0, y0, X, N_steps):
    x = [x0]
    y = [y0]
    h = (X - x0) / N_steps
    for i in range(N_steps):
        x.append(x[i] + h)
        k1 = h * func(x[i], y[i])
        k2 = h * func(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * func(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * func(x[i] + h, y[i] + k3)
        y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    pass


if __name__ == "__main__":
    x0 = 0
    y0 = 2
    X = 6.4
    N_steps = 20
    (x, y) = euler(my_func, x0, y0, X, N_steps)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    fig.show()
    (x, y) = improved_euler(my_func, x0, y0, X, N_steps)
    fig2, ax2 = plt.subplots()
    ax2.plot(x, y)
    fig2.show()
    (x, y) = improved_euler(my_func, x0, y0, X, N_steps)
    fig3, ax3 = plt.subplots()
    ax3.plot(x, y)
    fig3.show()
