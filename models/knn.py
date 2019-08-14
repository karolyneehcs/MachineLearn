import math 
import pandas as pd 
import csv 
import math 
import random  
import operator
import numpy as np
import pandas as pd 
import scipy
from scipy.spatial import distance
from random import shuffle 
from scipy import stats

class Knn:

	k = 2 #numero de vizinhos mais proximos 
	trainFeatures = [] #criando uma matriz com as features 
	trainLabels = [] #criando uma matriz ou array com labels de treino 

	def __init__(self, params):
		if 'k' in params:
			self.k = params['k']

	def train(self, input, output):
		self.trainFeatures = input
		self.trainLabels = output

	def test(self, input): 
		dist_euclidean = distance.cdist(self.trainFeatures,input,'euclidean')
		dist_euclidean = dist_euclidean.transpose()
			
		#matriz de zeros para definir o tamanho das distancias 
		outs = np.zeros(dist_euclidean.shape[0])

		#moda das distancias euclidianas 
		for i, rows in enumerate(dist_euclidean):
			idx = np.argsort(rows)
			idx = idx[0:self.k]
			rot = self.trainLabels[idx]
			out = stats.mode(rot)[0][0]
			outs [i] = out 
		return outs 



	

