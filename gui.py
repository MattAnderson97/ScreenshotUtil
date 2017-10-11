from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from win32gui import PumpMessages

import sys

from watcher import Watcher


class KeyPressThread(QThread):
    def run(self):
        watcher = Watcher()
        PumpMessages()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main window")

        self.central_widget = QWidget()
        self.btn = QPushButton("Hello")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.btn)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.keyWatcher = KeyPressThread()
        self.keyWatcher.start()
        # self.watcher.run()

        self.btn.clicked.connect(lambda: print("hello world"))
        # self.btnExit.clicked.connect(self.close)
        # self.actionExit.triggered.connect(self.close)

    def closeEvent(self, event):
        print("event")
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.keyWatcher.terminate()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()