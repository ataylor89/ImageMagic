import imagemagic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

FILENAME = 'stacksofwheat.jpg'
img = mpimg.imread(FILENAME)
n = len(img)
m = len(img[0])
print('%dx%d matrix (%s)' %(n, m, FILENAME))
print('n=%d' % n)
print('m=%d' % m)

canvas = imagemagic.make_canvas(img)
N = len(canvas)
print('%dx%d canvas' %(N, N))
print('N=%d' % N)
# plt.imshow(canvas)
# plt.show()

tcanvas = [[[255, 255, 255] for i in range(N)] for j in range(N)]
for row in range(int(n/2), int(N-n/2)):
    for col in range(int(m/2), int(N-m/2)):
        [x, y] = imagemagic.get_xy(col, row, N)
        [x, y] = imagemagic.rot90(x, y)
        [i, j] = imagemagic.get_ij(x, y, N)
        tcanvas[j][i] = canvas[row][col]

plt.imshow(tcanvas)
plt.show()