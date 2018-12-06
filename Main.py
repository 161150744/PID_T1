import sys
from skimage import data, io, filters, exposure
import matplotlib.pyplot as plt
import pandas as pd

def showBar(image):
    edges = filters.sobel(image)
    plt.bar( exposure.histogram(image)[1], exposure.histogram(image)[0])
    plt.show()

def getHistogram(image):
    edges = filters.sobel(image)
    return exposure.histogram(image)

def getGroup(listG):
    theBiggest = 0
    for i in range(len(listG)):
        if listG[theBiggest] < listG[i]:
            theBiggest = i
    return theBiggest

def main(args):
    groups = []
    histogram = getHistogram(data.horse())
    nDivX = int(args[0])
    for i in range(nDivX):
        groups.append([])
    nDivY = int(args[1])
    stepX = len(histogram[1])/nDivX
    stepY = len(histogram[0])/nDivY

if __name__ == '__main__':
    main(sys.argv[1:])
