import csv 
import math 
import random  
import operator
import numpy as np
import pandas as pd 
import scipy
from scipy.spatial.distance import cdist
from random import shuffle 
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


# constantes
porc = 0.8 # porcentagem de treino
K = 50  # vizinhos proximos
iris_data = np.array(pd.read_csv('./datasets/real/iris/data.csv'))
#separando arrays de dados e labels 
def labels (data): 
	data.copy()
	labels1 = np.zeros(data[:,-1].shape)
	matriz_treino = np.zeros(data[:,0:3].shape)
	return labels1, matriz_treino
#chamada da primeira funcao 
labels_treino, matriz_zeros = labels (iris_data)

#criando uma matriz fracionada 
def fracionamento (data,porcentagem):
	copy = data.copy()
	random.shuffle(copy)
	data_full = data.shape[0]
	data_porc = int (data_full*porcentagem)

	#matriz de teste e treino 
	data_treino = copy[0:data_porc,0:-1]
	label_treino = copy[0:data_porc, -1]

	data_teste = copy[data_porc:data_full, 0:-1]
	label_teste = copy[data_porc:data_full, -1]
	return label_treino, data_teste, data_treino 

#chamada da funcao 
treino_l, data_test, treino_dado = fracionamento(iris_data,porc)
def mode_euclidean_distances(data_test,treino_dado,data_ult):
	dist_euclidean = distance.cdist(treino_dado,data_test,'euclidean')
	
	#matriz de zeros para definir o tamanho das distancias 
	outs = np.zeros(dist_euclidean.shape[0])

	#moda das distancias euclidianas 
	for i, rows in enumerate(dist_euclidean):
		idx = np.argsort(rows)
		idx = idx[0:K]
		rot = data_ult[idx]
		out = stats.mode(rot)[0][0]
		outs [i] = out 
	return outs 

#chamada das distancias euclidianas 
moda_dists = mode_euclidean_distances(data_test,treino_dado,treino_l)

#alterando a escala da base de dados 
def scale (data):
	x_scale = np.zeros(len(data[:,0]))
	for i in range(len(data[:,0])):
		x_scale[i] = (data[i][0]-4.3)/3.6
	y_scale = np.zeros(len(data[:,1]))
	for i in range(len(data[:,1])):
		y_scale[i] = (data[i][1]-2)/2.4
	return x_scale, y_scale	
#chamada da função de escala
escala_x, escala_y = scale(iris_data)	

#criando uma função para retornar os minimos e os maximos da base de dados
def max_minXY (escala1, escala2):
	Ix = np.argsort(escala1)
	Iy = np.argsort(escala2)
	max_X = escala_x[Ix[-1]]
	min_X = escala_x[Ix[0]]
	max_Y = escala_y[Iy[-1]]
	min_Y = escala_y[Iy[0]]
	return max_X,min_X,max_Y,min_Y

maximum_X,minimum_X,maximum_Y,minimum_Y = max_minXY(escala_x,escala_y)
#tentativa 1 para criacao de pontos de teste 
x = np.linspace(minimum_X,maximum_X)
y = np.linspace(minimum_Y,maximum_Y)
pointsx,pointsy = np.meshgrid(x,y)

pointsx = np.array(pointsx)
pointsy = np.array(pointsy)

pointsx = pointsx.reshape(pointsx.shape[0]*pointsx.shape[1])
pointsy = pointsy.reshape(pointsy.shape[0]*pointsy.shape[1])

#criando um novo array com duas dimensoes
newScale = np.zeros((len(escala_x),2))
for i in range(len(newScale)):
	newScale[i][0] = escala_x[i]
for i in range(len(escala_x),2):
	newScale[i][1] = escala_y[i]

datasetTest = np.array([pointsx,pointsy]).transpose()

#calculando as distancias euclidianas do novo banco de dados
pointsTest = mode_euclidean_distances(datasetTest[:,:],newScale[:,0:2],iris_data[:,4])

#configurando as cores
coresLabelIris = ['']*len(iris_data[:,-1])
coresLabelTest = ['']*len(pointsTest)

for i in range(len(iris_data[:,-1])):
	if iris_data[i][-1] == 1: 
		coresLabelIris[i] = 'r'
	elif iris_data[i][-1] == 2:
		coresLabelIris[i] = 'dodgerblue'
	else: 
		coresLabelIris[i] = 'limegreen'

for i in range(len(pointsTest)):
	if pointsTest[i] == 1: 
		coresLabelTest[i] = 'orangered'
	elif pointsTest[i] == 2:
		coresLabelTest[i] = 'darkblue'
	else: 
		coresLabelTest[i] = 'darkgreen'

fig, ax = plt.subplots()
ax.scatter(pointsx, pointsy,c = coresLabelTest)	
ax.set_xlabel(r'$X$', fontsize=15)
ax.set_ylabel(r'$Y$', fontsize=15)
ax.set_title('data points')

ax.scatter(escala_x,escala_y, c = coresLabelIris)
plt.show()