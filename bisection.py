import numpy as np
import matplotlib.pyplot as plt

# CHANGE YOUR FUNCTION HERE
def f(x):
    return x**3 - x - 2

def bisection(a, b, tol=1e-6, max_iter=50):
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            break
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    print("Root (Bisection):", c)   # Print root before graph

    # graph value 
    X = np.linspace(a - 2, b + 2, 400)
    Y = f(X)

    plt.figure()
    plt.plot(X, Y, label="f(x)")
    plt.axhline(0, color='black')
    plt.scatter(c, f(c), color='red', label="Root")

    plt.title("Bisection Method — Root of f(x)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis (f(x))")
    plt.grid(True)
    plt.legend()
    plt.show()

    return c

bisection(1, 2)
