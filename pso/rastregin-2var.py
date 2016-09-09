import numpy as np
import matplotlib.pyplot as plt

def findBestGlobalIndex(performanceFn):
  return np.argmin(performanceFn)

def rast(x1, x2):
  particles = np.size(x1)
  restriction1 = np.zeros(particles)
  restriction2 = np.zeros(particles)
  restriction3 = np.zeros(particles)
  alpha1 = 1000
  alpha2 = 1000
  alpha3 = 1000
  # filter those who doesnt fit x <= 6
  index = (3 - x1) > 0
  restriction1[index] = (3 - x1[index]) * alpha1
  # filter those who doesnt fit x >= 2
  index = (2 - x2) > 0
  restriction2[index] = (2 - x2[index]) * alpha2
  # filter those who doesnt fit x1 + x2 <= 10
  index = (x1 + 2 * x2 - 10) < 0
  restriction3[index] = (x1[index] + 2 * x2[index] - 10) * alpha3

  return 10 + x1 ** 2 - 10 * np.cos(5 * x1) + \
         10 + x2 ** 2 - 10 * np.cos(5 * x2) + \
         restriction1 + restriction2

nParticles = 20
iterations = 10000
c1 = 0.01
c2 = 0.01

x = np.random.rand(nParticles)
x2 = np.random.rand(nParticles)

bestLocalParticles = x # Mejores locales iniciales x1pl
bestLocalParticlesPerformance = 10000000 * np.ones(nParticles) #Desempeno local inicial fpl
bestLocalParticles2 = x2 # Mejores locales iniciales x1pl
bestLocalParticlesPerformance2 = 10000000 * np.ones(nParticles) #Desempeno local inicial fpl

bestGlobal = 0 #x1pg
bestGlobal2 = 0 #x2pg
bestGlobalPerformance = 1000000 #fpg

speed = np.zeros(nParticles) # Velocidades iniciales vx1
speed2 = np.zeros(nParticles) # Velocidades iniciales vx1

for k in range(iterations):
  performanceFn = rast(x, x2) # Calcular los desempenos del enjambre
  # Encontrar al mejor global
  index = findBestGlobalIndex(performanceFn)
  if (performanceFn[index] < bestGlobalPerformance):
    bestGlobal = x[index]
    bestGlobal2 = x2[index]
    bestGlobalPerformance = performanceFn[index]

  for i in range(nParticles):
    if (performanceFn[i] < bestLocalParticlesPerformance[i]):
      bestLocalParticles[i] = x[i]
      bestLocalParticles2[i] = x2[i]
      bestLocalParticlesPerformance[i] = performanceFn[i]

  speed = speed + c1 * np.random.rand(nParticles) * (bestGlobal - x) \
                 + c2 * np.random.rand(nParticles) * (bestLocalParticles - x)
  speed2 = speed2 + c1 * np.random.rand(nParticles) * (bestGlobal2 - x2) \
                 + c2 * np.random.rand(nParticles) * (bestLocalParticles2 - x2)

  x = x + speed

# plt.plot(bestGlobal, bestGlobalPerformance, 'ro', x, performanceFn, 'b.', x2, y, 'b')
plt.plot([3, 3], [-10, 10], 'k--', [-10, 10], [2, 2], 'k--', [-10, 10], [10, 0], 'k--')
plt.plot(x, x2, 'b.', bestGlobal, bestGlobal2, 'go', 0, 0, 'ro')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([-10, 10, -10, 10])
plt.show()
