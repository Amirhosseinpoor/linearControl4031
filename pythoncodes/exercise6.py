
import numpy as np
import matplotlib.pyplot as plt
from control import tf, minreal, margin, step_response

G = tf([3750], [1, 25, 0])
C = tf([0.021, 1], [0.007, 1])
G1 = minreal(C * G)
plt.figure(1)
margin(G1)
plt.figure(2)
t1, y1 = step_response(minreal(G1 / (1 + G1)))
t2, y2 = step_response(tf([1], [1]))
plt.plot(t1, y1, label='Step response of system')
plt.plot(t2, y2, label='Step')
plt.legend()
plt.figure(3)
t3, y3 = step_response(minreal(tf([1], [1, 0]) * G1 / (1 + G1)))
t4, y4 = step_response(tf([1], [1, 0]))
plt.plot(t3, y3, label='Ramp response of system')
plt.plot(t4, y4, label='Ramp')
plt.title('Ramp Response')
plt.legend()
plt.show()
