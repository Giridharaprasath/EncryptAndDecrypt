import matplotlib.pyplot as plt
import numpy as np # type: ignore

left = [1, 2, 3, 4, 5, 6]

tick_label = ['DES', 'AES', 'RSA', 'ARC2', 'Salsa20', 'Blowfish']


#time_total = [3.625699999247445, 2.3844999996072147, 7.320599999948172, 2.8481999979703687, 1.8619000038597733, 3.025300000444986]

#time_large = [1730.467100000169, 1443.883900000401, 0, 2292.9700999957277, 1637.4455000041053, 1612.4955999985104]

time_pi = [267.486500000814, 260.82780000392813, 264.8867000004975, 267.5608999998076, 264.22200000524754, 271.11519999743905]

plt.bar(left, time_pi, tick_label = tick_label, width = 0.5)

plt.xlabel('Algorithms')
plt.ylabel('Total Time Taken in ms')
plt.title('Total Time Taken by different Algorithms')
plt.show()

"""
x_axis = np.arange(len(tick_label))

time_encrypt = [0.06089999988034833, 0.053899999329587445, 1.0600999982387293, 0.07839999852876645, 0.06520000169984996, 0.11830000039481092]
time_decrypt = [0.06459999895014334, 0.0593999993725447, 1.056799998274073, 0.05400000009103678, 0.013200002285884693, 0.038300000596791506]

plt.bar(x_axis - 0.2, time_encrypt, tick_label = tick_label, width = 0.4, label = 'Encrypt')
plt.bar(x_axis + 0.2, time_decrypt, tick_label = tick_label, width = 0.4, label = 'Decrypt')
plt.xlabel('Algorithms')
plt.ylabel('Time Taken in ms')
plt.title('Time Taken by different Algorithms')
plt.legend()
plt.show()
"""