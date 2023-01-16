# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 605)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(361, 605))
        MainWindow.setMaximumSize(QtCore.QSize(361, 605))
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dice3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.autodice = QtWidgets.QWidget(MainWindow)
        self.autodice.setMouseTracking(True)
        self.autodice.setObjectName("autodice")
        self.tg_api_settings = QtWidgets.QGroupBox(self.autodice)
        self.tg_api_settings.setGeometry(QtCore.QRect(10, 10, 341, 91))
        self.tg_api_settings.setObjectName("tg_api_settings")
        self.api_hash_label = QtWidgets.QLabel(self.tg_api_settings)
        self.api_hash_label.setGeometry(QtCore.QRect(10, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Georgian")
        font.setPointSize(10)
        self.api_hash_label.setFont(font)
        self.api_hash_label.setObjectName("api_hash_label")
        self.api_id_label = QtWidgets.QLabel(self.tg_api_settings)
        self.api_id_label.setGeometry(QtCore.QRect(10, 30, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Georgian")
        font.setPointSize(10)
        self.api_id_label.setFont(font)
        self.api_id_label.setObjectName("api_id_label")
        self.api_hash = QtWidgets.QLineEdit(self.tg_api_settings)
        self.api_hash.setGeometry(QtCore.QRect(100, 60, 231, 21))
        self.api_hash.setText("")
        self.api_hash.setAlignment(QtCore.Qt.AlignCenter)
        self.api_hash.setObjectName("api_hash")
        self.api_id = QtWidgets.QLineEdit(self.tg_api_settings)
        self.api_id.setGeometry(QtCore.QRect(100, 30, 231, 21))
        self.api_id.setText("")
        self.api_id.setAlignment(QtCore.Qt.AlignCenter)
        self.api_id.setObjectName("api_id")
        self.script_log = QtWidgets.QGroupBox(self.autodice)
        self.script_log.setGeometry(QtCore.QRect(10, 300, 341, 141))
        self.script_log.setObjectName("script_log")
        self.log = QtWidgets.QTextBrowser(self.script_log)
        self.log.setGeometry(QtCore.QRect(10, 30, 321, 101))
        self.log.setOpenLinks(False)
        self.log.setObjectName("log")
        self.script_settings = QtWidgets.QGroupBox(self.autodice)
        self.script_settings.setGeometry(QtCore.QRect(10, 110, 341, 181))
        self.script_settings.setObjectName("script_settings")
        self.chat_id = QtWidgets.QLineEdit(self.script_settings)
        self.chat_id.setGeometry(QtCore.QRect(120, 85, 211, 21))
        self.chat_id.setText("")
        self.chat_id.setAlignment(QtCore.Qt.AlignCenter)
        self.chat_id.setObjectName("chat_id")
        self.chat_id_label = QtWidgets.QLabel(self.script_settings)
        self.chat_id_label.setGeometry(QtCore.QRect(10, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Georgian")
        font.setPointSize(10)
        self.chat_id_label.setFont(font)
        self.chat_id_label.setObjectName("chat_id_label")
        self.min_value = QtWidgets.QSpinBox(self.script_settings)
        self.min_value.setGeometry(QtCore.QRect(280, 25, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.min_value.setFont(font)
        self.min_value.setMinimum(1)
        self.min_value.setMaximum(6)
        self.min_value.setProperty("value", 4)
        self.min_value.setObjectName("min_value")
        self.start_button = QtWidgets.QPushButton(self.script_settings)
        self.start_button.setGeometry(QtCore.QRect(10, 120, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.start_button.setFont(font)
        self.start_button.setCheckable(True)
        self.start_button.setChecked(False)
        self.start_button.setObjectName("start_button")
        self.min_value_label = QtWidgets.QLabel(self.script_settings)
        self.min_value_label.setGeometry(QtCore.QRect(10, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Georgian")
        font.setPointSize(10)
        self.min_value_label.setFont(font)
        self.min_value_label.setObjectName("min_value_label")
        self.dice_type_label = QtWidgets.QLabel(self.script_settings)
        self.dice_type_label.setGeometry(QtCore.QRect(10, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Georgian")
        font.setPointSize(10)
        self.dice_type_label.setFont(font)
        self.dice_type_label.setObjectName("dice_type_label")
        self.dice_type = QtWidgets.QComboBox(self.script_settings)
        self.dice_type.setGeometry(QtCore.QRect(120, 55, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dice_type.setFont(font)
        self.dice_type.setEditable(False)
        self.dice_type.setMaxVisibleItems(3)
        self.dice_type.setMaxCount(3)
        self.dice_type.setObjectName("dice_type")
        self.dice_type.addItem("")
        self.dice_type.addItem("")
        self.dice_type.addItem("")
        self.about_coder = QtWidgets.QGroupBox(self.autodice)
        self.about_coder.setGeometry(QtCore.QRect(10, 450, 341, 145))
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.about_coder.setFont(font)
        self.about_coder.setObjectName("about_coder")
        self.coded_by = QtWidgets.QLabel(self.about_coder)
        self.coded_by.setGeometry(QtCore.QRect(10, 20, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.coded_by.setFont(font)
        self.coded_by.setFocusPolicy(QtCore.Qt.NoFocus)
        self.coded_by.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.coded_by.setAutoFillBackground(False)
        self.coded_by.setFrameShadow(QtWidgets.QFrame.Plain)
        self.coded_by.setTextFormat(QtCore.Qt.AutoText)
        self.coded_by.setScaledContents(False)
        self.coded_by.setAlignment(QtCore.Qt.AlignCenter)
        self.coded_by.setObjectName("coded_by")
        self.web_label = QtWidgets.QLabel(self.about_coder)
        self.web_label.setGeometry(QtCore.QRect(10, 50, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.web_label.setFont(font)
        self.web_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.web_label.setObjectName("web_label")
        self.web_button = QtWidgets.QPushButton(self.about_coder)
        self.web_button.setGeometry(QtCore.QRect(100, 50, 231, 25))
        self.web_button.setObjectName("web_button")
        self.tg_label = QtWidgets.QLabel(self.about_coder)
        self.tg_label.setGeometry(QtCore.QRect(10, 80, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tg_label.setFont(font)
        self.tg_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tg_label.setObjectName("tg_label")
        self.tg_button = QtWidgets.QPushButton(self.about_coder)
        self.tg_button.setGeometry(QtCore.QRect(100, 80, 231, 25))
        self.tg_button.setObjectName("tg_button")
        self.qiwi_label = QtWidgets.QLabel(self.about_coder)
        self.qiwi_label.setGeometry(QtCore.QRect(10, 110, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.qiwi_label.setFont(font)
        self.qiwi_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qiwi_label.setObjectName("qiwi_label")
        self.qiwi_button = QtWidgets.QPushButton(self.about_coder)
        self.qiwi_button.setGeometry(QtCore.QRect(100, 110, 231, 25))
        self.qiwi_button.setObjectName("qiwi_button")
        MainWindow.setCentralWidget(self.autodice)

        self.retranslateUi(MainWindow)
        self.dice_type.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoDice v1.1"))
        self.tg_api_settings.setTitle(_translate("MainWindow", "Настройки telegram api"))
        self.api_hash_label.setText(_translate("MainWindow", "api_hash"))
        self.api_id_label.setText(_translate("MainWindow", "api_id"))
        self.api_hash.setPlaceholderText(_translate("MainWindow", "token"))
        self.api_id.setPlaceholderText(_translate("MainWindow", "12345"))
        self.script_log.setTitle(_translate("MainWindow", "Лог скрипта"))
        self.script_settings.setTitle(_translate("MainWindow", "Настройки скрипта"))
        self.chat_id.setPlaceholderText(_translate("MainWindow", "-1001438070264"))
        self.chat_id_label.setText(_translate("MainWindow", "ID чата"))
        self.start_button.setText(_translate("MainWindow", "Запуск"))
        self.min_value_label.setText(_translate("MainWindow", "Минимальное значение кости"))
        self.dice_type_label.setText(_translate("MainWindow", "Тип кости"))
        self.dice_type.setItemText(0, _translate("MainWindow", "кубик"))
        self.dice_type.setItemText(1, _translate("MainWindow", "дартс"))
        self.dice_type.setItemText(2, _translate("MainWindow", "баскетбол"))
        self.about_coder.setTitle(_translate("MainWindow", "О создателе"))
        self.coded_by.setText(_translate("MainWindow", "Coded by andr"))
        self.web_label.setText(_translate("MainWindow", "WWW:"))
        self.web_button.setText(_translate("MainWindow", "@andr"))
        self.tg_label.setText(_translate("MainWindow", "Telegram:"))
        self.tg_button.setText(_translate("MainWindow", "@andr"))
        self.qiwi_label.setText(_translate("MainWindow", "QIWI:"))
        self.qiwi_button.setText(_translate("MainWindow", "Купи мне дошик ;)"))