import numpy as np
import matplotlib.pyplot as plt

def time_simulate(m , b, k, omega_drive, F=1.0, x0=1.0, v0=0.0, dt=0.01, step=1000):

    omega_naught = np.sqrt(k / m)
    gamma = b / (2 * m)
    A = (F / m)

    x = np.zeros(step)
    t = np.arange(step) * dt
    x_vals, v = x0, v0

    for i in range(step):
        x[i] = x_vals
        a = A * np.sin(omega_drive * t[i]) - (omega_naught)**2 * x_vals - (b / m) * v
        v += a * dt
        x_vals += v * dt

    return t, x

def resonance_curve(m, b, k, F=1.0, f_step=1000, span=5.0):

    omega_naught = np.sqrt(k / m)
    gamma = b / (2 * m)
    A = (F / m)

    omega = np.linspace(0, span * omega_naught, f_step)
    amplitude = A / np.sqrt((omega_naught**2 - omega**2)**2 + (2 * gamma * omega)**2)

    return omega, amplitude

def main():

    dt, step, f_step = 0.01, 1000, 1000

    m = float(input("Enter the value for m: "))
    b = float(input("Enter the value for b: "))
    k = float(input("Enter the value for k: "))
    omega_drive = float(input("Enter the driving frequency: "))
    omega_naught = np.sqrt(k / m)

    t, x = time_simulate(m, b, k, omega_drive)
    omega, x_res = resonance_curve(m, b, k) 

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11,4))

    ax1.plot(t, x)
    ax1.set_title("Time-domain response")
    ax1.set_xlabel("time / s")
    ax1.set_ylabel("position / m")

    ax2.plot(omega, x_res)
    ax2.axvline(omega_naught, color="r", linestyle="--", label=r"$\omega_0$")
    ax2.axvline(omega_drive, color="g", linestyle=":", label=r"$\omega_{drive}$")
    ax2.set_title("Resonance curve")
    ax2.set_xlabel("driving frequency / rad/s")
    ax2.set_ylabel("steady-state amplitude / m")
    ax2.legend()

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()