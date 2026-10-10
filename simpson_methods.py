import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)
a = 0
b = np.pi / 2
I_exact = 1.0
n = 6

def simpson_simple(a, b):
    m = (a+b) / 2
    return (b-a) / 6 * (f(a) + 4 * f(m)+f(b))

def simpson_composite(a,b,n):
    if n <= 0 or n%2 != 0:
        raise ValueError("n must be a positive even integer")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 1:
            s += 4 * f(a + i * h)
        else:
            s += 2 * f(a + i * h)
    return h/3 * s

S1 = simpson_simple(a, b)
Sn = simpson_composite(a, b, n)

print("simpson methods")
print("-" * 50)
print(f"exact integral: {I_exact:.6f}")
print(f"simple Simpson: {S1:.6f}")
print(f"simple error: {abs(I_exact - S1):.6f}")
print(f"composite Simpson: {Sn:.6f}")
print(f"composite error: {abs(I_exact - Sn):.6f}")

# Graphs
x = np.linspace(a,b,200)
xi = np.linspace(a,b,n + 1)

fig,ax= plt.subplots(1,2,figsize=(12,5))

#Simple simpson
m = (a + b) / 2
p = np.polyfit([a, m, b], [f(a), f(m), f(b)], 2)
ax[0].plot(x, f(x), label="sin(x)")
ax[0].plot(x, np.polyval(p, x), "r--",label="quadratic polynomial")
ax[0].fill_between(x, np.polyval(p, x), 0,color="green", alpha=0.2)
ax[0].set_title(f"simple Simpson: {S1:.6f}")
ax[0].legend()
ax[0].grid(True)

#composite simpson
ax[1].plot(x, f(x), label="sin(x)")
for k in range(0, n, 2):
    x0, x1, x2 = xi[k], xi[k + 1], xi[k + 2]
    p = np.polyfit([x0, x1, x2], [f(x0), f(x1), f(x2)], 2)
    xx = np.linspace(x0, x2, 50)
    yy = np.polyval(p, xx)

    ax[1].plot(xx, yy, "r--")
    ax[1].fill_between(xx, yy, 0,color="green", alpha=0.2)

ax[1].set_title(f"composite Simpson (n={n}): {Sn:.6f}")
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.savefig("comparaison_simpson.png", dpi=150)
plt.show()