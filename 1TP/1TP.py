## Primeiro Trabalho Parcial: Parametrização de um FT.
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import step

def plot_step_response(final_settling_time):
    final_settling_time_ms= final_settling_time*1000

    tau = final_settling_time / 3
    K = 1

    numerator = [K]
    denominator = [tau, 1]

    sys = (numerator, denominator)

    t = np.linspace(0, 4 * final_settling_time, 1000)

    t, y = step(sys, T=t)

    plt.plot(t*1000, y, linewidth=2, label=f'{round(final_settling_time_ms,1)} ms')
    plt.legend()
    plt.grid(True)
    plt.xlabel('Time (ms)')
    plt.ylabel('Step Response')
    plt.title('Step Response of a First-Order Transfer Function')

for i in range(1, 6):
    plot_step_response(i * 1e-3)
    plt.savefig("1TP/output.png")

