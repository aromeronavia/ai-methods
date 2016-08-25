import numpy as np
import matplotlib.pyplot as plt

def initPopulation():
  return np.random.randint(1024, size=8)

def evaluateWithFunction(population):
  return population ** 2

def mutate(string):
  nbit = np.random.randint(10);
  strList = list(string)
  bit = strList[nbit]
  if bit == '1':
    strList[nbit] = '0'
    return ''.join(strList)

  strList[nbit] = '1'
  return ''.join(strList)

population = initPopulation()

generations = 100
average = np.zeros(generations)
for i in range(generations):
# Init
  evaluatedPopulation = evaluateWithFunction(population)
  average[i] = np.mean(evaluatedPopulation)

# Selection
  temp = np.zeros((8, 2))
  temp[:, 0] = evaluatedPopulation
  temp[:, 1] = population
  temp = temp[temp[:,0].argsort(),:]
  xpad = temp[4:8, 1]

#Cruzamiento
  xhijbin = ['0' for j in range(4)]
  xhijbin[0] = np.binary_repr(np.int(xpad[0]), width=10)[4:10] + \
               np.binary_repr(np.int(xpad[1]), width=10)[0:4]
  xhijbin[1] = np.binary_repr(np.int(xpad[1]), width=10)[4:10] + \
               np.binary_repr(np.int(xpad[0]), width=10)[0:4]
  xhijbin[2] = np.binary_repr(np.int(xpad[3]), width=10)[4:10] + \
               np.binary_repr(np.int(xpad[2]), width=10)[0:4]
  xhijbin[3] = np.binary_repr(np.int(xpad[2]), width=10)[4:10] + \
               np.binary_repr(np.int(xpad[3]), width=10)[0:4]

  # mutacion
  if (i % 10) == 0:
    nhijo = np.random.randint(4);
    xhijbin[nhijo] = mutate(xhijbin[nhijo])

  xhij = [int(xhijbin[k], 2) for k in range(4)]

  population[0:4] = xpad
  population[4:8] = xhij

plt.plot(average)
plt.show()
