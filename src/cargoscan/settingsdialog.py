import collections

from PySide import QtGui, QtCore

from views.ui_settingswindow import Ui_SettingsWindow


class SettingsDialog(QtGui.QDialog, Ui_SettingsWindow):
    def __init__(self, MainWindow, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.main_window = MainWindow

        self.ui.checkbox_items_table.setChecked(self.main_window.settings_show_table)
        self.ui.checkbox_abbreviate_value.setChecked(self.main_window.settings_abbreviate)
        self.ui.slider_opacity.setValue(int(self.main_window.settings_opacity))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ui.tabWidget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.settings_ok_button.clicked.connect(self.close)


        icon = QtGui.QIcon(QtGui.QPixmap(":img/add-icon.png"))
        for btn in (self.ui.btn_value_add, self.ui.btn_volume_add):
            btn.setIcon(icon)
            btn.setFlat(True)
            btn.setAutoFillBackground(True)
            btn.setStyleSheet("background: transparent")
            btn.setCursor(QtCore.Qt.PointingHandCursor)

        self.ui.valueTableWidget.cellClicked.connect(self.valueCellClicked)
        self.ui.volumeTableWidget.cellClicked.connect(self.volumeCellClicked)
        self.ui.btn_value_add.clicked.connect(lambda: self.addTableRow(self.ui.valueTableWidget))
        self.ui.btn_volume_add.clicked.connect(lambda: self.addTableRow(self.ui.volumeTableWidget))

        for tableWidget in self.ui.colors_tab.findChildren(QtGui.QTableWidget):
            tableWidget.setColumnCount(3)
            tableWidget.setColumnWidth(0, 100)
            tableWidget.setColumnWidth(1, 78)
            tableWidget.setColumnWidth(2, 25)
            tableWidget.verticalHeader().setDefaultSectionSize(25)
            tableWidget.setRowCount(0)
            tableWidget.setSortingEnabled(False)
            tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        for total, color in self.main_window.settings_value_table.items():
            self.addTableRow(self.ui.valueTableWidget, total, color)
        for total, color in self.main_window.settings_volume_table.items():
            self.addTableRow(self.ui.volumeTableWidget, total, color)

    def addTableRow(self, table, value=None, color=None):
        pushButton = QtGui.QPushButton()
        pushButton.setMinimumSize(QtCore.QSize(25, 25))
        pushButton.setMaximumSize(QtCore.QSize(25, 25))
        pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        pushButton.setAutoFillBackground(True)
        pushButton.setFlat(True)
        pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(":img/delete-icon.png")))
        pushButton.setStyleSheet("background-color: transparent;")
        pushButton.clicked.connect(lambda: self.removeTableRow(pushButton, table))

        widget = QtGui.QWidget()
        widget.setMinimumSize(QtCore.QSize(75, 0))
        widget.setMaximumSize(QtCore.QSize(75, 25))
        widget.setAutoFillBackground(True)
        palette = widget.palette()
        palette.setColor(QtGui.QPalette.Window, QtCore.Qt.red)
        widget.setPalette(palette)

        lineEdit = QtGui.QLineEdit()
        lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        lineEdit.setMaximumSize(QtCore.QSize(100, 25))

        if value:
            lineEdit.setText(str(value))

        row = table.rowCount()
        table.setRowCount(table.rowCount()+1)
        table.setCellWidget(row, 0, lineEdit)

        item = QtGui.QTableWidgetItem("Set Color")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        if color:
            item.setBackground(QtGui.QColor(color))
        table.setItem(row, 1, item)

        table.setCellWidget(row, 2, pushButton)

    def removeTableRow(self, button, table):
        for i in range(table.rowCount()):
            widget = table.cellWidget(i, 2)
            if widget == button:
                table.removeRow(i)

    def getTableValues(self, table):
        info = {}
        for row in range(table.rowCount()):
            lineEdit = table.cellWidget(row, 0)
            try:
                val = int(lineEdit.text())
            except ValueError:
                val = 0

            colorCell = table.item(row, 1)
            info[val] = str(colorCell.background().color().name())
        return collections.OrderedDict(sorted(info.items()))

    def closeEvent(self, event):
        self.saveSettings()
        event.accept()

    def valueCellClicked(self, row, col):
        self.cellClicked(row, col, self.ui.valueTableWidget)

    def volumeCellClicked(self, row, col):
        self.cellClicked(row, col, self.ui.volumeTableWidget)

    def cellClicked(self, row, col, table):
        if col == 1:
            color = QtGui.QColorDialog.getColor(QtCore.Qt.white, self, "Select Warning Color")
            item = table.item(row, col)
            item.setBackground(color)
            item.setSelected(False)

    def test(self, button, tableWidget):
        for i in range(tableWidget.rowCount()):
            for j in range(tableWidget.columnCount()):
                widget = tableWidget.cellWidget(i,j)

    def saveSettings(self):
        print('Writing savings to main window')
        self.main_window.settings_show_table  = self.ui.checkbox_items_table.isChecked()
        self.main_window.settings_abbreviate  = self.ui.checkbox_abbreviate_value.isChecked()
        self.main_window.settings_opacity     = self.ui.spinbox_opacity.value()
        self.main_window.settings_value_table = self.getTableValues(self.ui.valueTableWidget)
        self.main_window.settings_volume_table = self.getTableValues(self.ui.volumeTableWidget)
        self.main_window.saveSettings()
        self.main_window.setShowTable(self.main_window.settings_show_table)

# QtGui.QGridLayout(SettingsWindow)
class ColorLayout(QtGui.QGridLayout):
    def __init__(self, SettingsDialog, parent=None):
        super(ColorLayout, self).__init__(parent)
