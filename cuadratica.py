from utils import initpob, mutacion, selecbest, cruzamiento
import numpy as np
import matplotlib.pyplot as plt

npob = 20
nbits = 10
xmin = 0
xmax = 1023

npadres = 10
nhijos = npob - npadres

iterations = 100

yprom = np.zeros(iterations)

initialParents, initialParentsInt = initpob(npob, nbits, xmin, xmax)
initialParents2, initialParentsInt2 = initpob(npob, nbits, xmin, xmax)

for i in range(iterations):
  yp = initialParents ** 2 + initialParents2
  yprom[i] = np.mean(yp)

  bestParents, bestParentsInt = selecbest(npadres, initialParents, initialParentsInt, yp, 1)
  bestParents2, bestParentsInt2 = selecbest(npadres, initialParents2, initialParentsInt2, yp, 1)

  childs, childsInt = cruzamiento(bestParentsInt, nhijos, nbits, xmin, xmax)
  childs2, childsInt2 = cruzamiento(bestParentsInt2, nhijos, nbits, xmin, xmax)

  if i % 10 == 0:
    childs, childsInt = mutacion(childsInt, 1, nbits, xmin, xmax)
    childs2, childsInt2 = mutacion(childsInt2, 1, nbits, xmin, xmax)

  initialParents[0: npadres, 0] = bestParents[:, 0]
  initialParents[npadres: npob, 0] = childs[:, 0]
  initialParentsInt[0: npadres, 0] = bestParentsInt[:, 0]
  initialParentsInt[npadres: npob, 0] = childsInt[:, 0]

  initialParents2[0: npadres, 0] = bestParents2[:, 0]
  initialParents2[npadres: npob, 0] = childs2[:, 0]
  initialParentsInt2[0: npadres, 0] = bestParentsInt2[:, 0]
  initialParentsInt2[npadres: npob, 0] = childsInt2[:, 0]

plt.plot(yprom)
plt.show()
