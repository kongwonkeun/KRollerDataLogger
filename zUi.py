#
#
#

import os
import time

from PySide2.QtCore import Qt
from PySide2.QtCore import QThread
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QWidget

import zGui
import zBt

#================================
#
#
class UiWindow(QMainWindow):

    def __init__(self, bt):
        super(UiWindow, self).__init__()

        self.widget = QWidget()
        self.gui = gui.Ui_Form();
        self.gui.setupUi(self.widget)

        self.setCentralWidget(self.widget)
        self.setWindowTitle("main window")

        self.bt = bt
        self.bt.connect_rx(self.rxHandler)
        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        if  exc_type or exc_val or exc_tb:
            pass
        return

    def rxHandler(self, rotation, dir):
        print("---- someone calls rxHandler ----")
        return

    def stop(self):
        return

#
# eof
#
