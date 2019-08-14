import sys
sys.path.append('../utils')
sys.path.append('../models')


from dataset import Dataset
from plot_surface import Surface
from knn import Knn
from acc import Accuracy
import numpy as np 
from sklearn.metrics import accuracy_score

#prepara dataset
ds = Dataset({'path': 'artificial/spiral'});
ds.normalize()
ds.shuffle()

#treinamento do modelo
params = {
	'k': 2
}
knn = Knn(params)

knn.train(ds.trainFeatures, ds.trainLabels)
out = knn.test(ds.testFeatures)

plt = Surface(knn, ds.testFeatures, ds.testLabels)
plt.plot()

acc = accuracy_score(ds.testLabels, out)
print (acc)
