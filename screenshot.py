import pyscreenshot as ImageGrab

def screen(imageTitle):
    im = ImageGrab.grab()
    save(im, imageTitle)


def selection(imageTitle):
    bbox = None
    im = ImageGrab.grab(bbox = bbox)
    save(im, imageTitle)


def save(image, title):
    image.save(title)
    print("screenshot saved")