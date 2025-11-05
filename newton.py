import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# CHANGE YOUR FUNCTION HERE
def f(x):
    return x**3 - x - 2

# CHANGE derivative here
def df(x):
    return 3*x**2 - 1
# ----------------------

def newton(x0, tol=1e-6, max_iter=50):
    for _ in range(max_iter):
        x1 = x0 - f(x0)/df(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1

    print("Root (Newton–Raphson):", x1)

    # ---- Graph ----
    X = np.linspace(x1 - 2, x1 + 2, 400)
    Y = f(X)

    plt.figure()
    plt.plot(X, Y, label="f(x)")
    plt.axhline(0, color='black')
    plt.scatter(x1, f(x1), color='red', label="Root")

    plt.title("Newton–Raphson Method — Root of f(x)")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis (f(x))")
    plt.grid(True)
    plt.legend()
    plt.show()

    return x1

newton(1.5)
