
import numpy as np
import matplotlib.pyplot as plt
from control import tf, bode, pade

g = tf([5, 5], [5, 1, 0])
s = tf('s')
num, den = pade(2, 1)
delay = tf(num, den)
G = g * delay
plt.figure()
bode(G, dB=True, Hz=False, deg=True)
plt.show()