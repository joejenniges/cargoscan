
C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe resources\ui\resources.qrc -o src\cargoscan\views\resources_rc.py
C:\Python27\Scripts\pyside-uic resources\ui\mainwindow.ui -o src\cargoscan\views\ui_mainwindow.py
C:\Python27\Scripts\pyside-uic resources\ui\settingswindow.ui -o src\cargoscan\views\ui_settingswindow.py
C:\Python27\Scripts\pyside-uic resources\ui\aboutwindow.ui -o src\cargoscan\views\ui_aboutwindow.py
echo import resources_rc >> src\cargoscan\views\ui_mainwindow.py