import imagemagic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

FILENAME = 'stacksofwheat.jpg'

# imagemagic.rot_img(FILENAME, math.pi/2)
img = imagemagic.reflecty(FILENAME)
plt.imshow(img)
plt.show()