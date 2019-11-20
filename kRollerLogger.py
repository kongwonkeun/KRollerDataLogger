#
#
#

import sys
import signal
import os
import msvcrt
import time

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication

import zGui
import zUi
import zExcel
import zBt

G_bt = zBt.Bt()
G_excel = zExcel.Excel()

#================================
#
#
if  __name__ == '__main__':

    print("hello world")

    G_excel.open(os.getcwd() + "\\log.xls")
    G_bt.connect_excel(G_excel)
    G_bt.connect()

    #---- wait ---- for quit command
    while True:
        time.sleep(1)
        G_bt.tick()
        if  msvcrt.kbhit():
            c = msvcrt.getch()
            if  c == b'q':
                G_bt.stop()
                break
    sys.exit(0)
    #----

    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    rect = screen.availableGeometry()

    r = -1
    with ui.UiWindow(G_bt) as w:
        t = QTimer()
        t.setSingleShot(True)
        t.timeout.connect(w.showFullScreen)
        t.start(1000)
        w.setGeometry(rect)
        w.show()
        r = app.exec_()
        print("bye")

    sys.exit(r)

#
# eof
#
