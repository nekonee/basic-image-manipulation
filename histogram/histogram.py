from skimage import io, data
import matplotlib.pyplot as plt

'''
   Basic histogram function using coins image as an example
'''

image = data.coins()

plt.imshow(image, cmap="gray")
plt.axis('off')
plt.show()
print(image.shape, image.dtype)


def histogram(image):
    wartosci = [0 for _ in range(256)]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
             w = image[i,j]
             wartosci[w] += 1
             
    for w in range(256):
        print("Value: ", w, "\n number of pixels: ", wartosci[w])


histogram(image)
