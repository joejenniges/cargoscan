# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\mainwindow.ui'
#
# Created: Thu Jul 13 19:04:37 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 400)
        MainWindow.setMinimumSize(QtCore.QSize(460, 400))
        MainWindow.setMaximumSize(QtCore.QSize(460, 400))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(460, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.tableWidget.setStyleSheet("background-color: red")
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.totalLabel = QtGui.QLabel(self.centralWidget)
        self.totalLabel.setObjectName("totalLabel")
        self.gridLayout.addWidget(self.totalLabel, 0, 0, 1, 1)
        self.volumeLabel = QtGui.QLabel(self.centralWidget)
        self.volumeLabel.setObjectName("volumeLabel")
        self.gridLayout.addWidget(self.volumeLabel, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CargoScan", None, QtGui.QApplication.UnicodeUTF8))
        self.totalLabel.setText(QtGui.QApplication.translate("MainWindow", "Total:", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeLabel.setText(QtGui.QApplication.translate("MainWindow", "Volume:", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc 
