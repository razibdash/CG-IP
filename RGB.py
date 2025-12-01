from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

img_path = "Cat03.jpg"
image = Image.open(img_path)

image_array = np.array(image)

print("Image Array are given below\n")
print(image_array)
print("Image shape ", image_array.shape)

red_channel = image_array[:, :, 0]
green_channel = image_array[:, :, 1]
blue_channel = image_array[:, :, 2]

plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.imshow(red_channel, cmap='Reds')
plt.title("Red Channel")

plt.subplot(132)
plt.imshow(green_channel, cmap='Greens')
plt.title("Green Channel")

plt.subplot(133)
plt.imshow(blue_channel, cmap='Blues')
plt.title("Blue Channel")

plt.show()