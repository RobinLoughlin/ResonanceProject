import numpy as np
import matplotlib.pyplot as plt

dt, step = 0.01, 1000

x_vals, v = 1.0, 0.0

m = float(input("Enter the value for m: "))
b = float(input("Enter the value for b: "))
k = float(input("Enter the value for k: "))


x = np.zeros(step)
t = np.arange(step) * dt

for i in range(step):
    x[i] = x_vals
    a = - (k / m) * x_vals - (b / m) * v
    v += a * dt
    x_vals += v * dt

plt.plot(t, x)
plt.title("Simulation of SHM")
plt.xlabel("time /s")
plt.ylabel("position / m")
plt.show()
