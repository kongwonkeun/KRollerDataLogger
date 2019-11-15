#
#
#

import sys
import signal
import os

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication

import gui
import ui
import excel
import bt

G_bt = bt.Bt()
G_excel = excel.Excel()

#================================
#
#
if  __name__ == '__main__':

    print('hello world')

    G_excel.open('log.xls')
    G_excel.connect()
    G_excel.write((7,8,9,0)) #---- test ---- will be replace with table header
    G_bt.connect_excel(G_excel)
    G_bt.inquiry()

    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    rect = screen.availableGeometry()

    r = -1
    with ui.UiWindow(G_bt) as w:
        t = QTimer()
        t.setSingleShot(True)
        t.timeout.connect(w.showFullScreen)
        #t.start(1000)
        w.setGeometry(rect)
        w.show()
        r = app.exec_()
        print('bye')

    sys.exit(r)

#
# eof
#
