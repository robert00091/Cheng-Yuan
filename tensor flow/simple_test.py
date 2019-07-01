'''
Date: 2019/7/1
Author: Cheng-Yuan Wang
Title: Tensorflow with using Keras to find the linear equation
'''

# -*- coding: UTF-8 -*-

import tensorflow as tf
import keras as ks
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
import numpy as np

model = ks.Sequential([ks.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype = float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype = float)

model.fit(xs, ys, epochs = 1000)
print(model.predict([10.0]))
