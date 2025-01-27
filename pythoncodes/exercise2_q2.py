from control import tf, step_response, step_info
import matplotlib.pyplot as plt

G_open = tf([0.4], [1, 0.4])
T_closed = tf([0.4], [1, 0.8])

time_open, response_open = step_response(G_open)
time_closed, response_closed = step_response(T_closed)

plt.figure()
plt.plot(time_open, response_open, 'b', linewidth=1.5, label='Open-Loop')
plt.plot(time_closed, response_closed, 'r', linewidth=1.5, label='Closed-Loop')
plt.title('Step Response of Open-Loop and Closed-Loop Systems')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

info_open = step_info(G_open)
info_closed = step_info(T_closed)

steady_state_open = response_open[-1]
steady_state_closed = response_closed[-1]
steady_state_error_open = abs(1 - steady_state_open)
steady_state_error_closed = abs(0.5 - steady_state_closed)

time_constant_open = 1 / 0.4
time_constant_closed = 1 / 0.8

print('Open-Loop System Characteristics:')
print(f'  Rise Time: {info_open["RiseTime"]:.2f}')
print(f'  Settling Time: {info_open["SettlingTime"]:.2f}')
print(f'  Overshoot: {info_open["Overshoot"]:.1f}%')
print(f'  Steady-State Value: {steady_state_open:.2f}')
print(f'  Steady-State Error: {steady_state_error_open:.2f}')
print(f'  Time Constant: {time_constant_open:.2f} sec')

print('Closed-Loop System Characteristics:')
print(f'  Rise Time: {info_closed["RiseTime"]:.2f}')
print(f'  Settling Time: {info_closed["SettlingTime"]:.2f}')
print(f'  Overshoot: {info_closed["Overshoot"]:.1f}%')
print(f'  Steady-State Value: {steady_state_closed:.2f}')
print(f'  Steady-State Error: {steady_state_error_closed:.2f}')
print(f'  Time Constant: {time_constant_closed:.2f} sec')

plt.text(6, 0.85, f'Open-Loop:\nRise Time: {info_open["RiseTime"]:.2f} sec\nSettling Time: {info_open["SettlingTime"]:.2f} sec\nOvershoot: {info_open["Overshoot"]:.1f}%\nSteady-State Error: {steady_state_error_open:.2f}\nTime Constant: {time_constant_open:.2f} sec',
         verticalalignment='top', horizontalalignment='left', color='blue', fontsize=10)

plt.text(6, 0.2, f'Closed-Loop:\nRise Time: {info_closed["RiseTime"]:.2f} sec\nSettling Time: {info_closed["SettlingTime"]:.2f} sec\nOvershoot: {info_closed["Overshoot"]:.1f}%\nSteady-State Error: {steady_state_error_closed:.2f}\nTime Constant: {time_constant_closed:.2f} sec',
         verticalalignment='bottom', horizontalalignment='left', color='red', fontsize=10)

plt.show()
