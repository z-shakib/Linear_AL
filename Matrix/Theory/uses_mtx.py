import numpy as np
from scipy.signal import convolve2d

#! Image Representation: black and white-
image = np.array([[0, 255, 0],
                  [255, 0, 255],
                  [0, 255, 0]])
print("Black-and-White Image Matrix:")
print(image)

#!in Machine learning for model training and predictions:
X = np.array([[1.2, 0.8, 2.5],
              [0.5, 1.3, 0.7],
              [2.0, 1.8, 1.1]]) #Data set as a matrix
print("Dataset Matrix:")
print(X)

#! Computer vision:
img = np.array([[1, 1, 1],
                  [0, 0, 0],
                  [1, 1, 1]]) #! example image matrix

#! Filter matrix (edge detection kernel)
kernel = np.array([[-1, -1, -1],
                   [ 0,  0,  0],
                   [ 1,  1,  1]])
#! Convolution:
result = convolve2d(img, kernel, mode='valid')
print('Convolved Matrix (Edge Detection): ')
print(result)


#! Neural Networks: (Deep Learning)
W = np.array([[0.2, 0.4],
              [0.6, 0.8]]) # Neural Network weight matrix

#! Input Vector:
X = np.array([1, 0.5])

#! Matrix Multiplication.
Y = np.dot(W, X)
print("Neural Network Layer Output:")
print(Y)