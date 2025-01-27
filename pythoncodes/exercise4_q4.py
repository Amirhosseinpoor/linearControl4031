from control import tf, zeros, poles, dcgain, nyquist
import matplotlib.pyplot as plt
import numpy as np

# Define numerator and denominator
numerator = np.convolve([1, 1], np.convolve([1, 2], np.convolve([1, 3], [1, 4])))
denominator = np.convolve([1, 0, 0, 0], [1, 100])

# Create transfer function
h = tf(-1 * numerator, denominator)

# Get zeros, poles, and gain
zeros = zeros(h)
poles = poles(h)
gain = dcgain(h)

print("Zeros:", zeros)
print("Poles:", poles)
print("Gain:", gain)

# Plot Nyquist diagram
plt.figure()
nyquist(h)
plt.title('Nyquist Plot')
plt.grid(True)
plt.show()
