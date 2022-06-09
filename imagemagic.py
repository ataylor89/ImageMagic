import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

# Gets the x, y coordinates of a pixel in an nxm image
# The origin of the xy coordinate system is at the center of the image
def get_xy(row, col, n, m):
    i, j = col + 0.5, row + 0.5
    return [i - m/2, n/2 - j]

# Gets the row and column of a pixel in an nxm image
# The origin of the xy coordinate system is at the center of the image
def get_rowcol(x, y, n, m):
    return [int(n/2 - y), int(x + m/2)]

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
            np.array(get_xy(0, m-1, n, m)),
            np.array(get_xy(n-1, 0, n, m)),
            np.array(get_xy(n-1, m-1, n, m)))
    V = np.column_stack(V)
    # Perform the linear transformation T = AV to get the transformed vertices
    T = np.dot(A, V)
    xmax, xmin = max(T[0]), min(T[0])
    ymax, ymin = max(T[1]), min(T[1])
    print('xmax=%1.2f xmin=%1.2f' %(xmax, xmin))
    print('ymax=%1.2f ymin=%1.2f' %(ymax, ymin))
    N, M = int(round(ymax-ymin))+1, int(round(xmax-xmin))+1
    print("N=%d\nM=%d" %(N, M))

    # Get the xy coordinates for every pixel and store as column vectors in matrix X
    # The origin of the xy coordinate system is at the center of the image 
    X = []
    for row in range(n):
        for col in range(m):
            vertex = get_xy(row, col, n, m)
            X.append(np.array(vertex))
    X = tuple(X)
    X = np.column_stack(X)  

    # Perform the linear transformation Y = AX
    # Y contains the new coordinates for every pixel
    Y = np.dot(A, X)

    # Create a matrix for our new image
    # Let's call it canvas
    # The new matrix has N rows and M columns
    canvas = [[[255, 255, 255] for i in range(M)] for j in range(N)]

    # Copy the RGB values in img to the appropriate row and column in canvas 
    num_cols = len(X[0])
    for col in range(num_cols):
        x, y = X[0][col], X[1][col]
        xt, yt = Y[0][col], Y[1][col]
        [row, col] = get_rowcol(x, y, n, m)
        [row_t, col_t] = get_rowcol(xt, yt, N, M)
        canvas[row_t][col_t] = img[row][col]

    return canvas