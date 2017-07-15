import sys
import time
import requests
import pickle
import pyperclip
import collections
from PySide import QtGui, QtCore
from PySide.QtCore import Qt

from settingsdialog import SettingsDialog
from aboutdialog import AboutDialog
from views.ui_mainwindow import Ui_MainWindow
from . import __appname__, __organization__

def run():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

class ClipThread(QtCore.QObject):
    copied = QtCore.Signal(str)

    def __init__(self, MainWindow, parent=None):
        super(ClipThread, self).__init__(parent)
        self.window = MainWindow
        pyperclip.copy('')
        self.last_clipboard = ''
        self.active = True

    def process(self):
        while self.active:
            tmp_val = pyperclip.paste()
            if tmp_val != self.last_clipboard:
                self.last_clipboard = tmp_val
                self.copied.emit(tmp_val)
            time.sleep(0.1)

class QSortableTableWidgetItem (QtGui.QTableWidgetItem):
    def __init__(self, value):
        super(QSortableTableWidgetItem, self).__init__("%s" % value)

    def __lt__(self, other):
        if (isinstance(other, QSortableTableWidgetItem)):
            selfVal = float(self.text().replace(",", ""))
            otherVal = float(other.text().replace(",", ""))
            # selfDataValue = float(self.data(Qt.EditRole).toString().replace(",", ""))
            # otherDataValue = float(other.data(Qt.EditRole).toString().replace(",", ""))
            return selfVal < otherVal
        else:
            return QtGui.QTableWidgetItem.__lt__(self, other)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        qfile = QtCore.QFile(":css/app.css")
        if qfile.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
             content = str(qfile.readAll())
        qfile.close()
        self.setStyleSheet(content)
        self.ui.setupUi(self)
        self.overlay = False

        self.settings = QtCore.QSettings(QtCore.QSettings.IniFormat,
                                         QtCore.QSettings.UserScope,
                                         __organization__,
                                         __appname__)
        self.readSettings()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Qty', 'Item', 'Value'])
        self.ui.tableWidget.setFixedWidth(442)
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 280)
        self.ui.tableWidget.setColumnWidth(2, 110)

        icon = QtGui.QIcon(QtGui.QPixmap(":img/question-mark.png"))
        self.ui.btn_about.setIcon(icon)
        icon = QtGui.QIcon(QtGui.QPixmap(":img/settings.png"))
        self.ui.btn_settings.setIcon(icon)

        QtGui.QShortcut(QtGui.QKeySequence(Qt.Key_O), self, self.toggleOverlayMode)
        QtGui.QShortcut(QtGui.QKeySequence(Qt.Key_S), self, self.settingsDialog)
        self.ui.btn_settings.clicked.connect(self.settingsDialog)
        self.ui.btn_about.clicked.connect(self.aboutDialog)

        self.startClipboard()

    def readSettings(self):
        self.settings.beginGroup("MainWindow")

        geometry              = self.settings.value("geometry")
        if geometry:
            self.restoreGeometry(geometry)

        self.settings_value_table  = self.settings.value("value_table") or collections.OrderedDict()
        self.settings_volume_table = self.settings.value("volume_table") or collections.OrderedDict()
        self.settings_show_table   = True if self.settings.value("show_table", "true") == "true" else False
        self.setShowTable(self.settings_show_table)
        self.settings_abbreviate   = True if self.settings.value("abbreviate", "true") == "true" else False
        self.settings_opacity      = self.settings.value("opacity", 20)

        self.settings.endGroup()

    def saveSettings(self):
        self.settings.beginGroup("MainWindow")

        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("value_table", self.settings_value_table)
        self.settings.setValue("volume_table", self.settings_volume_table)
        self.settings.setValue("show_table", self.settings_show_table)
        self.settings.setValue("abbreviate", self.settings_abbreviate)
        self.settings.setValue("opacity", self.settings_opacity)

        self.settings.endGroup()

    def setShowTable(self, state):
        self.ui.tableWidget.setVisible(state)
        if state:
            self.setMinimumSize(460, 200)
            self.setMaximumSize(460, 400)
        else:
            self.setFixedSize(460, 34)

    def openDialog(self, dialog):
        if self.overlay:
            self.toggleOverlayMode()
            QtCore.QTimer.singleShot(100, lambda: self.openDialog(dialog))
        else:
            dialog.exec_()

    def settingsDialog(self):
        self.openDialog(SettingsDialog(self))

    def aboutDialog(self):
        self.openDialog(AboutDialog(self))

    def closeEvent(self, event):
        # Terminate clipboard thread safely
        self.clipThread.active = False
        self.clipboard_thread.terminate()
        self.clipboard_thread.wait()
        self.saveSettings()
        event.accept()

    def toggleOverlayMode(self):
        self.overlay = not self.overlay

        flags = self.windowFlags()

        if (self.overlay):
            self.geometry = self.saveGeometry()
            self.setWindowOpacity(int(self.settings_opacity) / 100.0)
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
            self.ui.centralWidget.setAutoFillBackground(False)
            self.ui.tableWidget.setAutoFillBackground(False)
        else:
            self.setWindowOpacity(1.0)
            flags = flags ^ Qt.FramelessWindowHint ^ Qt.WindowStaysOnTopHint
            self.setWindowFlags(flags)
            self.ui.centralWidget.setAutoFillBackground(True)
            self.ui.tableWidget.setAutoFillBackground(True)
            self.setFocus()

        self.restoreGeometry(self.geometry)

        self.show()
        self.repaint()
        return 0

    def startClipboard(self):
        print("starting clipboard")
        self.clipboard_thread = QtCore.QThread()
        self.clipThread = ClipThread(self)
        self.clipThread.moveToThread(self.clipboard_thread)
        self.clipboard_thread.started.connect(self.clipThread.process)
        self.clipThread.copied.connect(self.handleClipboard)
        self.clipboard_thread.start()

    def handleClipboard(self, raw_text):
        body = self.getEvepraisal(raw_text)
        if body:
            self.updateTable(body['items'])
            value  = float(body['totals']['sell'])
            rawValue = value
            volume = float(body['totals']['volume'])

            valString = ""
            volString = ""

            valueLabel  = self.ui.totalLabel
            volumeLabel = self.ui.volumeLabel

            if self.settings_abbreviate:
                mag = ""
                if value > 1000000000:
                    mag = "Billion"
                    value = value / 1000000000.0
                elif value > 1000000:
                    mag = "Million"
                    value = value / 1000000.0
                elif value > 1000:
                    mag = "Thousand"
                    value = value / 1000.0

                valString = "Total: {:.2f} {}".format(value, mag)
                volString = "Volume: {:,} m3".format(volume)
            else:
                valString = "Total: {:,}".format(value)
                volString = "Volume: {:,} m3".format(volume)

            valueLabel.setText(valString)
            valueLabel.setStyleSheet("color: #000;")
            volumeLabel.setText(volString)
            volumeLabel.setStyleSheet("color: #000;")

            for total, color in self.settings_value_table.items():
                if rawValue >= total:
                    valueLabel.setStyleSheet("color: {}".format(color))

            for total, color in self.settings_volume_table.items():
                if volume >= total:
                    volumeLabel.setStyleSheet("color: {}".format(color))

    def updateTable(self, items):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(items))
        self.ui.tableWidget.setSortingEnabled(False)
        font = QtGui.QFont("Segoe", 7)
        for i in range(len(items)):
            item = items[i]
            qty_item  = QSortableTableWidgetItem("{:,}".format(item['quantity']))
            item_item = QtGui.QTableWidgetItem(item['name'])
            val_item  = QSortableTableWidgetItem("{:,.2f}".format(item['prices']['sell']['min'] * item['quantity']))
            qty_item.setFont(font)
            item_item.setFont(font)
            val_item.setFont(font)
            self.ui.tableWidget.setItem(i, 0, qty_item)
            self.ui.tableWidget.setItem(i, 1, item_item)
            self.ui.tableWidget.setItem(i, 2, val_item)
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.sortItems(2, Qt.DescendingOrder)


    def getEvepraisal(self, raw_text):
        r = requests.post('http://evepraisal.com/appraisal', data={'market': 'jita', 'raw_textarea': raw_text})
        if r.status_code == 200:
            paste_id = r.headers['X-Appraisal-Id']
            r = requests.get('http://evepraisal.com/a/{}.json'.format(paste_id))
            if r.status_code == 200:
                return r.json()
        return None