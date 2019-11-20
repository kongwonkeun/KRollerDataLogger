# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui',
# licensing of 'gui.ui' applies.
#
# Created: Tue Oct  1 15:56:23 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

#================================
#
#
class Ui_Form(object):

    def __init__(self):
        self.start_time = 0
        self.current_time = 0
        self.min = 0
        self.max = 0
        self.width = 0
        self.center = 0
        self.rotation_per_sec = 0
        self.meter_per_sec = 0
        self.rotation_per_min = 0
        self.distance_per_min = 0
        self.wheel_rotation_per_min = 0
        self.cadence = 0
        self.sum_of_rotation = 0
        self.sum_of_distance = 0
        self.kilometer_per_hour = 0
        self.roller_diameter = 0
        self.wheel_diameter = 0
        self.W_ratio = 0.0
        self.W_not_set = True
        self.chain_ring_T = 0
        self.sprocket_T = 0
        self.T_ratio = 0.0
        self.T_not_set = True
        return

    def changedTW3(self, row, col):
        if  row == 1 and col == 0:
            t = self.tableWidget_3.item(row, col).text()
            self.roller_diameter = int(t)
            self.W_not_set = True

        if  row == 1 and col == 1:
            t = self.tableWidget_3.item(row, col).text()
            self.wheel_diameter = int(t)
            self.W_not_set = True

        if  self.wheel_diameter != 0 and self.roller_diameter != 0 and self.W_not_set:
            self.W_not_set = False
            self.W_ratio = self.roller_diameter / self.wheel_diameter
            item = QtWidgets.QTableWidgetItem()
            item.setText(format(self.W_ratio, '.2f'))
            self.tableWidget_3.setItem(1, 2, item)
        return

    def changedTW4(self, row, col):
        if  row == 1 and col == 0:
            t = self.tableWidget_4.item(row, col).text()
            self.chain_ring_T = int(t)
            self.T_not_set = True

        if  row == 1 and col == 1:
            t = self.tableWidget_4.item(row, col).text()
            self.sprocket_T = int(t)
            self.T_not_set = True

        if  self.chain_ring_T != 0 and self.sprocket_T != 0 and self.T_not_set:
            self.T_not_set = False
            self.T_ratio = self.chain_ring_T / self.sprocket_T
            item = QtWidgets.QTableWidgetItem()
            item.setText(format(self.T_ratio, '.2f'))
            self.tableWidget_4.setItem(1, 2, item)
        return

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 768)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(21, 260, 56, 16))
        self.label_4.setObjectName("label_4")

        self.tableWidget_3 = QtWidgets.QTableWidget(Form)
        self.tableWidget_3.setGeometry(QtCore.QRect(630, 280, 500, 121))
        self.tableWidget_3.setRowCount(3)
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 2, item)

        self.tableWidget_3.cellChanged.connect(self.changedTW3)

        self.tableWidget_4 = QtWidgets.QTableWidget(Form)
        self.tableWidget_4.setGeometry(QtCore.QRect(630, 410, 500, 121))
        self.tableWidget_4.setRowCount(3)
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 2, item)

        self.tableWidget_4.cellChanged.connect(self.changedTW4)

        self.tableWidget_5 = QtWidgets.QTableWidget(Form)
        self.tableWidget_5.setGeometry(QtCore.QRect(630, 150, 500, 121))
        self.tableWidget_5.setRowCount(3)
        self.tableWidget_5.setColumnCount(3)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(3)
        self.tableWidget_5.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 2, item)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 650, 591, 16))
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 670, 591, 16))
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 570, 591, 16))
        self.label_7.setObjectName("label_7")
        
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 590, 591, 16))
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 610, 591, 16))
        self.label_9.setObjectName("label_9")
        
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 630, 591, 16))
        self.label_10.setObjectName("label_10")
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(21, 22, 56, 16))
        self.label.setObjectName("label")
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(21, 40, 591, 194))
        self.widget.setObjectName("widget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout.addWidget(self.label_2)
        
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(22, 279, 591, 281))
        self.widget1.setObjectName("widget1")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget1)
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 2, item)
        self.horizontalLayout_2.addWidget(self.tableWidget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.start_time = datetime.now()
        item = QtWidgets.QTableWidgetItem()
        item.setText(str(self.start_time))
        self.tableWidget_5.setItem(1, 0, item)
        return

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "회전운동", None, -1))

        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.item(0, 0).setText(QtWidgets.QApplication.translate("Form", "롤러직경(mm)", None, -1))
        self.tableWidget_3.item(0, 1).setText(QtWidgets.QApplication.translate("Form", "바퀴외경(mm)", None, -1))
        self.tableWidget_3.item(0, 2).setText(QtWidgets.QApplication.translate("Form", "회전비", None, -1))
        self.tableWidget_3.item(2, 0).setText(QtWidgets.QApplication.translate("Form", "R", None, -1))
        self.tableWidget_3.item(2, 1).setText(QtWidgets.QApplication.translate("Form", "W", None, -1))
        self.tableWidget_3.item(2, 2).setText(QtWidgets.QApplication.translate("Form", "R / W", None, -1))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.item(0, 0).setText(QtWidgets.QApplication.translate("Form", "체인링(T)", None, -1))
        self.tableWidget_4.item(0, 1).setText(QtWidgets.QApplication.translate("Form", "스프라켓(T)", None, -1))
        self.tableWidget_4.item(0, 2).setText(QtWidgets.QApplication.translate("Form", "기어비", None, -1))
        self.tableWidget_4.item(2, 0).setText(QtWidgets.QApplication.translate("Form", "C", None, -1))
        self.tableWidget_4.item(2, 1).setText(QtWidgets.QApplication.translate("Form", "S", None, -1))
        self.tableWidget_4.item(2, 2).setText(QtWidgets.QApplication.translate("Form", "C / S", None, -1))
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        self.tableWidget_5.item(0, 0).setText(QtWidgets.QApplication.translate("Form", "시작시간", None, -1))
        self.tableWidget_5.item(0, 1).setText(QtWidgets.QApplication.translate("Form", "현재시간", None, -1))
        self.tableWidget_5.item(0, 2).setText(QtWidgets.QApplication.translate("Form", "경과시간", None, -1))
        self.tableWidget_5.item(2, 0).setText(QtWidgets.QApplication.translate("Form", "S", None, -1))
        self.tableWidget_5.item(2, 1).setText(QtWidgets.QApplication.translate("Form", "C", None, -1))
        self.tableWidget_5.item(2, 2).setText(QtWidgets.QApplication.translate("Form", "S - C", None, -1))
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QtWidgets.QApplication.translate("Form", "분당바퀴회전수 = 분당회전수 X 회전비 또는 분당이동거리(m) X 1000 / 3.14 / 바퀴외경", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "케이던스 = 분당바퀴회전수 X 기어비", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "순간속도 = 초당회전수 X 롤러직경 X 3.14 / 1000 (m/sec)", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "분당이동거리 = 분당회전수 X 롤러직경 X 3.14 / 1000 (m/min)", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Form", "총이동거리 = 누적회전수 X 롤러직경 X 3.14 /1000 (m)", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "평균속도 = 총이동거리 / 1000 / 시간 (Km/h)", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "좌우이동", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p align=\"center\">클램프</p><p align=\"center\">좌우이동</p></body></html>", None, -1))
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.item(0, 0).setText(QtWidgets.QApplication.translate("Form", "최소값", None, -1))
        self.tableWidget.item(0, 1).setText(QtWidgets.QApplication.translate("Form", "최대값", None, -1))
        self.tableWidget.item(0, 2).setText(QtWidgets.QApplication.translate("Form", "좌우이동거리", None, -1))
        self.tableWidget.item(0, 3).setText(QtWidgets.QApplication.translate("Form", "중심값", None, -1))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p align=\"center\">롤러</p><p align=\"center\">회전운동</p></body></html>", None, -1))
        
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.item(0, 0).setText(QtWidgets.QApplication.translate("Form", "초당회전수", None, -1))
        self.tableWidget_2.item(0, 1).setText(QtWidgets.QApplication.translate("Form", "순간속도(초속)", None, -1))
        self.tableWidget_2.item(2, 0).setText(QtWidgets.QApplication.translate("Form", "분당회전수", None, -1))
        self.tableWidget_2.item(2, 1).setText(QtWidgets.QApplication.translate("Form", "분당이동거리", None, -1))
        self.tableWidget_2.item(2, 2).setText(QtWidgets.QApplication.translate("Form", "분당바퀴회전수", None, -1))
        self.tableWidget_2.item(2, 3).setText(QtWidgets.QApplication.translate("Form", "케이던스", None, -1))
        self.tableWidget_2.item(4, 0).setText(QtWidgets.QApplication.translate("Form", "누적회전수", None, -1))
        self.tableWidget_2.item(4, 1).setText(QtWidgets.QApplication.translate("Form", "총이동거리", None, -1))
        self.tableWidget_2.item(4, 2).setText(QtWidgets.QApplication.translate("Form", "평균속도(시속)", None, -1))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        return

#
# eof
#
