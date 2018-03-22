'''
You can specify both values you want to start with and the ones you'd like to finish with
'''

'''
In order to see the results of binarization you'll see a simple demo- before and after photo taken from skimage database with their histograms
'''

import matplotlib.pyplot as plt
from skimage import data, exposure
import numpy as np

def histogram(img):
    hist, bins = exposure.histogram(img)
    plt.plot(25* bins, hist)
    plt.grid('on')
    plt.show()


def present(img, suptitle):
    plt.imshow(img, cmap='gray')
    plt.suptitle(suptitle)
    plt.axis('off')
    plt.show()
    histogram(img)
    
def binarization(img, bottomValue, topValue, newBottom, newTop):
    #all 4 parameters are supposed to be between 0 and 255
    imgFinal = np.copy(img)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if(img[x][y] < bottomValue):
                imgFinal[x][y] = newBottom
            elif(img[x][y] > topValue):
                imgFinal[x][y] = newTop

    present(img, "First")
    present(imgFinal, "Second")


binarization(data.coins(), 100, 200, 0, 255)
