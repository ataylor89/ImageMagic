import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

# Algorithm
# 1. Create an XY coordinate system with an origin at the center of the image
# 2. Get the XY coordinates of the corners of the image 
# 3. Apply a linear transformation to the corners of the image
#    Let A be the matrix of the transformation
#    Let V be a matrix that has the xy coordinates of the corners as column vectors
#    Then the xy coordinates of the new image are given by the transformation
#    T = AV
# 4. Calculate the dimensions of the new image N and M from the equations
#    N = ymax-ymin + 1
#    M = xmax-xmin + 1
#    where ymax, ymin = max(T[1]), min(T[1])
#    and xmax, xmin = max(T[0]), min(T[0])
#    N is the number of rows in the new image and M is the number of columns
# 5. Let X be a matrix that has the coordinates of every pixel from the image as a column vector
#    Let A be the matrix of transformation
#    Then the corresponding coordinates in the new image are given by the transformation
#    Y = AX 
# 6. Get the row and column values for every column vector in matrices X and Y 
#    and copy the RGB values from the old image into the new image
#    using the appropriate row and column values

# Converting between row column values and xy coordinates
# Let (x,y) be the coordinates of pixel P in an nxm image
# The upper left corner of the image has coordinates (-m/2, n/2)
# The position of P relative to the upper left corner is 
# (i, j) = (|x - (-m/2)|, |y - n/2|) 
#        = (|x + m/2|, |y - n/2|) 
#        = (x + m/2, n/2 - y)
# The row and column values are given by 
# row = floor(j) = int(n/2 - y)
# col = floor(i) = int(x + m/2)

# Gets the x, y coordinates of a pixel in an nxm image
def get_xy(row, col, n, m):
    i, j = col + 0.5, row + 0.5
    return [i - m/2, n/2 - j]

# Gets the row and column of a pixel in an nxm image
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

    # Get the dimensions of the new (transformed) image
    V = (np.array([-m/2, n/2]), np.array([-m/2, -n/2]), np.array([m/2, n/2]), np.array([m/2, -n/2]))
    V = np.column_stack(V)
    # Perform the linear transformation T = AV on the corners of the original image
    T = np.dot(A, V)
    xmax, xmin = max(T[0]), min(T[0])
    ymax, ymin = max(T[1]), min(T[1])
    print('xmax=%1.2f xmin=%1.2f' %(xmax, xmin))
    print('ymax=%1.2f ymin=%1.2f' %(ymax, ymin))
    # The dimensions of the new image are N rows and M columns
    N, M = int(ymax-ymin), int(xmax-xmin)
    print("N=%d\nM=%d" %(N, M))

    # Get the xy coordinates for every pixel and store as column vectors in matrix X
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

    # Copy the RGB values from img into the appropriate pixel in canvas 
    num_cols = len(X[0])
    for col in range(num_cols):
        x, y = X[0][col], X[1][col]
        xt, yt = Y[0][col], Y[1][col]
        [row, col] = get_rowcol(x, y, n, m)
        [row_t, col_t] = get_rowcol(xt, yt, N, M)
        canvas[row_t][col_t] = img[row][col]

    return canvas