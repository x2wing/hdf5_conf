#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication, QPushButton, QFileDialog)
from PyQt5 import QtCore


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.lbl = QLabel("Ubuntu", self)

        self.combo = QComboBox(self)
        # data = {'file_paths': [r'e:\temp\README.txt', r'e:\профиль\t.hdf5', r'e:\профиль\тест.hdf5']}
        # self.combo.addItems(data['file_paths'])
        self.combo.setGeometry(0, 0, 200, 50)
        btn_save = QPushButton("Save", self)
        btn_save.setGeometry(0, 60, 60, 30)
        btn_save.clicked[bool].connect(self.save_file)

        btn_load = QPushButton("Load", self)
        btn_load.setGeometry(70, 60, 60, 30)
        btn_load.clicked[bool].connect(self.load_file)

        # self.save_file()

        # self.combo.move(50, 50)
        self.lbl.setGeometry(80, 80, 50, 150)

        self.combo.activated[int].connect(self.selectionchange)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('QComboBox')
        self.setWindowFlags(QtCore.Qt.Widget|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.show()

    def save_file(self):
        description = 'Таблица hdf5'
        default_path = r'e:\temp'
        filter = "Таблицы hdf5  (*.hdf5)"
        dialog = QFileDialog.getSaveFileName(self, description, default_path, filter)
        self.combo.addItem(dialog[0])

    def load_file(self):
        pass

    def set_item(self, pressed):
        self.combo.addItem('fucking code')

    def on_activated(self, text):
        self.lbl.setText(text + 'tail')
        self.lbl.adjustSize()

    def selectionchange(self, i):
        print("Items in the list are :")
        for count in range(self.combo.count()):
            print(self.combo.itemText(count))
        print("Current index", i, "selection changed ", self.combo.currentText())
        self.combo.addItem('DSL Linux')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
