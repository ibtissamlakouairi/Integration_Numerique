import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

a = 0
b = np.pi / 2
I_exact = 1.0
n = 6

def trapeze_simple(a, b):
    return (b - a) / 2 * (f(a) + f(b))

def trapeze_composite(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    return h / 2 * s

T1 = trapeze_simple(a, b)
Tn = trapeze_composite(a, b, n)

print("trapezoidal methods")
print("-" * 50)
print(f"exact: {I_exact:.6f}")
print(f"simple trapezoid: {T1:.6f}")
print(f"simple error: {abs(I_exact - T1):.6f}")
print(f"composite trapezoid: {Tn:.6f}")
print(f"composite error: {abs(I_exact - Tn):.6f}")

#graphs
x = np.linspace(a,b,200)
xi = np.linspace(a,b,n+1)
fig, ax = plt.subplots(1,2,figsize=(12,5))

#simple trapezoid
ax[0].plot(x,f(x),label="sin(x)")
ax[0].plot([a,b],[f(a),f(b)],"r--",
           label="Trapezoid")
ax[0].fill([a,a,b,b],[0,f(a),f(b),0],color="red", alpha=0.2)
ax[0].set_title(f"simple trapezoid: {T1:.6f}")
ax[0].legend()
ax[0].grid(True)

#composite trapezoid
ax[1].plot(x, f(x), label="sin(x)")
for i in range(n):
    x0, x1 = xi[i], xi[i + 1]
    y0, y1 = f(x0), f(x1)
    ax[1].fill([x0, x0, x1, x1], [0, y0, y1, 0], color="orange", alpha=0.25)
    ax[1].plot([x0, x1], [y0, y1], "r-o")

ax[1].set_title(f"Composite trapezoid (n={n}): {Tn:.6f}")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.savefig("comparaison_trapeze.png", dpi=150)
plt.show()