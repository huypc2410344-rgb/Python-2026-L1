import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 500)

y = 2 * x + (np.sin(x))**2 + 3

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$y = 2x + \sin^2(x) + 3$', color='blue')

plt.grid(True)
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.savefig("po.pdf", format="pdf", bbox_inches='tight')

plt.show()