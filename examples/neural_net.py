from sklearn import datasets
from deep_learning import layers
from deep_learning.losses import MAE, CrossEntropy
from deep_learning.util import one_hot
from deep_learning.optimizers import SGD
from deep_learning.initializers import HeNormal, HeUniform, XavierNormal, XavierUniform
from deep_learning.neural_network import NeuralNetwork

data = datasets.load_digits()
x = data.data
y = data.target

x = x / 256.

y = one_hot(y)
print(x.shape, y.shape)

opt = SGD(lr=1/1000)
cross_entropy = CrossEntropy()
# initializer = HeUniform()
initializer = HeNormal()


model = NeuralNetwork(opt, cross_entropy)
model.add(layers.Input(input_shape=(x.shape)))
model.add(layers.Dense(16, activation='relu', initializer=initializer))
model.add(layers.Dense(8, activation='relu', initializer=initializer))
model.add(layers.Dense(10, activation='softmax'))
model.summary()
model.fit(x, y, 100, verbose=0)
acc = model.evaluate(x, y)
print(f"Accuracy {acc:.3f} on training set")
