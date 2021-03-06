#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import numpy as np
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication, QPushButton, QFileDialog)
from PyQt5 import QtCore

from iof import Save, Load

class Mysignal(QtCore.QObject):
    mysignal = QtCore.pyqtSignal()



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.data = np.random.randint(1,10, (5,5))
        print(self.data)
        print(os.path.dirname(os.path.abspath(__file__)))

        self.mysignal = Mysignal()

        self.lbl = QLabel("Ubuntu", self)

        self.combo = QComboBox(self)
        # data = {'file_paths': [r'e:\temp\README.txt', r'e:\профиль\t.hdf5', r'e:\профиль\тест.hdf5']}
        # self.combo.addItems(data['file_paths'])
        self.combo.setGeometry(0, 0, 200, 50)
        self.btn_save = QPushButton("Save", self)
        self.btn_save.setGeometry(0, 60, 60, 30)
        self.btn_save.clicked[bool].connect(self.save_file)

        btn_load = QPushButton("Load", self)
        btn_load.setGeometry(70, 60, 60, 30)
        # btn_load.clicked[bool].connect(self.load_file)
        btn_load.clicked.connect(self.btn_save.click)


        self.mysignal.mysignal.connect(self.save_file)
        # self.save_file()

        # self.combo.move(50, 50)
        self.lbl.setGeometry(80, 80, 50, 150)

        self.combo.activated[int].connect(self.selectionchange)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('QComboBox')
        self.setWindowFlags(QtCore.Qt.Widget|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.show()

    def get_save_filepath(self):
        description = 'Сохранить hdf5'
        default_path = os.path.dirname(os.path.abspath(__file__))
        filter = "Таблицы hdf5  (*.hdf5)"
        path, _ = QFileDialog.getSaveFileName(self, description, default_path, filter)
        print(path)
        return path

    def save_file(self):
        path = self.get_save_filepath()
        self.combo.addItem(path)
        if path:
            Save()(self.data, filepath=path)

    def load_file(self):
        self.mysignal.mysignal.emit()

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
