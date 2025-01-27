from control import tf, pade, bode_plot
import matplotlib.pyplot as plt

s = tf('s')
g = tf([5, 5], [5, 1, 0])


delay_time = 2
num, den = pade(delay_time, 1)
G_exp = tf(num, den)

final_g = g * G_exp

plt.figure()
bode_plot(g)
plt.grid(True)
plt.title('Bode Plot without exp')

plt.figure()
bode_plot(final_g)
plt.grid(True)
plt.title('Bode Plot with exp (Pade Approximation)')

plt.show()
