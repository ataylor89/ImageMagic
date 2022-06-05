import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

# Creates a square matrix to contain the image, and centers the image in the canvas
def make_canvas(img):
    n = len(img)
    m = len(img[0])
    N = max(n, m) * 2
    # We create a blank white canvas from an NxN square matrix
    canvas = [[[255, 255, 255] for i in range(N)] for j in range(N)]
    for row in range(n):
        for col in range(m):
            # We shift our image horizontally by m/2 and vertically by m-n/2
            canvas[row+int(m-n/2)][col+int(m/2)] = img[row][col]
    return canvas

# Gets the (x, y) coordinates of pixel (i, j) in an nxn square matrix
def get_xy(i, j, n):
    return [i - n/2, n/2 - j]

# Gets the (i, j) values for pixel (x, y) in an nxn square matrix
def get_ij(x, y, n):
    # x = i - n/2 
    # i = x + n/2
    # y = n/2 - j 
    # j = n/2 - y
    return [int(x + n/2), int(n/2 - y)]

# Rotates an image around the origin by T radians
def rot_img(filename, T):
    # Read the image from file
    img = mpimg.imread(filename)
    n, m = len(img), len(img[0])
    print('%dx%d matrix (%s)' %(n, m, filename))

    # Make a blank white canvas to contain the image
    canvas = make_canvas(img)
    N = len(canvas)
    print('%dx%d canvas' %(N, N))

    # Make a blank white canvas for the new image
    # We are using the letter 't' as a prefix or suffix to mean "transformed"
    tcanvas = [[[255, 255, 255] for i in range(N)] for j in range(N)]

    # Create a matrix X for the (x, y) coordinates of image pixels
    X = []
    for row in range(10, N-10):
        for col in range(10, N-10):
            vertex = get_xy(col, row, N)
            X.append(np.array(vertex))
    X = tuple(X)
    X = np.column_stack(X)  

    # Multiply X by the rotation matrix and store in a new matrix Y
    A = [[math.cos(T), -1 * math.sin(T)],
         [math.sin(T), math.cos(T)]]
    Y = np.dot(A, X)

    # Write the new image (after transformation) to its canvas
    num_vertices = len(X[0])
    for i in range(num_vertices):
        x, y = X[0][i], X[1][i]
        xt, yt = Y[0][i], Y[1][i]
        [i, j] = get_ij(x, y, N)
        [it, jt] = get_ij(xt, yt, N)
        tcanvas[jt][it] = canvas[j][i]

    return tcanvas