import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from MVC import controller
from MVC.gui import GUI
from MVC.model import Model
from MVC import stylesheet

BASE_DIR = os.path.dirname(__file__)

try:
    from ctypes import windll
    myappid = 'com.kmilewdev.photomod.v1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon(os.path.join(BASE_DIR, 'resources', 'icons', 'main.ico')))
    app.setStyleSheet(stylesheet.get_stylesheet())
    model = Model()
    gui = GUI()
    gui.show()
    controller = controller.Controller(model=model, view=gui)
    sys.exit(app.exec())