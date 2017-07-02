import sys
import time
import StringIO
import requests

from PySide import QtGui, QtCore
from PySide.QtGui import QApplication, QMessageBox
import pyperclip

from views.ui_mainwindow import Ui_MainWindow

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
                # self.window.handleClipboard(tmp_val)
            time.sleep(0.1)

class QCustomTableWidgetItem (QtGui.QTableWidgetItem):
    def __init__(self, value):
        super(QCustomTableWidgetItem, self).__init__("%s" % value)

    def __lt__(self, other):
        if (isinstance(other, QCustomTableWidgetItem)):
            selfVal = float(self.text().replace(",", ""))
            otherVal = float(other.text().replace(",", ""))
            # selfDataValue = float(self.data(QtCore.Qt.EditRole).toString().replace(",", ""))
            # otherDataValue = float(other.data(QtCore.Qt.EditRole).toString().replace(",", ""))
            return selfVal < otherVal
        else:
            return QtGui.QTableWidgetItem.__lt__(self, other)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Qty', 'Item', 'Value'])
        self.ui.tableWidget.setFixedWidth(640)
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 400)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.startClipboard()

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
            self.ui.totalLabel.setText("Total: {:,} ISK".format(body['totals']['sell']))
            self.ui.volumeLabel.setText("Volume: {:,} m3".format(body['totals']['volume']))

    def updateTable(self, items):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(items))
        self.ui.tableWidget.setSortingEnabled(False)
        for i in range(len(items)):
            item = items[i]
            qty_item  = QCustomTableWidgetItem("{:,}".format(item['quantity']))
            item_item = QtGui.QTableWidgetItem(item['name'])
            val_item  = QCustomTableWidgetItem("{:,.2f}".format(item['prices']['sell']['min'] * item['quantity']))
            self.ui.tableWidget.setItem(i, 0, qty_item)
            self.ui.tableWidget.setItem(i, 1, item_item)
            self.ui.tableWidget.setItem(i, 2, val_item)
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.sortItems(2, QtCore.Qt.DescendingOrder)


    def getEvepraisal(self, raw_text):
        r = requests.post('http://evepraisal.com/appraisal', data={'market': 'jita', 'raw_textarea': raw_text})
        print(raw_text)
        if r.status_code == 200:
            paste_id = r.headers['X-Appraisal-Id']
            r = requests.get('http://evepraisal.com/a/{}.json'.format(paste_id))
            if r.status_code == 200:
                return r.json()
        return None