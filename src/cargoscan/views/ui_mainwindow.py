# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\mainwindow.ui'
#
# Created: Sat Jul 15 12:57:34 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(460, 0))
        MainWindow.setMaximumSize(QtCore.QSize(460, 400))
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.totalLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalLabel.setFont(font)
        self.totalLabel.setObjectName("totalLabel")
        self.gridLayout.addWidget(self.totalLabel, 0, 0, 1, 1)
        self.volumeLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setObjectName("volumeLabel")
        self.gridLayout.addWidget(self.volumeLabel, 0, 1, 1, 1)
        self.btn_about = QtGui.QPushButton(self.centralWidget)
        self.btn_about.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_about.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_about.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_about.setAutoFillBackground(True)
        self.btn_about.setText("")
        self.btn_about.setFlat(True)
        self.btn_about.setObjectName("btn_about")
        self.gridLayout.addWidget(self.btn_about, 0, 2, 1, 1)
        self.btn_settings = QtGui.QPushButton(self.centralWidget)
        self.btn_settings.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_settings.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_settings.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_settings.setAutoFillBackground(True)
        self.btn_settings.setText("")
        self.btn_settings.setFlat(True)
        self.btn_settings.setObjectName("btn_settings")
        self.gridLayout.addWidget(self.btn_settings, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CargoScan", None, QtGui.QApplication.UnicodeUTF8))
        self.totalLabel.setText(QtGui.QApplication.translate("MainWindow", "Total:", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeLabel.setText(QtGui.QApplication.translate("MainWindow", "Volume:", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc 
