import matplotlib 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class Surface: 
	
	model = []
	input = [] # 
	output = []
	min_X = 0.0
	max_X = 0.0 
	min_Y = 0.0
	min_Y = 0.0
	


	def __init__(self, model, input, output):
		self.model = model
		self.input = input 
		self.output = output
		self.min_X = min(self.input[:,0]) #selecionar o valor minimo do array x
		self.max_X = max(self.input[:,0]) #selecionar o valor maximo do array x 
		self.min_Y = min(self.input[:,1]) #seleciona o valor minimo do array y 
		self.max_Y = max(self.input[:,1]) #seleciona o valor maximo do array y 

	def plot(self): 
		x = np.linspace(self.min_X,self.max_X,150)
		y = np.linspace(self.min_Y,self.max_Y,150)
		pointsx,pointsy = np.meshgrid(x,y)

		pointsx = np.array(pointsx)
		pointsy = np.array(pointsy)

		pointsx = pointsx.reshape(pointsx.shape[0]*pointsx.shape[1])
		pointsy = pointsy.reshape(pointsy.shape[0]*pointsy.shape[1])

		plots = np.array([pointsx,pointsy]).transpose() 
		out = self.model.test(plots)

		fig, ax = plt.subplots()
		ax.scatter(pointsx, pointsy,c = out)
		ax.set_xlabel(r'$X$', fontsize=15)
		ax.set_ylabel(r'$Y$', fontsize=15)
		ax.set_title('data points')
	
		plt.plot(self.input[self.output==1., 0], self.input[self.output==1., 1], '.')
		plt.plot(self.input[self.output==2., 0], self.input[self.output==2., 1], '.')
		plt.show()		
 
		