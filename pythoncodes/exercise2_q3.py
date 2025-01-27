from control import tf, step_response, step_info
import matplotlib.pyplot as plt

K = 8.41
T = tf([K], [1, 4, K])

time, response = step_response(T)

plt.figure()
plt.plot(time, response)
plt.title('Step Response of the System for K = 8.41')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

info = step_info(T)
print(info)