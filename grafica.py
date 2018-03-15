import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt('fecha_manchas.dat')
plt.plot(datos[:,0],datos[:,1])
plt.savefig('fecha_manchas.pdf')
