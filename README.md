# QtProject
## Техническое задание
### 1. Описание
Программа представляет собой вариацию книжного магазина. Состоит из трех вкладок: 
- Первая вкладка (Главная страница) является каталогом. Пользователь может задать три опциональных параметра и из составленного списка выбирать книги. При выборе любой книги будет показана ее обложка, аннотация и кнопка добавления в закладки (Пункты 2.1)
-	Вторая вкладка (Закладки) предоставляет пользователю список сохраненных книг (Пункт 2.2)
-	Третья вкладка (БД) предоставляет пользователю базу данных с опциональной возможностью добавления своей книги (Пункт 2.3)

### 2. Структура вкладок
-----------------
#### 2.1.1 Главная страница
Интерфейс пользователя:
[![Screenshot-2021-10-28-223745.jpg](https://i.postimg.cc/137mDnNt/Screenshot-2021-10-28-223745.jpg)](https://postimg.cc/hXxRBGsW)

#### 2.1.2 Структура
Для осуществления работы используются:
-	3 QFontBox(-а) – для установки параметров подбора книг
-	QListWidget – для отображения списка книг
-	2QPushButton(-а) – для добавления книги в закладки и запуска функции подбора
-	2 QLabel(-а) – для отображения аннотации и обложки книги.

#### 2.1.3 Принцип работы
Для работы необходима БД, в которой хранится название, автор и страна выпуска книги. После нажатия на кнопку «Подобрать» исполняется функция подбора, ее результат выводится в список. При нажатии на любой из результатов будут считываться закрепленные за ним значения (изображение и текст) и выводиться внутри виджета справа. При нажатии на кнопку «В закладки» название книги будет добавляться в текстовый документ.

-------------
#### 2.2.1 Структура
Для осуществления работы используются:
-	QListWidget – для отображения списка книг
-	2 QLabel(-а) – для отображения аннотации и обложки книги

#### 2.2.2 Принцип работы
Работа устроена по схожему принципу, только пользователь не указывает никаких параметров. Данные для отображения берутся из БД. Подбор основан на выборе тех книг, названия которых есть в текстовом файле (сделано так, чтобы даже при выключении программы данные не стирались). В остальном работает все также.

-----------------
#### 2.3.1 Структура
Для осуществления работы используются:
-	QListWidget – для отображения списка БД
-	QPushButton – для подтверждения осуществления удаления/изменения/добавления информации

#### 2.3.2 Принцип работы
На странице будет отображена БД в виде таблицы (будет использоваться QListWidget). Также пользователю будет предоставлена возможность удалить, изменить и добавить новую книгу. Для добавления информации пользователю следует нажать соответствующую кнопку. После нажатия ему будет выведено окно (QMessageBox) в который он добавит необходимые данные, после чего книга будет добавлена в словарь.

--------------
### 3. Примечание
Обязательно должны быть осуществлены пункты (2.1 и 2.2), пункт 2.3 может быть выполнен частично (отображение БД и его функционирование).
README по мере работы может получить изменения.
Принцип работ может измениться
