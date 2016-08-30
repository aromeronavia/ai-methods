# -*- coding: utf-8 -*-
"""

"""

import numpy as np;
import matplotlib.pyplot as plt;

#%%
# Definición de la función de inicialización
def initpob(npob,nbits,xmin,xmax):
    # xint = np.round(((2**nbits)-1)*np.random.rand(npob,1));
    #
    # npob = numero de pobladores
    # nbits = numero de bits del codigo genetico
    # xmin = limite inferior del espacio de busqueda
    # xmax = limite superior del espacio de busqueda
    xint = np.random.randint(2**nbits,size=(npob,1))
    xpob = ((xmax-xmin)/((2**nbits)-1))*xint+xmin;
    return xpob,xint

#%%
# Definición de la función de selección
def selecbest(npadres,xpob,xint,ypob,minmax):
  # Ordenar los pobladores según su desempeño.
  #
  # npadres = numero de padres que se quieren salvar
  # xpob = pobladores en el espacio de busqueda
  # xint = cromosoma en decimal
  # ypob = desempeño de los pobladores
  # minmax = 1 si se quiere maximizar y -1 si se quiere minimizar
  npob,ntemp = np.shape(xpob);
  temp = np.zeros((npob,3));
  temp[:,0] = ypob[:,0];
  temp[:,1] = xpob[:,0];
  temp[:,2] = xint[:,0];
  temp = temp[temp[:,0].argsort(),:];
  if minmax == 1:
    xpadres=temp[npob-npadres:npob,1];
    xintpadres=temp[npob-npadres:npob,2];
  elif minmax == -1:
    xpadres=temp[0:npadres,1];
    xintpadres=temp[0:npadres,2];
  else:
    print('No se eligio un argumento valido para minmax')
    return -1,1
  xpadres = xpadres.reshape((npadres,1));
  xintpadres = xintpadres.reshape((npadres,1));
  return xpadres,xintpadres

#%%
#Definición de la función de cruzamiento
def cruzamiento(xint,nhijo,nbits,xmin,xmax,method):
  # Realizacion de nhijo numero de pobladores nuevos a partir de xint
  #
  # xint = cromosoma en decimal
  # nhijo = numero de hijos que se quieren generar
  # nbits = numero de bits del cromosoma de los pobladores
  # xmin = limite inferior del espacio de busqueda
  # xmax = limite superior del espacio de busqueda

  npadre, ntemp = np.shape(xint)
  xinthijo = np.zeros((nhijo,1))
  xhijo = xinthijo
  if npadre == 1:
    print("Precuación: Con un solo padre no se tiene recombinación de genes")
  px = np.tile(np.arange(0,npadre),nhijo//npadre+1)
  for ind in range(0,nhijo):
    cromx = np.binary_repr(np.int(xint[px[ind],0]),width=nbits)
    cromy = np.binary_repr(np.int(xint[px[ind+1],0]),width=nbits)

    if method==1:
      # Metodo 1 para cruzamiento
      crombit = np.random.randint(nbits-1)+1;
      if ind%2 == 0:
        cromhijo = cromx[0:crombit]+cromy[crombit:10];
      else:
        cromhijo = cromy[crombit:10]+cromx[0:crombit];
    elif method==2:
			#Metodo 2 para cruzamiento "Doble punto cruce"
			cruce1 = np.random.randint(nbits - 1) + 1
			while True:
				cruce2 = np.random.randint(nbits - 1) + 1
				if (cruce2 != cruce1):
					break
			if cruce1 < cruce2:
				if ind % 2 == 0:
					cromhijo = cromx[0:cruce1] + cromy[cruce1:cruce2] + cromx[cruce2:nbits]
				else:
					cromhijo = cromy[0:cruce1] + cromx[cruce1:cruce2] + cromy[cruce2:nbits]
			else: # cruce2<cruce1:
				if ind % 2 == 0: #ver con que padre empieza el cruce
					cromhijo = cromx[0:cruce2] + cromy[cruce2:cruce1] + cromx[cruce2:nbits];
				else:
					cromhijo = cromy[0:cruce2] + cromx[cruce2:cruce2] + cromy[cruce2:nbits];
    elif method==3:
      cromhijo = [0 for i in range(nbits)]
      for i in range(nbits):
        randomCromNumber = np.random.randint(2)
        if (randomCromNumber == 0):
          cromhijo[i] = str(cromx[i])
        else:
          cromhijo[i] = str(cromy[i])

      cromhijo = ''.join(cromhijo)
      ##
    elif method==4:
      preliminarBinary = np.binary_repr(int(cromy, 2) + int(cromx, 2), width=nbits)
      if len(preliminarBinary) == 10:
        cromhijo = preliminarBinary
      else:
        cromhijo = preliminarBinary[1: ]
      ##

    xinthijo[ind,0]=int(cromhijo,2)
    xhijo[ind,0] = ((xmax-xmin)/(np.double(2**nbits)-1))*xinthijo[ind,0]+xmin
  return xhijo,xinthijo

#%%
#Definición de la función de cruzamiento
def mutacion(xint,nmut,nbits,xmin,xmax):
  # Realizacion de nmut numero de mutaciones en los pobladores xint
  #
  # xint = cromosoma en decimal
  # nmut = numero de mutantes que se queiren generar
  # nbits = numero de bits del cromosoma de los pobladores
  # xmin = limite inferior del espacio de busqueda
  # xmax = limite superior del espacio de busqueda
  nhijo,ntemp = np.shape(xint);
  for ind in range(0,nmut):
    nhijmut = np.random.randint(nhijo);
    nbitmut = np.random.randint(nbits);
    crom = np.binary_repr(np.int(xint[nhijmut,0]),width=nbits);
    if crom[nbitmut] == '1':
      crom = crom[0:nbitmut]+'0'+crom[nbitmut+1:nbits];
    else:
      crom = crom[0:nbitmut]+'1'+crom[nbitmut+1:nbits];
    xint[nhijmut,0]=int(crom,2);
  xmut = ((xmax-xmin)/((2**nbits)-1))*xint+xmin;
  return xmut,xint
#%%

def rast(x1, x2):
  return 10 + x1 ** 2 - 10 * np.cos(5 * x1) + \
         x2 ** 2 - 10 * np.cos(5 * x2)

def ackley(x1, x2):
  return -10 - np.exp(-np.sqrt(x1 ** 2)) \
      -np.exp(np.cos(5 * x1)) \
      -10 * np.exp(-np.sqrt(x2 ** 2)) \
      -np.exp(np.cos(5*x2)) + 10 + np.exp(1)

def rosen(x1, x2):
  return 100 * (x2-x1)**2 + (1 - x1)**2

