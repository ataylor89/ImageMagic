import imagemagic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

FILENAME = 'stacksofwheat.jpg'

img = imagemagic.reflecty(FILENAME)
plt.axis("off")
plt.imshow(img)
# plt.savefig('reflecty.jpg')
plt.show()