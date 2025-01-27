import sympy as sp
from control import tf, series, feedback, minreal, poles

s = tf([1, 0], [1])

G1 = 1 / s
G2 = 2 * s + 1
G3 = 1 / (s**2 + 1)
G4 = s / (s + 1)

H1 = 3 / s
H2 = (s - 1) / (s + 3)
H3 = s / (s**2 + 3 * s + 1)
H4 = 1 / (s + 2)

y2 = s

input_to_G1 = y2
input_to_G2 = G1
input_to_G3 = G4 + G2 - H2
input_to_G4 = y2

input_to_H1 = G1
input_to_H2 = G3 - H4
input_to_H3 = G3 - H4
input_to_H4 = G3 - H4

y5 = G3 - H4

plant_ic = minreal(tf([y5.num[0]], [y5.den[0]]))

poles = poles(plant_ic)

print("Simplified Transfer Function:", plant_ic)
print("Poles of the system:", poles)
