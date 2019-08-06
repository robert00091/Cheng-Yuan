Horse & Human Judgement
===

![image](https://github.com/robert00091/Cheng-Yuan/blob/master/tensor%20flow/Photo_judge/horse.jpg)


Download the training pictures and unzip the folder
----
```
https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip 
```

Judge the pictures
----

``` Python

image = Image.open('Your picture')
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

```
