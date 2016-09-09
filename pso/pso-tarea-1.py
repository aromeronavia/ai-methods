# Alberto Ignacio Romero Navia
import numpy as np
import matplotlib.pyplot as plt

nParticles = 20
iterations = 1000
c1 = 0.01
c2 = 0.01

x1 = np.random.rand(nParticles)
x1pl = x1
xlpg = 0
vx1 = np.zeros(nParticles)

x2 = np.random.rand(nParticles)
x2pl = x2
x2pg = 0
vx2 = np.zeros(nParticles)

x3 = np.random.rand(nParticles)
x3pl = x1
x3pg = 0
vx3 = np.zeros(nParticles)

fpl = 1000000 * np.ones(nParticles)
fpg = 1000000

for k in range(iterations):
  fp = -(-x1 * (10 + 100 * x1) - \
       x2 * (5 + 40 *x2) - x3 * (5 + 50 * x3))
  index = np.argmin(fp);
  if fp[index] < fpg:
    x1pg = x1[index]
    x2pg = x2[index]
    x3pg = x3[index]
    fpg = fp[index]

  for ind in range(nParticles):
    if fp[ind] < fpl[ind]:
      x1pl[ind] = x1[ind]
      x2pl[ind] = x2[ind]
      x3pl[ind] = x3[ind]
      fpl[ind] = fp[ind]

  vx1 = vx1 + c1 * np.random.rand(nParticles) * (x1pg - x1) \
          + c2 * np.random.rand(nParticles) * (x1pl - x1)
  x1 = x1 + vx1

  vx2 = vx2 + c1 * np.random.rand(nParticles) * (x2pg - x2) \
          + c2 * np.random.rand(nParticles) * (x2pl - x2)
  x2 = x2 + vx2

  vx3 = vx3 + c1 * np.random.rand(nParticles) * (x3pg - x3) \
          + c2 * np.random.rand(nParticles) * (x3pl - x3)
  x3 = x3 + vx3

plt.figure(1)
plt.axis([-1, 1, -1, 1])
plt.plot(x1, x2, 'b.', x1pg, x2pg, 'go', 0, 0, 'ro')
print('resultados: X1=%.4f, X2=%.4f, X3=%.4f, fp=%.4f' % (x1pg, x2pg, x3pg, fpg));

# resultados X1=-0.0499, X2=-0.0635, X3=-0.0503, fp=-0.5312
