import numpy as np
import matplotlib.pyplot as plt

def initialize(num_harmonics):
    amplitudes = np.zeros(num_harmonics)
    phases = np.zeros(num_harmonics)
    return amplitudes, phases

def update_display(amplitudes, phases, current_harmonic):
    maxT = 2
    intervalT = 1/200
    t = np.arange(0, maxT, intervalT)

    # Plot combined signal
    x = np.zeros(len(t))
    for n in range(1, len(amplitudes) + 1):
        x += amplitudes[n-1] * np.sin(2 * np.pi * n * t + phases[n-1])

    plt.figure(figsize=(15, 10))

    # Combined Signal
    plt.subplot(3, 1, 1)
    plt.plot(t, x)
    plt.title('Combined Signal')
    plt.grid()

    # Current Harmonic
    y = amplitudes[current_harmonic - 1] * np.sin(2 * np.pi * current_harmonic * t + phases[current_harmonic - 1])
    plt.subplot(3, 1, 2)
    plt.plot(t, y)
    plt.title(f'Harmonic {current_harmonic}')
    plt.grid()

    # Spectral Profile
    ax = plt.figure().add_subplot(313, projection='3d')
    # Stem plot without 'use_line_collection'
    for i in range(1, len(amplitudes) + 1):
        ax.plot([i, i], [0, phases[i-1]], [0, amplitudes[i-1]], marker='o', color='r')

    ax.set_title('Spectral Profile')
    ax.set_xlabel('Harmonic')
    ax.set_ylabel('Phase')
    ax.set_zlabel('Amplitude')

    plt.tight_layout()
    plt.show()

def update_amplitude(amplitudes, harmonic, amplitude):
    if 1 <= harmonic <= len(amplitudes):
        amplitudes[harmonic - 1] = amplitude

def update_phase(phases, harmonic, phase):
    if 1 <= harmonic <= len(phases):
        phases[harmonic - 1] = phase

def main():
    num_harmonics = 3
    amplitudes, phases = initialize(num_harmonics)

    update_amplitude(amplitudes, 1, 1.0)
    update_phase(phases, 1, np.pi / 4)
    update_amplitude(amplitudes, 2, 0.5)
    update_phase(phases, 2, np.pi / 2)
    update_amplitude(amplitudes, 3, 0.3)
    update_phase(phases, 3, np.pi)

    current_harmonic = 3  # Set the current harmonic
    update_display(amplitudes, phases, current_harmonic)

# Run the main function
if __name__ == "__main__":
    main()
