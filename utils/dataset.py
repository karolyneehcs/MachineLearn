import csv
import numpy as np
import pandas as pd
import math

class Dataset:

	basepath='../datasets'
	percs=[80, 0, 20]
	normType='range' # mean
	trainFeatures=[]
	trainLabels=[]
	validationFeatures=[]
	validationLabels=[]
	testFeatures=[]
	testLabels=[]

	def __init__(self, params):

		if not 'path' in params:
			print('path não informado nos parâmetros do construtor.\n')
			return 

		self.data = np.array(pd.read_csv('{}/{}/data.csv'.format(self.basepath, params['path'])))
		self.features = self.data[:, 0:-1];
		self.labels = self.data[:, -1];


		if 'percs' in params:
			self.percs = params['path']	
		
		if 'normType' in params:
			self.normType = params['normType']	



		#TODO: validar se a soma dos elementos de self.percs é diferente de 100
		#TODO: mensagens caso o parâmetro path não seja informado				
	
	def normalize(self):
		minim = np.min(self.features)
		maxim = np.max(self.features)
		self.features = (self.features - minim) / (maxim - minim)

	def shuffle(self):
		nTrain = math.ceil((self.percs[0]/100) * len(self.labels))
		nValid = math.ceil((self.percs[1]/100) * len(self.labels))
		nTests = math.ceil((self.percs[2]/100) * len(self.labels))
		
		inds   = np.random.permutation(len(self.labels))

		trainInds = inds[0:nTrain]
		validInds = inds[nTrain:(nTrain+nValid)]
		testsInds = inds[(nTrain+nValid)-1:(nTrain+nValid+nTests)]

		self.trainFeatures = self.features[trainInds, :]
		self.trainLabels = self.labels[trainInds]
		self.validationFeatures = self.features[validInds, :]
		self.validationLabels = self.labels[validInds]
		self.testFeatures = self.features[testsInds]
		self.testLabels = self.labels[testsInds]
