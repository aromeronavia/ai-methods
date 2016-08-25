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
  xpob = ((xmax-xmin)/(np.double(2**nbits)-1))*xint+xmin;
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
def cruzamiento(xint,nhijo,nbits,xmin,xmax):
  # Realizacion de nhijo numero de pobladores nuevos a partir de xint
  #
  # xint = cromosoma en decimal
  # nhijo = numero de hijos que se quieren generar
  # nbits = numero de bits del cromosoma de los pobladores
  # xmin = limite inferior del espacio de busqueda
  # xmax = limite superior del espacio de busqueda

  npadre,ntemp = np.shape(xint);
  xinthijo=np.zeros((nhijo,1));
  xhijo=xinthijo;
  if npadre==1:
    print("Precuación: Con un solo padre no se tiene recombinación de genes")
  px = np.tile(np.arange(0,npadre),nhijo//npadre+1);
  for ind in range(0,nhijo):
    cromx = np.binary_repr(np.int(xint[px[ind],0]),width=nbits);
    cromy = np.binary_repr(np.int(xint[px[ind+1],0]),width=nbits);
    crombit = np.random.randint(nbits-1)+1;
    # Metodo 1 para cruzamiento
    if ind%2 == 0:
      cromhijo = cromx[0:crombit]+cromy[crombit:10];
    else:
      cromhijo = cromy[crombit:10]+cromx[0:crombit];

    #Metodo 2 para cruzamiento
    ##

    #Metodo 3 para cruzamiento
    ##

    #Metodo 4 para cruzamiento
    ##

    xinthijo[ind,0]=int(cromhijo,2);
    xhijo[ind,0] = ((xmax-xmin)/(np.double(2**nbits)-1))*xinthijo[ind,0]+xmin;
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
  xmut = ((xmax-xmin)/(np.double(2**nbits)-1))*xint+xmin;
  return xmut,xint

#%%
