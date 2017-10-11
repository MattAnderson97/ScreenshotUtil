import pyscreenshot as ImageGrab

def screen(imageTitle):
    im = ImageGrab.grab()
    save(im)


def selection(imageTitle):
    bbox = None
    im = ImageGrab.grab(bbox = bbox)
    save(im)


def save(image):
    image.save()
    print("screenshot saved")