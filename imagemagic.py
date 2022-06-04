import numpy as np

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
def rot90(x, y):
    A = [[0, -1], 
         [1, 0]]
    return np.dot(A, [x, y]).tolist()