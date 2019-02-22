import tkinter
from PIL import Image, ImageTk
from functools import lru_cache

@lru_cache(maxsize=32) #set maxsize to None for unlimited cacheing
def fetch_image(name):
    """Get image from IMAGES dictionary. Up to 32 Images are cached to speed second load.

    :param name: string image file name
    :return: PIL.Image
    """
    return Image.open('C:/Users/himanshu/Desktop/Django/Bootstrap_Project/images/{}.png'.format(name))
class Window(object):
    def __init__(self, image):
        self.root = tkinter.Tk()
        self.make_image(image)
    def make_image(self, name):
        self.image = ImageTk.PhotoImage(fetch_image(name)) #you must keep a reference to the PhotoImage in self!
        pic = tkinter.Label(self.root, image=self.image)
        pic.pack()

if __name__ == "__main__":
    black = Window(image='career1')
    black.root.mainloop()
    white = Window(image='career2')
    white.root.mainloop()
    black_again = Window(image='career3')
    black_again.root.mainloop()