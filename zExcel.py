#
#
#

import os
import sys
import time

from PySide2.QtCore import QThread
from PySide2.QtCore import Signal
from PySide2.QtCore import Slot

import win32com.client

EXCEL_FILE  = "log.xls"
EXCEL_SHEET = "log"

#================================
#
#
class Excel(object):

    def __init__(self):
        self.line = 4
        self.start = 'A'
        self.end = 'F'
        return

    def open(self, file):
        self.excelApp = win32com.client.Dispatch("Excel.Application")
        self.excelApp.Visible = True
        self.excelApp.Workbooks.Open(file)
        return

    def connect(self):
        return

    def write_header(self):
        r1 = 'A1:K1'
        d1 = ('날짜','시간','분','초','속도','좌우','최대','최소','폭','이동거리','경과시간')
        r2 = 'A2:K2'
        d2 = ('*','*','*','*','cm/sec','cm','cm','cm','cm','m','초')
        self.excelApp.Range(r1).Value = d1
        self.excelApp.Range(r2).Value = d2
        return

    def write_summery(self, record):
        r = 'G3:K3'
        self.excelApp.Range(r).Value = record
        return

    def write(self, record):
        range = 'A3:F3'
        self.excelApp.Range(range).Value = record
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
        self.sheet.write(0, 0, "it is a read-write test with excel file")
        self.xfile.save(EXCEL_FILE)
        #---- read ----
        self.x = xlrd.open_workbook(EXCEL_FILE)
        self.s = self.x.sheet_by_index(0)
        print(self.s.cell_value(0, 0))
        return

#
# eof
#
