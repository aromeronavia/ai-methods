import numpy as np
import matplotlib.pyplot as plt

def findBestGlobalIndex(performanceFn):
  return np.argmin(performanceFn)

def rast(x):
  particles = np.size(x)
  restriction1 = np.zeros(particles)
  restriction2 = np.zeros(particles)
  alpha1 = 100
  alpha2 = 100
  # filter where x <= 6
  index = (x - 6) > 0
  restriction1[index] = (x[index] - 6) * alpha1
  # filter where x >= 2
  index = (2 - x) > 0
  restriction2[index] = (2 - x[index]) * alpha2

  return 10 + x ** 2 - 10 * np.cos(5 * x) + restriction1 + restriction2

nParticles = 10
iterations = 10000
c1 = 0.01
c2 = 0.01

x = np.random.rand(nParticles)

bestLocalParticles = x # Mejores locales iniciales x1pl
bestLocalParticlesPerformance = 10000000 * np.ones(nParticles) #Desempeno local inicial fpl

bestGlobal = 0 #x1pg
bestGlobalPerformance = 1000000 #fpg

speed = np.zeros(nParticles) # Velocidades iniciales vx1

for k in range(iterations):
  performanceFn = rast(x) # Calcular los desempenos del enjambre
  # Encontrar al mejor global
  index = findBestGlobalIndex(performanceFn)
  if (performanceFn[index] < bestGlobalPerformance):
    bestGlobal = x[index]
    bestGlobalPerformance = performanceFn[index]

  for i in range(nParticles):
    if (performanceFn[i] < bestLocalParticlesPerformance[i]):
      bestLocalParticles[i] = x[i]
      bestLocalParticlesPerformance[i] = performanceFn[i]

  speed = speed + c1 * np.random.rand(nParticles) * (bestGlobal - x) \
                 + c2 * np.random.rand(nParticles) * (bestLocalParticles - x)

  x = x + speed

performanceFn = rast(x)
x2 = np.arange(-10, 10, 0.01)
y = rast(x2)

plt.plot(bestGlobal, bestGlobalPerformance, 'ro', x, performanceFn, 'b.', x2, y, 'b')
plt.show()
