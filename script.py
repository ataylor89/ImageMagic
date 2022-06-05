import imagemagic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

FILENAME = 'stacksofwheat.jpg'

def show_img():
    img = mpimg.imread(FILENAME)
    plt.imshow(img)
    plt.show()

def rot_img(T):
    canvas = imagemagic.rot_img(FILENAME, T)
    plt.imshow(canvas)
    plt.show()

if __name__ == "__main__":
    rot_img(math.pi/2)
    # rot_img(math.pi)
    # rot_img(3*math.pi/2)
    # rot_img(math.pi/4)
    # rot_img(2*math.pi)
    # show_img()