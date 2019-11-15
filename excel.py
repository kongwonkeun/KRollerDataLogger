#
#
#

import os
import sys
import time

from PySide2.QtCore import QThread
from PySide2.QtCore import Signal
from PySide2.QtCore import Slot

import xlwt
import xlrd
import win32com.client

EXCEL_FILE  = 'log.xls'
EXCEL_SHEET = 'log'

#================================
#
#
class ExcelThread(QThread):

    def __init__(self, file):
        super(ExcelThread, self).__init__()
        self.file = file
        return

    def run(self):
        os.system('start excel.exe "%s\\%s"' % (sys.path[0], self.file))
        return

#================================
#
#
class Excel(object):

    def __init__(self):
        self.line = 1
        self.start = 'A'
        self.end = 'C'
        return

    def open(self, file):
        #---- thread ----
        self.thread = ExcelThread(file)
        self.thread.start(QThread.IdlePriority)
        time.sleep(5)
        return

    def connect(self):
        self.excelApp = win32com.client.GetActiveObject('Excel.Application')
        self.excelApp.Visible = True
        return

    def write(self, record):
        range = self.start + str(self.line) + ':' + self.end + str(self.line)
        self.excelApp.Range(range).Value = record
        self.line += 1
        return

    def skip(self, line):
        self.line += line
        return

    def test(self):
        #---- write ----
        self.xfile = xlwt.Workbook()
        self.sheet = self.xfile.add_sheet(EXCEL_SHEET)
        self.sheet.write(0, 0, 'it is a read-write test with excel file')
        self.xfile.save(EXCEL_FILE)
        #---- read ----
        self.x = xlrd.open_workbook(EXCEL_FILE)
        self.s = self.x.sheet_by_index(0)
        print(self.s.cell_value(0, 0))
        return

    def hi(self):
        print('---- someone calls me ----')
        return

#
# eof
#
