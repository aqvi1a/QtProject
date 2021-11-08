import sys, shelve, sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon


class MainW(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('PROJECT.ui', self)
        con = sqlite3.connect('books.db')
        self.cur = con.cursor()
        self.right_now = None
        self.favourite = self.cur.execute(f'''SELECT title FROM Favourite''').fetchall()
        for el in self.favourite:
            self.spisok_fav.addItem(el[0])
        with shelve.open('nigi.txt') as kni:
            c1 = kni.values()
            k = []
            for el in c1:
                k += el
        c = self.cur.execute("""SELECT DISTINCT autor FROM Library""").fetchall()
        c2 = self.cur.execute("""SELECT DISTINCT country FROM Library""").fetchall()
        for el in c:
            self.autor.addItem(''.join(el))
        for el in set(k):
            self.genre.addItem(''.join(el).strip())
        for el in c2:
            self.country.addItem(''.join(el))
        self.podbor.clicked.connect(self.filtr)
        self.lupa.clicked.connect(self.pupa)
        self.spisok.currentItemChanged.connect(self.lis)
        self.spisok_fav.currentItemChanged.connect(self.lis_fav)
        self.zaklad.clicked.connect(self.fav)

    def cheto(self):
        jk = self.cur.execute(f'''SELECT name FROM Library
                                        WHERE img = \"{self.right_now}\"''').fetchall()[0][0]
        f = [i[0] for i in self.favourite]
        if jk in f:
            self.zaklad.setIcon(QIcon('fav.png'))
        else:
            self.zaklad.setIcon(QIcon('non_fav.png'))

    def filtr(self):  # функция подбора по параметрам
        self.spisok.clear()
        genr_k = []
        if self.genre.currentText() !='Все':
            with shelve.open('nigi.txt') as f:
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
            self.niga.setPixmap(imag)
            self.right_now = c[0][0]
            self.cheto()
        else:
            self.description.setText('Книга не найдена')
            self.niga.clear()

    def lis(self):  # функция отображения данных из списка
        nigga = self.spisok.currentItem()
        n = nigga.text().split(',')[0]
        c = self.cur.execute(f'''SELECT img, desc FROM Library
                WHERE name = "{n}"''').fetchall()
        with open(f'descrip/{c[0][1]}', encoding='utf-8') as file:
            self.description.setText(file.read())
        imag = QPixmap(f'images/{c[0][0]}')
        self.niga.setPixmap(imag)
        self.right_now = c[0][0]
        self.cheto()

    def lis_fav(self):  # функция отображения данных из списка
        nigga = self.spisok_fav.currentItem()
        n = nigga.text().split(',')[0]
        c = self.cur.execute(f'''SELECT img, desc FROM Library
                WHERE name = "{n}"''').fetchall()
        with open(f'descrip/{c[0][1]}', encoding='utf-8') as file:
            self.description2.setText(file.read())
        imag = QPixmap(f'images/{c[0][0]}')
        self.nigg_2.setPixmap(imag)

    def fav(self):
        con = sqlite3.connect('books.db')
        cur = con.cursor()
        if self.niga:
            c = cur.execute(f'''SELECT name FROM Library
            WHERE img = \"{self.right_now}\"''').fetchall()[0][0]
            f = [i[0] for i in self.favourite]
            if c not in f:
                cur.execute(f'''INSERT INTO Favourite(title) VALUES("{c}")''')
                con.commit()
                self.zaklad.setIcon(QIcon('fav.png'))
                self.favourite = cur.execute(f'''SELECT title FROM Favourite''').fetchall()
            else:
                cur.execute(f'''DELETE FROM Favourite WHERE title = "{c}"''')
                con.commit()
                self.zaklad.setIcon(QIcon('non_fav.png'))
                self.favourite = cur.execute(f'''SELECT title FROM Favourite''').fetchall()
            self.spisok_fav.clear()
            for el in self.favourite:
                self.spisok_fav.addItem(el[0])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainW()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
