import random
from string import ascii_letters, digits
from win32gui import PumpMessages, PostQuitMessage

from pyHook import HookManager, GetKeyState
from pyHook.HookManager import HookConstants

from src import screenshot


class Watcher(object):
    def __init__(self):
        self.hm = HookManager()
        self.hm.KeyDown = self.key_down_event
        self.hm.HookKeyboard()

    def key_down_event(self, event):
        try:
            if GetKeyState(HookConstants.VKeyToID('VK_SHIFT')) and GetKeyState(HookConstants.VKeyToID('VK_MENU')):
                if HookConstants.IDToName(event.KeyID) == "1":
                    print("screenshot!")
                    title = "".join(random.choice(ascii_letters + digits) for i in range(16))
                    screenshot.screen(title + ".png")
                elif HookConstants.IDToName(event.KeyID) == "2":
                    print("screenshot active window")
                elif HookConstants.IDToName(event.KeyID) == "3":
                    print("screenshot selection")
        except:
            pass
        finally:
            return True
    def shutdown(self):
        PostQuitMessage(0)
        self.hm.UnhookKeyboard()


if __name__ == "__main__":
    watcher = Watcher()
    PumpMessages()