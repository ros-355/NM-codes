import numpy as np
import matplotlib.pyplot as plt

# USER FUNCTION (Replace here)
def f(x):
    return x**3 - x - 2    # example


# BISECTION METHOD
def bisection(a, b, tol=1e-6, max_iter=20):

    print("\n--- BISECTION METHOD ITERATIONS ---")
    if f(a) * f(b) > 0:
        print("No root in interval! f(a) & f(b) have same signs.")
        return None

    table = []
    for i in range(1, max_iter+1):
        c = (a + b) / 2
        table.append([i, a, b, c, f(c)])
        print(f"Iter={i:2d}  a={a:.6f}  b={b:.6f}  c={c:.6f}  f(c)={f(c):.6f}")

        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    

    # Graph
    X = np.linspace(a, b, 400)
    plt.figure()
    plt.plot(X, f(X), label="f(x)")
    plt.axhline(0)
    plt.scatter([c], [f(c)], color='red', label=f"Root approx = {c:.4f}")
    plt.title("Bisection Method Result")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

    return c
# NEWTON RAPHSON
def newton_raphson(x0, tol=1e-6, max_iter=20):

    print("\n--- NEWTON–RAPHSON METHOD ITERATIONS ---")

    # Numerical derivative
    def df(x):
        h = 1e-5
        return (f(x+h) - f(x-h)) / (2*h)

    x = x0
    for i in range(1, max_iter+1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Derivative became zero.")
            return None

        x_new = x - fx/dfx
        print(f"Iter={i:2d}  x={x:.6f}  f(x)={fx:.6f}")

        if abs(x_new - x) < tol:
            x = x_new
            break
        x = x_new

    # Graph
    X = np.linspace(x-2, x+2, 400)
    plt.figure()
    plt.plot(X, f(X), label="f(x)")
    plt.axhline(0)
    plt.scatter([x], [f(x)], color='red', label=f"Root approx = {x:.4f}")
    plt.title("Newton–Raphson Method Result")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

    return x

# FALSE POSITION (REGULA FALSI)
def false_position(a, b, tol=1e-6, max_iter=20):

    print("\n--- FALSE POSITION METHOD ITERATIONS ---")
    if f(a) * f(b) > 0:
        print("No root in interval! f(a) & f(b) have same signs.")
        return None

    c = a
    for i in range(1, max_iter+1):
        c = b - f(b)*(b - a)/(f(b) - f(a))
        print(f"Iter={i:2d}  a={a:.6f}  b={b:.6f}  c={c:.6f}  f(c)={f(c):.6f}")

        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    # Graph
    X = np.linspace(a, b, 400)
    plt.figure()
    plt.plot(X, f(X), label="f(x)")
    plt.axhline(0)
    plt.scatter([c], [f(c)], color='red', label=f"Root approx = {c:.4f}")
    plt.title("False Position Method Result")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

    return c


# ======================================================
# RUN
# ======================================================
root_bis  = bisection(1, 2)
root_nr   = newton_raphson(1.5)
root_fp   = false_position(1, 2)
print("\nApprox roots:")
print("Bisection      =", root_bis)
print("Newton-Raphson =", root_nr)
print("False-Position =", root_fp)
