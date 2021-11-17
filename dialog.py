import sqlite3, shelve, os
from os import path
from PyQt5 import QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from dial import Ui_Dialog


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        con = sqlite3.connect('books.db')
        self.ok1, self.ok2 = True, True
        self.cur = con.cursor()
        self.setupUi(self)
        self.key.textChanged.connect(self.check)
        self.close_button.clicked.connect(self.cls)
        self.name.textChanged.connect(self.name_check)
        self.img_but.clicked.connect(self.img_search)
        self.desc_but.clicked.connect(self.desc_search)
        self.confirm.clicked.connect(self.confirm_click)

    def check(self):
        lis = list(map(lambda x: x[0], self.cur.execute('''SELECT genre FROM Library''').fetchall()))
        if self.key.text().lower() in lis:
            mes = QMessageBox()
            mes.setWindowTitle('Warning')
            mes.setText('Данный ключ уже существует')
            mes.exec()
            self.ok1 = False
        self.ok1 = True

    def name_check(self):
        lis = list(map(lambda x: x[0], self.cur.execute('''SELECT name FROM Library''').fetchall()))
        if self.name.text() in lis:
            mes = QMessageBox()
            mes.setWindowTitle('Warning')
            mes.setText('Данная книга уже в БД')
            mes.exec()
            self.ok2 = False
        self.ok2 = True

    def img_search(self):
        self.file_img = QFileDialog.getOpenFileName(self, 'Выбрать изображение', '', '*.jpg')[0]
        self.img.setText(QFileInfo(self.file_img).fileName())

    def desc_search(self):
        self.file_desc = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', '*.txt')[0]
        self.desc.setText(QFileInfo(self.file_desc).fileName())

    def confirm_click(self):
        con = sqlite3.connect('books.db')
        cur = con.cursor()
        p_desc = os.path.abspath('descrip')
        p_imag = os.path.abspath('images')
        if self.ok1 and self.ok2:
            key = self.key.text()
            source_path_img, n_i = self.file_img, f'{key}.jpg'
            source_path_desc, n_d = self.file_desc, f'{key}.txt'
            if path.exists(source_path_img) and path.exists(source_path_desc):
                os.rename(self.file_img, f'{p_imag}/{key}.jpg')
                os.rename(self.file_desc, f'{p_desc}/{key}.txt')
                cur.execute(f'''INSERT INTO Library (name, genre, autor, country, img, desc)
                VALUES(\"{self.name.text()}\", \"{key}\", \"{self.autor.text()}\", \"{self.count.text()}\", 
                 \"{n_i}\", \"{n_d}\")''')
                con.commit()
                with shelve.open('nigi') as kni:
                    g = self.genres.toPlainText().split(', ')
                    kni[key] = g
                self.close()

    def cls(self):
        self.close()