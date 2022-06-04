import imagemagic
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

FILENAME = 'stacksofwheat.jpg'

def show_img():
    img = mpimg.imread(FILENAME)
    plt.imshow(img)
    plt.show()

def rot_img():
    canvas = imagemagic.rot_img_90(FILENAME)
    plt.imshow(canvas)
    plt.show()

if __name__ == "__main__":
    rot_img()