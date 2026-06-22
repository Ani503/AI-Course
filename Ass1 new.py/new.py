import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x_sin= np.arange(0,np.pi*2,0.1)
y_sin= np.sin(x_sin)
plt.figure(figsize=(10,5))
plt.plot(x_sin,y_sin)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid()
plt.show()  