import matplotlib.pyplot as plt
import numpy as np # type: ignore

left = [1, 2, 3, 4, 5, 6]

tick_label = ['DES', 'AES', 'RSA', 'ARC2', 'Salsa20', 'Blowfish']

time_pi = [267.486500000814, 260.82780000392813, 264.8867000004975, 267.5608999998076, 264.22200000524754, 271.11519999743905]

time_10_pi = [2099.810099993192, 2096.236299999873, 2116.4763000051607, 2100.205899994762, 2080.4553999987547, 2114.921900005138]

plt.bar(left, time_10_pi, tick_label = tick_label, width = 0.5)

plt.xlabel('Algorithms')
plt.ylabel('Total Time Taken in ms')
plt.title('Total Time Taken by different Algorithms')
plt.ylim(0, 3000)
plt.show()