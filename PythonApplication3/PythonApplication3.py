import random as random_number
import matplotlib.pyplot as plt
from numpy import array


def MCint3(f, a, b, n, N=100):
    '''Cохраняет каждое N приближение интеграла
    в массив I и записываем соответствующее значение k'''
    s = 0

    I_values = []
    k_values = []
    for k in range(1, n+1):
        x = random_number.uniform(a, b)
        s += f(x)
        if k % N == 0:
            I = (float(b-a)/k)*s
            I_values.append(I)
            k_values.append(k)
    return k_values, I_values

def f1(x):
    return 2 + 3*x

k, I = MCint3(f1, 1, 2, 1000000, N=10000)
error = 6.5 - array(I)

plt.title('Monte Carlo integration')
plt.xlabel('n')
plt.ylabel('error')
plt.plot(k, error)
plt.show()