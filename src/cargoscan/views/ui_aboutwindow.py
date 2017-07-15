# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\aboutwindow.ui'
#
# Created: Sat Jul 15 12:57:35 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(392, 455)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setMaximumSize(QtCore.QSize(16777215, 455))
        AboutDialog.setWhatsThis("")
        self.gridLayout = QtGui.QGridLayout(AboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtGui.QPushButton(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.iconLabel = QtGui.QLabel(AboutDialog)
        self.iconLabel.setMinimumSize(QtCore.QSize(256, 256))
        self.iconLabel.setMaximumSize(QtCore.QSize(256, 256))
        self.iconLabel.setText("")
        self.iconLabel.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setObjectName("iconLabel")
        self.horizontalLayout.addWidget(self.iconLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label = QtGui.QLabel(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), AboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("AboutDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Created by Joe Jenniges</span></p><p><span style=\" font-size:12pt;\">Copyright 2017</span></p><p><span style=\" font-size:12pt;\">This program is free and open source and can be downloaded </span><a href=\"https://github.com/gunfighterj/cargoscan\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">here</span></a><span style=\" font-size:12pt;\">.</span></p><p><span style=\" font-size:10pt;\">Isk donations to GunfighterJ. Writing software is how he can afford the game!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

