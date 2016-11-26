"""This script can be executed as Jupyter only"""

# It requires some other output mechanism than stdout

#%%
import matplotlib.pyplot as plt
import numpy as np

XVAR = np.linspace(0, 20, 100)
plt.plot(XVAR, np.sin(XVAR))
plt.show()
