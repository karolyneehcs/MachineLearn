#TODO fazer retornar somente a accuracy total do modelo


import numpy as np 
import scipy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import math 




class CrossValidation:

	treinoLabels = []
	dataTreino = []
	n = None 


	def __init__(self, treinoLabels, dataTreino,number):
		self.treinoLabels = treinoLabels
		self.dataTreino = dataTreino
		self.number = n

		print ("Realizando a validação\n")

	def nFolders(self):
		bFolders = math.ceil((len(dataTreino))/self.number)

		matrixF = np.zeros((n,bFolders))
		matrixFLabels = np.zeros((n,bFolders))
		m = 1

		for i in range (n):
			for j in range (bFolders):
				matrixF[i][j] = self.dataTreino[j*m]
				matrixFLabels[i][j] = self.treinoLabels[i*m]
				m = m + 1 	
		

			









