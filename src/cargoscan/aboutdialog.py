from PySide import QtGui, QtCore

from views.ui_aboutwindow import Ui_AboutDialog


class AboutDialog(QtGui.QDialog, Ui_AboutDialog):
    def __init__(self, MainWindow, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        pixmap = QtGui.QPixmap(":img/logo.png")
        self.ui.iconLabel.setPixmap(pixmap.scaled(256, 256, QtCore.Qt.KeepAspectRatio))
