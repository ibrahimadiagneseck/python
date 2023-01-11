import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# x = np.linspace(-5, 5, 200)
# y = np.sin(x)
# ax.plot(x, y)
# plt.show()

x = np.linspace(-5, 5, 200)
y = np.sin(x)
ax.plot(x, y, label="courbe") # pour legende
ax.legend() # pour legende
ax.set_xlabel('axe des abscisses')
ax.set_ylabel('axe des ordonnees')
ax.set_title('figures')
plt.show()
 