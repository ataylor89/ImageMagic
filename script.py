import imagemagic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

FILENAME = 'stacksofwheat.jpg'

img = imagemagic.reflecty(FILENAME)
# img = imagemagic.rotate(FILENAME, math.pi/4)
plt.axis("off")
plt.imshow(img)
plt.savefig('transformations/reflecty.jpg')
plt.show()