"""
Resonance Simultation:

Inputs:
-mass of system m (kg)
-spring constant k (N/m)
-damping coefficient b (kg/s)
-driving frequency F (rad/s)       

Author: Robin Loughlin
Course: Theoretical Physics
Date: 28-09-2026
"""


import numpy as np
import matplotlib.pyplot as plt

def validate(m, b, k):
    """
    Tests validity of parameters for oscillation- raises an error if not valid
    """

    if m <= 0:
        raise ValueError(
        "The oscillator must have a mass greater than 0 to have a natural frequency"
        )               
    
    if b < 0:
        raise ValueError(
            "b must me a non negative number, as negative damping adds energy to the system"
        )

    if k <= 0:
        raise ValueError(
            "k must me a positive number to provide a restoring force"
        )


def time_simulate(m , b, k, omega_drive, F=1.0, x0=1.0, v0=0.0, dt=0.01, step=1000):
    """
    Simulates a damped oscillator, returns its position at each instant in time
    """

    validate(m, b, k)

    omega_naught = np.sqrt(k / m)
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
    """
    Creates a curve of amplitude against driving frequency for the forced oscillator to show resonance
    """

    validate(m, b, k)

    omega_naught = np.sqrt(k / m)
    gamma = b / (2 * m)
    A = (F / m)

    omega = np.linspace(0, span * omega_naught, f_step)
    amplitude = A / np.sqrt((omega_naught**2 - omega**2)**2 + (2 * gamma * omega)**2)

    return omega, amplitude

def main():
    """
    Inputs, plots
    """

    try:
        """
        Attempts value inputs, breaks if values do not produce an oscillator
        """
        
        m = float(input("Enter the value for m: "))
        b = float(input("Enter the value for b: "))
        k = float(input("Enter the value for k: "))
        omega_drive = float(input("Enter the driving frequency: "))

        t, x = time_simulate(m, b, k, omega_drive)
        omega, x_res = resonance_curve(m, b, k)
        validate(m, b, k)

    except ValueError as error:
        print(f"Error: {error}")
        return

    omega_naught = np.sqrt(k / m) 

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11,4))

    ax1.plot(t, x)                                         # Oscillator plot
    ax1.set_title("Time-domain response")
    ax1.set_xlabel("time / s")
    ax1.set_ylabel("position / m")

    ax2.plot(omega, x_res)                                                          # Resonance plot
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