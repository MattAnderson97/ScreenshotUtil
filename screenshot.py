import pyscreenshot as ImageGrab

def screen(imageTitle):
    im = ImageGrab.grab()
    im.save(imageTitle)
    print("screenshot saved")


def selection(imageTitle):
    bbox = None
    im = ImageGrab.grab(bbox = bbox)
    im.save(imageTitle)
    print("screenshot saved")
