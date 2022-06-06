import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

# Gets the (x, y) coordinates of pixel (i, j) in an nxm matrix
# i is the column and j is the row
# The xy coordinate system has an origin at the center of the matrix
def get_xy(i, j, n, m):
    return [i - (m-1)/2, (n-1)/2 - j]

# Gets the (i, j) values for a pixel with coordinates (x, y) in an nxm matrix
# i is the column and j is the row
# The xy coordinate system has an origin at the center of the matrix
#
# Equations:
# x = i - m/2 
# i = x + m/2
# y = n/2 - j 
# j = n/2 - y
def get_ij(x, y, n, m):
    return [int(x + (m-1)/2), int((n-1)/2 - y)]

# Rotates an image around the origin by the specified number of radians
def rot_img(filename, radians):
    # Read the image from file
    img = mpimg.imread(filename)
    n, m = len(img), len(img[0])
    print('%dx%d matrix (%s)' %(n, m, filename))

    # Create the rotation matrix A
    A = [[math.cos(radians), -1 * math.sin(radians)],
         [math.sin(radians), math.cos(radians)]]

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
    N, M = int(ymax-ymin)+2, int(xmax-xmin)+2

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

    # Write the new image (after transformation) to canvas
    num_cols = len(X[0])
    for col in range(num_cols):
        x, y = X[0][col], X[1][col]
        xt, yt = Y[0][col], Y[1][col]
        [i, j] = get_ij(x, y, n, m)
        [it, jt] = get_ij(xt, yt, N, M)
        canvas[jt][it] = img[j][i]

    return canvas