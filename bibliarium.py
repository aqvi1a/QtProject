import sys, shelve, sqlite3, os

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap, QIcon
from dialog import Dialog


class MainW(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('PROJECT.ui', self)
        con = sqlite3.connect('books.db')
        self.cur = con.cursor()
        self.right_now = None
        self.favourite = self.cur.execute(f'''SELECT title FROM Favourite''').fetchall()
        c = self.cur.execute("""SELECT DISTINCT autor FROM Library""").fetchall()
        c2 = self.cur.execute("""SELECT DISTINCT country FROM Library""").fetchall()
        db = self.cur.execute('''SELECT * FROM Library''').fetchall()
        for i in self.favourite:
            self.spisok_fav.addItem(i[0])
        with shelve.open('nigi') as kni:
            k, c1 = [], kni.values()
            for i in c1:
                k += i
            k = list(set(k))
            k.sort()
        for i in c:
            self.autor.addItem(''.join(i))
        for i in k:
            self.genre.addItem(''.join(i.capitalize()).strip())
        for i in c2:
            self.country.addItem(''.join(i))
        self.dbtable.setRowCount(len(db))
        self.dbtable.setColumnCount(7)
        self.dbtable.setHorizontalHeaderLabels(['№', 'Название', 'Жанр', 'Автор', 'Страна', 'Изображение', 'Описание'])
        for i, item in enumerate(db):
            for j in range(7):
                self.dbtable.setItem(i, j, QTableWidgetItem(str(item[j])))
                if j in [0, 1, 2, 5, 6]:
                    self.dbtable.item(i, j).setFlags(QtCore.Qt.ItemIsEnabled)
        self.db_change_dict = {}
        self.podbor.clicked.connect(self.filtr)
        self.lupa.clicked.connect(self.pupa)
        self.spisok.currentItemChanged.connect(self.lis)
        self.spisok_fav.currentItemChanged.connect(self.lis_fav)
        self.zaklad.clicked.connect(self.fav)
        self.tab.currentChanged.connect(self.changed)
        self.dbtable.itemChanged.connect(self.db_changed)
        self.save_changes.clicked.connect(self.save_db_changes)
        self.add_book.clicked.connect(self.add)
        self.del_but.clicked.connect(self.delet)

    def db_update(self):
        db = self.cur.execute('''SELECT * FROM Library''').fetchall()
        self.dbtable.setRowCount(len(db))
        self.dbtable.setColumnCount(7)
        self.dbtable.setHorizontalHeaderLabels(['№', 'Название', 'Жанр', 'Автор', 'Страна', 'Изображение', 'Описание'])
        for i, item in enumerate(db):
            for j in range(7):
                self.dbtable.setItem(i, j, QTableWidgetItem(str(item[j])))
                if j in [0, 1, 2, 5, 6]:
                    self.dbtable.item(i, j).setFlags(QtCore.Qt.ItemIsEnabled)
        self.db_change_dict = {}
        self.smth()

    def smth(self):
        con = sqlite3.connect('books.db')
        self.cur = con.cursor()
        self.country.clear(), self.autor.clear(), self.genre.clear()
        c = self.cur.execute("""SELECT DISTINCT autor FROM Library""").fetchall()
        c2 = self.cur.execute("""SELECT DISTINCT country FROM Library""").fetchall()
        self.country.addItem('Все'), self.autor.addItem('Все'), self.genre.addItem('Все')
        with shelve.open('nigi') as kni:
            c1, k = kni.values(), []
            for i in c1:
                k += i
            k = list(set(k))
            k.sort()
        for i in c:
            self.autor.addItem(''.join(i))
        for i in k:
            self.genre.addItem(''.join(i.capitalize()).strip())
        for i in c2:
            self.country.addItem(''.join(i))

    def changed(self):
        if self.tab.currentIndex() == 1:
            if not self.spisok_fav:
                self.img_show2.clear()
                self.description2.clear()

    def in_fav(self):
        jk = self.cur.execute(f'''SELECT name FROM Library
                                        WHERE img = \"{self.right_now}\"''').fetchall()[0][0]
        f = [i[0] for i in self.favourite]
        if jk in f:
            self.zaklad.setIcon(QIcon('icons/fav.png'))
        else:
            self.zaklad.setIcon(QIcon('icons/non_fav.png'))

    def filtr(self):  # функция подбора по параметрам
        self.spisok.clear()
        self.img_show.clear()
        self.description.clear()
        self.right_now = None
        self.zaklad.setIcon(QIcon('icons/non_fav.png'))
        genr_k = []
        if self.genre.currentText() != 'Все':
            with shelve.open('nigi') as f:
                k = self.cur.execute('''SELECT genre FROM Library''').fetchall()
                for el in k:
                    if self.genre.currentText() in f[el[0]]:
                        n = self.cur.execute(f'''SELECT name, autor FROM Library
                        WHERE genre = \"{el[0]}\"''').fetchall()
                        genr_k.append([n[0][0], n[0][1]])
        elems, boxes, fi = ['autor', 'country'], [self.autor, self.country], []
        for el in boxes:
            if el.currentText() != 'Все':
                fi.append(f'{elems[boxes.index(el)]} = "{el.currentText()}"')
        if not fi and not genr_k:
            filt = self.cur.execute('''SELECT name, autor FROM Library''').fetchall()
            for ele in filt:
                self.spisok.addItem(f'{ele[0]}, {ele[1]}')
        else:
            if fi and genr_k:
                filt = self.cur.execute(f'''SELECT name, autor FROM Library
                WHERE {'AND '.join(fi)}''').fetchall()
                for ele in filt:
                    if list(ele) in genr_k:
                        self.spisok.addItem(f'{ele[0]}, {ele[1]}')
            elif fi:
                filt = self.cur.execute(f'''SELECT name, autor FROM Library
                                WHERE {'AND '.join(fi)}''').fetchall()
                for ele in filt:
                    self.spisok.addItem(f'{ele[0]}, {ele[1]}')
            else:
                for ele in genr_k:
                    self.spisok.addItem(f'{ele[0]}, {ele[1]}')

    def pupa(self):  # функция подбора по поисковой строке
        n = self.stroka.text().capitalize()
        c = self.cur.execute(f'''SELECT img, desc FROM Library
        WHERE name = "{n}"''').fetchall()
        if c:
            with open(f'descrip/{c[0][1]}', encoding='utf-8') as file:
                self.description.setText(file.read())
            imag = QPixmap(f'images/{c[0][0]}')
            self.img_show.setPixmap(imag)
            self.right_now = c[0][0]
            self.in_fav()
        else:
            self.description.setText('Книга не найдена')
            self.img_show.clear()

    def lis(self):  # функция отображения данных из списка
        try:
            book = self.spisok.currentItem()
            n = book.text().split(',')[0]
            c = self.cur.execute(f'''SELECT img, desc FROM Library
                    WHERE name = "{n}"''').fetchall()
            with open(f'descrip/{c[0][1]}', encoding='utf-8') as file:
                self.description.setText(file.read())
            imag = QPixmap(f'images/{c[0][0]}')
            self.img_show.setPixmap(imag)
            self.right_now = c[0][0]
            self.in_fav()
        except AttributeError:
            pass

    def lis_fav(self):  # функция отображения данных из списка
        try:
            book = self.spisok_fav.currentItem()
            n = book.text().split(',')[0]
            c = self.cur.execute(f'''SELECT img, desc FROM Library
                    WHERE name = "{n}"''').fetchall()
            with open(f'descrip/{c[0][1]}', encoding='utf-8') as file:
                self.description2.setText(file.read())
            imag = QPixmap(f'images/{c[0][0]}')
            self.img_show2.setPixmap(imag)
        except AttributeError:
            pass

    def fav(self):
        try:
            con = sqlite3.connect('books.db')
            cur = con.cursor()
            if self.right_now:
                c = cur.execute(f'''SELECT name FROM Library
                WHERE img = \"{self.right_now}\"''').fetchall()[0][0]
                f = [i[0] for i in self.favourite]
                if c not in f:
                    cur.execute(f'''INSERT INTO Favourite(title) VALUES("{c}")''')
                    con.commit()
                    self.zaklad.setIcon(QIcon('icons/fav.png'))
                    self.favourite = cur.execute(f'''SELECT title FROM Favourite''').fetchall()
                else:
                    cur.execute(f'''DELETE FROM Favourite WHERE title = "{c}"''')
                    con.commit()
                    self.zaklad.setIcon(QIcon('icons/non_fav.png'))
                    self.favourite = cur.execute(f'''SELECT title FROM Favourite''').fetchall()
                self.spisok_fav.clear()
                for el in self.favourite:
                    self.spisok_fav.addItem(el[0])
        except IndexError:
            pass

    def db_changed(self, item):
        n = self.dbtable.horizontalHeaderItem(item.column()).text()
        idi = self.dbtable.item(item.row(), 0).text()
        self.db_change_dict.setdefault(idi, []).append([n, item.text()])

    def save_db_changes(self):
        con = sqlite3.connect('books.db')
        cur = con.cursor()
        user_to_db = {'Название': 'name', 'Автор': 'autor', 'Страна': 'country'}
        for el in self.db_change_dict:
            for val in self.db_change_dict[el]:
                new = user_to_db[val[0]]
                cur.execute(f'''UPDATE Library SET {new}=\"{val[1]}\" WHERE id={el}''')
                con.commit()
        self.smth()

    def add(self):
        dia = Dialog()
        dia.exec()
        self.db_update()

    def delet(self):
        now = self.dbtable.currentItem()
        n = self.dbtable.horizontalHeaderItem(now.column()).text()
        con = sqlite3.connect('books.db')
        cur = con.cursor()
        user_to_db = {'Название': 'name', 'Автор': 'autor', 'Страна': 'country', "№": 'id', 'Изображение': 'img',
                      'Описание': 'desc'}
        new = user_to_db[n]
        a = cur.execute(f'''SELECT name, genre FROM Library WHERE {new}=\"{now.text()}\"''').fetchall()
        print(a)
        tit, genr = a[0][0], a[0][1]
        cur.execute(f'''DELETE FROM Library WHERE name = \"{tit}\"''')
        cur.execute(f'''DELETE FROM Favourite WHERE title = \"{tit}\"''')
        with shelve.open('nigi') as sh:
            del sh[genr]
        p_desc = os.path.abspath('descrip')
        p_imag = os.path.abspath('images')
        os.remove(f'{p_imag}/{genr}.jpg')
        os.remove(f'{p_desc}/{genr}.txt')
        con.commit()
        self.smth()
        self.spisok_fav.clear()
        self.favourite = self.cur.execute(f'''SELECT title FROM Favourite''').fetchall()
        for i in self.favourite:
            self.spisok_fav.addItem(i[0])
        self.db_update()
        self.spisok.clear(), self.description.clear(), self.zaklad.setIcon(QIcon('icons/non_fav.png')), \
        self.img_show.clear()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainW()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())