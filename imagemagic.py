import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

# Gets the (x, y) coordinates of pixel (i, j) in an nxm matrix
# i is the column and j is the row
# The xy coordinate system has an origin at the center of the image
def get_xy(i, j, n, m):
    return [i - (m-1)/2, (n-1)/2 - j]

# Gets the (i, j) values in an nxm matrix for a pixel with coordinates (x, y) 
# i is the column and j is the row
# The xy coordinate system has an origin at the center of the image
#
# Equations:
# x = i - (m-1)/2 
# i = x + (m-1)/2
# y = (n-1)/2 - j 
# j = (n-1)/2 - y
#
# For example if n=100, m=200
# Then the vertices of the image are (99.5, 49.5), (-99.5, 49.5), (-99.5, -49.5), (99.5, -49.5)
def get_ij(x, y, n, m):
    return [int(round(x + (m-1)/2)), int(round((n-1)/2 - y))]

# Rotates an image around the origin by the specified number of radians
def rotate(filename, radians):
    A = [[math.cos(radians), -1 * math.sin(radians)],
         [math.sin(radians), math.cos(radians)]]
    return transform(filename, A)

# Reflects an image around the x axis in an xy coordinate system
def reflectx(filename):
    A = [[1, 0],
         [0, -1]]
    return transform(filename, A)

# Reflects an image around the y axis in an xy coordinate system
def reflecty(filename):
    A = [[-1, 0], 
         [0, 1]]
    return transform(filename, A)

def transform(filename, A):
    # Read the image from file
    img = mpimg.imread(filename)
    n, m = len(img), len(img[0])
    print('%dx%d matrix (%s)' %(n, m, filename))

    # Get the dimensions for our new image
    # N is the number of rows, M is the number of columns
    # V and T are vertex matrices 
    V = (np.array(get_xy(0, 0, n, m)), 
            np.array(get_xy(m-1, 0, n, m)),
            np.array(get_xy(0, n-1, n, m)),
            np.array(get_xy(m-1, n-1, n, m)))
    V = np.column_stack(V)
    # Perform the linear transformation T = AV to get the transformed vertices
    T = np.dot(A, V)
    xmax, xmin = max(T[0]), min(T[0])
    ymax, ymin = max(T[1]), min(T[1])
    print('xmax=%1.2f xmin=%1.2f' %(xmax, xmin))
    print('ymax=%1.2f ymin=%1.2f' %(ymax, ymin))
    N, M = int(round(ymax-ymin))+1, int(round(xmax-xmin))+1
    print("N=%d\nM=%d" %(N, M))

    # Convert to a new coordinate system with (x, y) coordinates and an origin at the center of the image
    # Store the (x, y) coordinates of every pixel as column vectors in X
    X = []
    for row in range(n):
        for col in range(m):
            vertex = get_xy(col, row, n, m)
            X.append(np.array(vertex))
    X = tuple(X)
    X = np.column_stack(X)  

    # Perform the linear transformation Y = AX
    # Y contains the transformed vectors
    Y = np.dot(A, X)

    # Create a matrix for our new image
    # Let's call it canvas
    # The new matrix has N rows and M columns
    canvas = [[[255, 255, 255] for i in range(M)] for j in range(N)]

    # Copy the RGB values in img to the appropriate row and column in canvas 
    # Convert between coordinate systems to get the new position of values
    num_cols = len(X[0])
    for col in range(num_cols):
        x, y = X[0][col], X[1][col]
        xt, yt = Y[0][col], Y[1][col]
        [i, j] = get_ij(x, y, n, m)
        [it, jt] = get_ij(xt, yt, N, M)
        canvas[jt][it] = img[j][i]

    return canvas