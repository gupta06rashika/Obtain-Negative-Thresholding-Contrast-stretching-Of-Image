from PIL import Image
import numpy as np


# reading the image and store it in img object
img = Image.open("c:\\Users\\User\\Downloads\\ex4.jpg");

#convert to grey image
gray_img = img.convert(mode='L')

#convert image to array
img_to_array = np.asarray(gray_img)


#Find Min and Max of Image Array
minn,maxx = [np.amin(img_to_array), np.amax(img_to_array)]

#Make a empty array that will store contrast stretched array
contrast_array = []

#looping on pixel tochange in between range
for i in range(img.size[1]):
    contrast_array.append(list(255*(x-minn)/(maxx-minn) for x in img_to_array[i]))

#Convert again to image from array
contrast_image = Image.fromarray(np.array(contrast_array).astype('uint8'))

#save the contrast image
contrast_image.save('c:\\Users\\User\\Downloads\\Contrast.jpg')

