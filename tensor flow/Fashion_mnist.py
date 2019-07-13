'''
Date: 2019/7/13
Author: Cheng-Yuan Wang
Title: Using Tensorflow's datasets Fasion Mnist to learn computer vision
'''

import tensorflow as tf
import matplotlib.pyplot as plt

# Check the accuracy and stop it
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('loss')<0.4):
      print("\nReached 60% accuracy so cancelling training!")
      self.model.stop_training = True

callbacks = myCallback()
# Import fashion mnist database
f_mnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) = f_mnist.load_data()
plt.imshow(training_images[0])

# Normalize data
training_images=training_images/255.0
test_images=test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(512, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metics = ['accuracy'])
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])

plt.show()