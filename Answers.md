# Bibliarium
## Пояснительная записка
### 1. Устройство интерфейса
Программа представляет собой вариацию книжного магазина. Состоит из трех вкладок: 
- Первая вкладка (Библиариум) является каталогом. Пользователь может задать три опциональных параметра и из составленного списка выбирать книги. При выборе любой книги будет показана ее обложка, аннотация и кнопка добавления в закладки  - готово
-	Вторая вкладка (Закладки) предоставляет пользователю список сохраненных книг  - готово
-	Третья вкладка (BD) предоставляет пользователю базу данных с опциональной возможностью добавления своей книги - в процессе

### 2. Структура вкладок
-----------------
#### 2.1.1 Главная страница
Интерфейс пользователя:
[![Screenshot-2021-11-08-224915.jpg](https://i.postimg.cc/3w2qtXq5/Screenshot-2021-11-08-224915.jpg)](https://postimg.cc/nscTzDZ0)

#### 2.1.2 Код
Выбрать книгу можно 2 вариантами:
- Вбить название в страницу поиска, если книга есть, то она покажется, иначе выведется надпись "Книга не найдена".
Код функции поиска:
```python
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
```
- Задать параметры для поиска (или оставить как есть) и в предложенно списке выбрать книгу.
Для осуществления работы используется несколько функций. Их код представлен ниже.

Функция подбора по параметрам:
```python
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
```
Функция отображения выбранной книги:
```python
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
```
Также используется вспомогательная функция cheto() - необходимо для корректного отображения состояния (в закладках/не в закладках) для книги:
```python
    def cheto(self):
        jk = self.cur.execute(f'''SELECT name FROM Library
                                        WHERE img = \"{self.right_now}\"''').fetchall()[0][0]
        f = [i[0] for i in self.favourite]
        if jk in f:
            self.zaklad.setIcon(QIcon('fav.png'))
        else:
            self.zaklad.setIcon(QIcon('non_fav.png'))
```
Дальнейшее заполнение  - в процессе