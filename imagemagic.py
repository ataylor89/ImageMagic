import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Creates a square matrix to contain the image, and centers the image in the canvas
def make_canvas(img):
    n = len(img)
    m = len(img[0])
    N = max(n, m) * 2
    # Let's create an NxN blank white canvas 
    canvas = [[[255, 255, 255] for i in range(N)] for j in range(N)]
    for row in range(n):
        for col in range(m):
            # We shift our image horizontally by m/2 and vertically by m-n/2
            # Horizontal shift = m - m/2 = m/2
            # Vertical shift = m - n/2
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

# Rotates a vector 90 degrees counterclockwise around the origin
def rot_vec_90(x, y):
    A = [[0, -1], 
         [1, 0]]
    return np.dot(A, [x, y]).tolist()

# Rotates an image 90 degrees counterclockwise around the origin
def rot_img_90(filename):
    img = mpimg.imread(filename)
    n, m = len(img), len(img[0])
    print('%dx%d matrix (%s)' %(n, m, filename))

    canvas = make_canvas(img)
    N = len(canvas)
    print('%dx%d canvas' %(N, N))

    tcanvas = [[[255, 255, 255] for i in range(N)] for j in range(N)]
    for row in range(int(n/2), int(N-n/2)):
        for col in range(int(m/2), int(N-m/2)):
            [x, y] = get_xy(col, row, N)
            [x, y] = rot_vec_90(x, y)
            [i, j] = get_ij(x, y, N)
            tcanvas[j][i] = canvas[row][col]
    return tcanvas