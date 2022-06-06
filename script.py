import imagemagic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

FILENAME = 'stacksofwheat.jpg'
# img = mpimg.imread(FILENAME)
# img = imagemagic.rotate(FILENAME, 2*math.pi)
img = imagemagic.reflectx(FILENAME)
# img = imagemagic.reflecty(FILENAME)
plt.imshow(img)
plt.show()