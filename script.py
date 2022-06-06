import imagemagic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

FILENAME = 'stacksofwheat.jpg'

# img = mpimg.imread(FILENAME)
# img = imagemagic.rotate(FILENAME, 3*math.pi/2)
img = imagemagic.reflecty(FILENAME)
# img = imagemagic.reflecty(FILENAME)
plt.axis("off")
plt.imshow(img)
# plt.savefig('reflecty.jpg')
plt.show()