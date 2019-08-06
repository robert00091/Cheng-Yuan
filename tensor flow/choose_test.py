import os
import matplotlib.pyplot as plt
import matplotlib.image as mp
import tensorflow as tf
import numpy as np
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from PIL import Image


# Directory with our training horse pictures
train_horse_dir = os.path.join('horses')
# Directory with our training human pictures
train_human_dir = os.path.join('humans')

train_horse_names = os.listdir(train_horse_dir)
#print(train_horse_names[:8])

train_human_names = os.listdir(train_human_dir)
#print(train_human_names[:8])


#print(train_horse_dir[:10])
#print(train_human_dir[:10])

rows, cols = 4, 4


fig = plt.gcf()
fig.set_size_inches(cols * 4, rows * 4)

pic_index = 8
next_horse_pix = [os.path.join(train_horse_dir, fname)
                for fname in train_horse_names[pic_index-8:pic_index]]

next_human_pix = [os.path.join(train_human_dir, fname)
                for fname in train_human_names[pic_index-8:pic_index]]

# Show up the pictures
for i, img_path in enumerate(next_horse_pix+next_human_pix):
  # Set up subplot; subplot indices start at 1
  sp = plt.subplot(rows, cols, i + 1)
  sp.axis('Off') # Don't show axes (or gridlines)

  img = mp.imread(img_path)
  plt.imshow(img)

plt.show()


# Begin training those pictures
model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 300x300 with 3 bytes color
    # This is the first convolution
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # The second convolution
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The third convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fourth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # The fifth convolution
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    # Only 1 output neuron. It will contain a value from 0-1 where 0 for 1 class ('horses') and 1 for the other ('humans')
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['acc'])

# All images will be rescaled by 1./255
train_datagen = ImageDataGenerator(rescale=1/255)

# Flow training images in batches of 128 using train_datagen generator
train_generator = train_datagen.flow_from_directory(
        '../horse-or-human/',  # This is the source directory for training images
        target_size=(300, 300),
        batch_size=128,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

history = model.fit_generator(
      train_generator,
      steps_per_epoch=8,
      epochs=15,
      verbose=1)


# Judge images
image = Image.open('beauty.jpg')
target = (300,300)
img = image.resize(target) # Resize the picture
x = img_to_array(img)
x = np.expand_dims(x, axis=0) # Extend the dimension

images = np.vstack([x])
classes = model.predict(images, batch_size=10)
print(classes[0])

if classes[0] > 0.5:
    print( "Image is a human.")
else:
    print("Image is a horse.")
