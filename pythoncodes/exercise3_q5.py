from control import tf, step_response, step_info, poles, zeros, dcgain
import matplotlib.pyplot as plt

G = tf([5, 10], [1, 4, 5])
T = tf([5, 10], [1, 9, 15])

print('System:')
poles = poles(G)
zeros = zeros(G)
print("Poles:", poles)
print("Zeros:", zeros)

response, time = step_response(T)

plt.figure()
plt.plot(time, response, '-', linewidth=0.5)
plt.grid(True)
plt.title('Step Response')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')
plt.show()

info = step_info(T)
print('Step Response Characteristics:')
print(info)

k = dcgain(G)
error_steady_state = 1 / (1 + k)
print(f'Steady-State Error: {error_steady_state}')
