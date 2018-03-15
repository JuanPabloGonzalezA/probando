import numpy as np


datos=np.loadtxt('monthrg.dat')

tiempo=datos[:,0]+(datos[:,1]-1)/12.0
manchas=datos[:,3]
posiciones=tiempo>=1900

tiempo=tiempo[posiciones]
manchas=manchas[posiciones]

datosfinales=np.array([tiempo,manchas])
datosfinales=np.transpose(datosfinales)

np.savetxt('fecha_manchas.dat',datosfinales)
