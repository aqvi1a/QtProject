# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PROJECT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 859)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(790, 859))
        MainWindow.setMaximumSize(QtCore.QSize(790, 859))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.description = QtWidgets.QLabel(self.Main)
        self.description.setGeometry(QtCore.QRect(350, 500, 391, 261))
        self.description.setAutoFillBackground(False)
        self.description.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.description.setFrameShadow(QtWidgets.QFrame.Raised)
        self.description.setText("")
        self.description.setTextFormat(QtCore.Qt.RichText)
        self.description.setScaledContents(False)
        self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description.setWordWrap(True)
        self.description.setOpenExternalLinks(False)
        self.description.setObjectName("description")
        self.listView = QtWidgets.QListView(self.Main)
        self.listView.setGeometry(QtCore.QRect(340, 10, 421, 761))
        self.listView.setObjectName("listView")
        self.img_show = QtWidgets.QLabel(self.Main)
        self.img_show.setGeometry(QtCore.QRect(350, 20, 311, 461))
        self.img_show.setText("")
        self.img_show.setPixmap(QtGui.QPixmap("../../../../../Desktop/2836943_detail.jpg"))
        self.img_show.setScaledContents(True)
        self.img_show.setObjectName("img_show")
        self.zaklad = QtWidgets.QPushButton(self.Main)
        self.zaklad.setEnabled(True)
        self.zaklad.setGeometry(QtCore.QRect(725, 20, 20, 23))
        self.zaklad.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("non_fav.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zaklad.setIcon(icon)
        self.zaklad.setObjectName("zaklad")
        self.spisok = QtWidgets.QListWidget(self.Main)
        self.spisok.setGeometry(QtCore.QRect(10, 220, 321, 551))
        self.spisok.setObjectName("spisok")
        self.groupBox = QtWidgets.QGroupBox(self.Main)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 261, 151))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 241, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.genre = QtWidgets.QComboBox(self.layoutWidget)
        self.genre.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.genre.setObjectName("genre")
        self.genre.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.genre)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.country = QtWidgets.QComboBox(self.layoutWidget)
        self.country.setObjectName("country")
        self.country.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.country)
        self.autor = QtWidgets.QComboBox(self.layoutWidget)
        self.autor.setObjectName("autor")
        self.autor.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.autor)
        self.podbor = QtWidgets.QPushButton(self.groupBox)
        self.podbor.setGeometry(QtCore.QRect(10, 110, 91, 31))
        self.podbor.setObjectName("podbor")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Main)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 301, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lupa = QtWidgets.QPushButton(self.groupBox_2)
        self.lupa.setEnabled(True)
        self.lupa.setGeometry(QtCore.QRect(260, 20, 31, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.lupa.sizePolicy().hasHeightForWidth())
        self.lupa.setSizePolicy(sizePolicy)
        self.lupa.setMaximumSize(QtCore.QSize(102, 100))
        self.lupa.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("but.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lupa.setIcon(icon1)
        self.lupa.setObjectName("lupa")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 23, 241, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.stroka = QtWidgets.QLineEdit(self.layoutWidget1)
        self.stroka.setObjectName("stroka")
        self.horizontalLayout_2.addWidget(self.stroka)
        self.listView.raise_()
        self.description.raise_()
        self.img_show.raise_()
        self.zaklad.raise_()
        self.spisok.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.tab.addTab(self.Main, "")
        self.Mark = QtWidgets.QWidget()
        self.Mark.setObjectName("Mark")
        self.spisok_fav = QtWidgets.QListWidget(self.Mark)
        self.spisok_fav.setGeometry(QtCore.QRect(10, 10, 256, 301))
        self.spisok_fav.setObjectName("spisok_fav")
        self.listView_3 = QtWidgets.QListView(self.Mark)
        self.listView_3.setGeometry(QtCore.QRect(300, 10, 421, 761))
        self.listView_3.setObjectName("listView_3")
        self.img_show2 = QtWidgets.QLabel(self.Mark)
        self.img_show2.setGeometry(QtCore.QRect(310, 20, 311, 461))
        self.img_show2.setText("")
        self.img_show2.setPixmap(QtGui.QPixmap("../../../../../Desktop/2836943_detail.jpg"))
        self.img_show2.setScaledContents(True)
        self.img_show2.setObjectName("img_show2")
        self.description2 = QtWidgets.QLabel(self.Mark)
        self.description2.setGeometry(QtCore.QRect(310, 500, 391, 261))
        self.description2.setAutoFillBackground(False)
        self.description2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.description2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.description2.setText("")
        self.description2.setTextFormat(QtCore.Qt.RichText)
        self.description2.setScaledContents(False)
        self.description2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description2.setWordWrap(True)
        self.description2.setOpenExternalLinks(False)
        self.description2.setObjectName("description2")
        self.tab.addTab(self.Mark, "")
        self.DB = QtWidgets.QWidget()
        self.DB.setObjectName("DB")
        self.dbtable = QtWidgets.QTableWidget(self.DB)
        self.dbtable.setGeometry(QtCore.QRect(10, 10, 751, 341))
        self.dbtable.setObjectName("dbtable")
        self.dbtable.setColumnCount(0)
        self.dbtable.setRowCount(0)
        self.save_changes = QtWidgets.QPushButton(self.DB)
        self.save_changes.setGeometry(QtCore.QRect(10, 360, 131, 23))
        self.save_changes.setObjectName("save_changes")
        self.tab.addTab(self.DB, "")
        self.horizontalLayout.addWidget(self.tab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(2)
        self.genre.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Фильтры"))
        self.label_2.setText(_translate("MainWindow", "Жанры:"))
        self.genre.setCurrentText(_translate("MainWindow", "Все"))
        self.genre.setItemText(0, _translate("MainWindow", "Все"))
        self.label_3.setText(_translate("MainWindow", "Авторы:"))
        self.label_4.setText(_translate("MainWindow", "Страна:"))
        self.country.setItemText(0, _translate("MainWindow", "Все"))
        self.autor.setItemText(0, _translate("MainWindow", "Все"))
        self.podbor.setText(_translate("MainWindow", "Подобрать"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Поиск по названию"))
        self.label_5.setText(_translate("MainWindow", "Поиск"))
        self.tab.setTabText(self.tab.indexOf(self.Main), _translate("MainWindow", "Библиариум"))
        self.tab.setTabText(self.tab.indexOf(self.Mark), _translate("MainWindow", "Закладки"))
        self.save_changes.setText(_translate("MainWindow", "Сохранить изменения"))
        self.tab.setTabText(self.tab.indexOf(self.DB), _translate("MainWindow", "DB"))
