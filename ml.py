import turtle
import time
import math
from PyQt5 import QtCore, QtGui, QtWidgets

t = turtle.Turtle()  # ракета
t.screen.setup(width=1200, height=1000, startx=0, starty=0)
t1 = turtle.Turtle()  # Рисовалка рамок и надписей
t2 = turtle.Turtle()  # самолет
t3 = turtle.Turtle()
t4 = turtle.Turtle()  # параметры
t5 = turtle.Turtle()  # масштаб
t6 = turtle.Turtle()  # самолет в энергетике
t7 = turtle.Turtle()  # ловушка в энергетике
t8 = turtle.Turtle()  # тросс
t9 = turtle.Turtle()  # энергоцентр
t0 = turtle.Turtle()  # Рисовалка вертикального масштаба
t4_start = t4.pos()
t5_start = t5.pos()
t8_start = t8.pos()
t9_start = t9.pos()
t0_start = t0.pos()


class Ui_MainWindow(object):
    def __init__(self):
        self.input_energ_lov = 0
        self.rocket_energo = 0
        self.epr_airplane = 0
        # self.current_range = 10
        self.PxG = 0


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_en_pot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_en_pot.setGeometry(QtCore.QRect(800, 250, 120, 30))
        self.pushButton_en_pot.setObjectName("pushButton")
        self.pushButton_en_pot.setStyleSheet("QPushButton{background-color : lightblue;}")
        self.pushButton_en_pot.clicked.connect(self.start)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(102, 60, 61, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(78, 63, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 62, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(208, 102, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 115, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 100, 61, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 129, 291, 201))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget.verticalHeader().setMinimumSectionSize(28)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 33, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(598, 65, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(506, 66, 16, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 63, 61, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(598, 135, 41, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(471, 133, 51, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 133, 61, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(532, 171, 61, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(383, 171, 141, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(600, 173, 100, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(410, 207, 121, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(598, 215, 31, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(530, 213, 61, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(384, 220, 151, 20))
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(420, 280, 101, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(598, 282, 131, 16))
        self.label_18.setObjectName("label_18")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(530, 280, 61, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(870, 30, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(792, 63, 131, 20))
        self.label_20.setObjectName("label_20")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(932, 63, 61, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1000, 65, 131, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(808, 104, 121, 20))
        self.label_22.setObjectName("label_22")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(932, 104, 61, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1000, 106, 31, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(780, 143, 151, 20))
        self.label_24.setObjectName("label_24")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(932, 143, 61, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(1000, 145, 31, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(794, 180, 151, 20))
        self.label_26.setObjectName("label_26")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(930, 180, 61, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(598, 102, 16, 16))
        self.label_16.setObjectName("label_16")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(506, 103, 16, 16))
        self.label_30.setObjectName("label_30")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(530, 100, 61, 22))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(431, 245, 91, 30))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(598, 252, 31, 16))
        self.label_32.setObjectName("label_32")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(530, 250, 61, 22))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(380, 252, 151, 30))
        self.label_33.setObjectName("label_33")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(1000, 180, 31, 16))
        self.label_27.setObjectName("label_27")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "20"))
        self.label.setText(_translate("MainWindow", "Параметры ловушки"))
        self.label_2.setText(_translate("MainWindow", "P"))
        self.label_3.setText(_translate("MainWindow", "Вт"))
        self.label_4.setText(_translate("MainWindow", "град."))
        self.label_5.setText(_translate("MainWindow", "Сектор защиты +/-"))
        self.lineEdit_2.setText(_translate("MainWindow", "25"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "+- град"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ку (дБ) аз."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ку (дБ) у.м."))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "0 "))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "9.3"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "9.3"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "8.8"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "8.8"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "8.3"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "8.3"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "7.8"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "7.8"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "20"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "7.3"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "7.3"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "25"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "6.3"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("MainWindow", "6.3"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "Параметры ракеты"))
        self.label_7.setText(_translate("MainWindow", "Вт"))
        self.label_8.setText(_translate("MainWindow", "P"))
        self.lineEdit_3.setText(_translate("MainWindow", "500"))
        self.label_9.setText(_translate("MainWindow", "град."))
        self.label_10.setText(_translate("MainWindow", "Сектор "))
        self.lineEdit_4.setText(_translate("MainWindow", "8"))
        self.lineEdit_5.setText(_translate("MainWindow", "3"))
        self.lineEdit_6.setText(_translate("MainWindow", "75"))
        self.label_11.setText(_translate("MainWindow", "Удаление от самолета"))
        self.label_12.setText(_translate("MainWindow", "км (не менее 3)"))
        self.label_13.setText(_translate("MainWindow", "Положение ракеты"))
        self.label_14.setText(_translate("MainWindow", "град"))
        self.label_15.setText(_translate("MainWindow", "относительно самолета"))
        self.label_17.setText(_translate("MainWindow", "Скорость ракеты"))
        self.label_18.setText(_translate("MainWindow", "м/сек"))
        self.lineEdit_7.setText(_translate("MainWindow", "2500"))
        self.label_19.setText(_translate("MainWindow", "Параметры самолета"))
        self.label_20.setText(_translate("MainWindow", "Скорость самолета"))
        self.lineEdit_8.setText(_translate("MainWindow", "500"))
        self.label_21.setText(_translate("MainWindow", "м/сек"))
        self.label_22.setText(_translate("MainWindow",
                                         "<html><head/><body><p>ЭПР ППС (0<span style=\" vertical-align:super;\">о </span>+- 60<span style=\" vertical-align:super;\">о</span>)</p></body></html>"))
        self.lineEdit_9.setText(_translate("MainWindow", "85"))
        self.label_23.setText(_translate("MainWindow",
                                         "<html><head/><body><p>м<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow",
                                         "<html><head/><body><p>ЭПР боковой (90<span style=\" vertical-align:super;\">о </span>+- 30<span style=\" vertical-align:super;\">о</span>)</p></body></html>"))
        self.lineEdit_10.setText(_translate("MainWindow", "1000"))
        self.label_25.setText(_translate("MainWindow",
                                         "<html><head/><body><p>м<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow",
                                         "<html><head/><body><p>ЭПР ЗПС (180<span style=\" vertical-align:super;\">о </span>+- 60<span style=\" vertical-align:super;\">о</span>)</p></body></html>"))
        self.lineEdit_11.setText(_translate("MainWindow", "45"))
        self.label_16.setText(_translate("MainWindow", "Дб"))

        self.label_30.setText(_translate("MainWindow", "Ку"))
        self.lineEdit_12.setText(_translate("MainWindow", "26"))
        self.lineEdit_13.setText(_translate("MainWindow", "9"))
        self.label_31.setText(_translate("MainWindow", "Рабочая частота"))
        self.label_32.setText(_translate("MainWindow", "ГГц"))
        self.pushButton_en_pot.setText('Моделировать')

        self.label_27.setText(_translate("MainWindow",
                                         "<html><head/><body><p>м<span style=\" vertical-align:super;\">2</span></p></body></html>"))

    """ЗАПУСК МОДЕЛИРОВАНИЯ"""

    def zero_point(self):
        t.setheading(0), t0.setheading(0), t.clear(), t1.clear(), t5.clear(), t4.clear()
        t1.speed(100), t1.penup(), t1.hideturtle()
        t.speed(100), t.penup(), t.goto(-150, 0), t.pendown()
        t2.speed(100), t2.penup(), t2.goto(-150, 0), t2.pendown()
        t3.speed(100), t3.penup(), t3.goto(-500, 0), t3.pendown()
        t4.speed(100), t4.penup(), t4.pendown()
        t4.goto(t4_start), t5.goto(t5_start), t8.goto(t8_start), t9.goto(t9_start), t0.goto(t0_start)
        t6.speed(100), t6.penup(), t6.goto(-500, 0), t6.pendown()
        t7.speed(100), t7.penup(), t7.goto(-500, 0), t7.pendown()
        t8.speed(100), t9.speed(100), t0.speed(100)
        t4.hideturtle(), t4.penup(), t4.goto(320, 350), t4.pendown()
        t.hideturtle(), t1.hideturtle(), t2.hideturtle(), t3.hideturtle(), t4.hideturtle(), t5.hideturtle(), t6.hideturtle(),
        t7.hideturtle(), t8.hideturtle(), t9.hideturtle(), t0.hideturtle()

    def start(self):
        MainWindow.showMinimized()
        self.speed_rocket = float(self.lineEdit_7.text().replace(',', '.'))  # скорость ракеты
        self.speed_airplane = float(self.lineEdit_8.text().replace(',', '.'))  # скорость самолета
        self.start_pos_range_km = float(self.lineEdit_5.text().replace(',', '.'))  # стартовая позиция ракеты
        self.start_pos_angle = float(self.lineEdit_6.text().replace(',', '.'))  # стартовый угол атаки ракеты
        self.lov_sector = float(self.lineEdit_2.text().replace(',', '.'))
        self.rocket_sector = float(self.lineEdit_4.text().replace(',', '.'))
        self.Hz = float(3 * (10 ** 8) / (float(self.lineEdit_13.text().replace(',', '.')) * (10 ** 9)))
        self.G_rocket = 10 ** (float(self.lineEdit_12.text().replace(',', '.')) / 10) # Кус ракеты в разах
        self.P_rocket = float(self.lineEdit_3.text().replace(',', '.')) # Мощность ракеты
        self.lenght_sector = 500  # длинна сектора ракеты
        self.current_range = self.start_pos_range_km
        self.input_energ_ot_lovywki = 0
        self.Flag = True
        self.coin = 3
        self.zero_point()
        self.choice_mashtab()

    """ВЫБОР МАСШТАБА ДЛЯ ОТРИСОВКИ"""

    def choice_mashtab(self):
        t0.hideturtle()
        t1.penup(), t1.pensize(3), t1.goto(-570, 450), t1.pendown(), t1.goto(290, 450), t1.goto(290, -420)
        t1.goto(-570, -420), t1.goto(-570, 450)
        t3.clear()

        if self.start_pos_range_km > 20:
            self.start_pos_range = self.start_pos_range_km * 4
            self.speed_airplane_mashtab = self.speed_airplane / 250
            self.speed_rocket_mashtab = self.speed_rocket / 250
            self.set_maschtab(11, 40, 10.000)
            self.coin = 0
            t3.penup(), t3.goto(-250, 420), t3.write('АЗИМУТ. Масштаб скорости 1:1', font=5)
            self.start_point()
        elif self.start_pos_range_km <= 20 and self.start_pos_range_km > 8:
            self.start_pos_range = self.start_pos_range_km * 16
            self.speed_airplane_mashtab = self.speed_airplane / 62
            self.speed_rocket_mashtab = self.speed_rocket / 62
            self.set_maschtab(11, 40, 2.500)
            self.coin = 1
            t3.penup(), t3.goto(-250, 420), t3.write('АЗИМУТ. Масштаб скорости 1:1', font=5)
            self.start_point()
        else:
            self.start_pos_range = self.start_pos_range_km * 60
            self.set_maschtab(14, 32, 500)
            self.speed_airplane_mashtab = round((self.speed_airplane / 16) / 5)
            self.speed_rocket_mashtab = round((self.speed_rocket / 16) / 5)
            self.coin = 2
            t3.penup(), t3.goto(-250, 420), t3.write('АЗИМУТ. Масштаб скорости 1:5', font=5)
            self.start_point()

        """ РИСОВАНИЕ МАСШТАБА"""

    """ОТРИСОВКА МАСШТАБА"""

    def set_maschtab(self, cupucity_ring, range_ring, mashtab):
        for i in range(cupucity_ring):
            t5.hideturtle()
            t5.speed(100)
            t5.color('Gray')
            t5.penup()
            t5.setheading(90)
            t5.goto(range_ring * i - 150, 0)
            t5.write(f'{mashtab * i}')
            t5.pendown()
            t5.circle(range_ring * i)

        """ПОСТАНОВКА РАКЕТЫ В НАЧАЛЬНУЮ ТОЧКУ"""

    """РАСЧЕТ ТОЧКИ НАХОЖДЕНИЯ РАКЕИЫ"""

    def start_point(self):
        t.speed(100)
        t.color('Red')
        t.penup()
        if self.Flag:
            t.forward(self.start_pos_range)
            t.left(90)
            t.circle(self.start_pos_range, self.start_pos_angle)  # изначальное угловое положение
            t.setheading(t.towards(t2.pos()))
            t.pendown()

        """ТОЧКА ПЕРЕХОДА НА СЛЕДУЮЩИЙ ГРАФИК"""

        while self.current_range * 1000 >= self.speed_rocket:
            if math.sqrt((t.pos()[0] - t2.pos()[0]) ** 2 + (t.pos()[1] - t2.pos()[1]) ** 2) <= 100 and self.coin != 2:
                t.goto(t.pos()[0] - t2.pos()[0] - 150, t.pos()[1]), t2.goto(-150, 0), t.setheading(t.towards(t2.pos()))
                t.clear(), t2.clear(), t5.clear()
                t.backward(300)
                self.Flag = False

                self.choice_mashtab()
            else:
                if self.coin == 0:
                    self.start_pos_range_km = round(math.sqrt(
                        (t.pos()[0] - t2.pos()[0]) ** 2 + (t.pos()[1] - t2.pos()[1]) ** 2) / 8, 2)
                elif self.coin == 1:
                    self.start_pos_range_km = round((math.sqrt(
                        (t.pos()[0] - t2.pos()[0]) ** 2 + (t.pos()[1] - t2.pos()[1]) ** 2)) / 32, 2)
                elif self.coin == 2:
                    self.start_pos_range_km = round((math.sqrt(
                        (t.pos()[0] - t2.pos()[0]) ** 2 + (t.pos()[1] - t2.pos()[1]) ** 2)) / 115, 2)
            self.current_range = round(self.start_pos_range_km * 2, 2)
            self.get_trace()
            self.get_speed_init()
            self.input_energ_ot_lovywki = round(self.get_input_energ_ot_lovywki(), 1)
            self.epr_airplane = self.get_input_energ_ot_rocket()
        else:
            self.start_pos_range_km = round((math.sqrt(
                (t.pos()[0] - t2.pos()[0]) ** 2 + (t.pos()[1] - t2.pos()[1]) ** 2)) / 115, 2)
            self.current_range = round(self.start_pos_range_km * 2, 2)
            self.finish()



    """АНИМАЦИЯ СЕКТОРА И ДВИЖЕНИЯ РАКЕТЫ"""

    def get_trace(self):
        if self.start_pos_angle <= 180:
            self.current_angle = round(t.heading() - 180, 2)
            t4.write(f'Расстояние Р-С: {self.current_range} км\nСкорость ракеты: {self.speed_rocket}'
                     f'м/с\nСкорость самолета: {self.speed_airplane}\nУгол поворота Р-С: {self.current_angle}\nЭнергопотенциал '
                     f'ловушки: {self.input_energ_ot_lovywki}\nМощность отраженного сигнала{self.epr_airplane}')
        else:
            self.current_angle = round(t.heading() + 180, 2)
            t4.write(
                f'Расстояние Р-С: {self.current_range} км\nСкорость ракеты: {self.speed_rocket} '
                f'м/с\nСкорость самолета: {self.speed_airplane}\nУгол поворота Р-С: {self.current_angle}\nЭнергопотенциал '
                     f'ловушки :{self.input_energ_ot_lovywki}\nМощность отраженного сигнала: {self.epr_airplane}')



    """РАСЧЕТ МАСШТАБА ДВИЖЕНИЯ"""

    def get_speed_init(self):
        t.color('Red')
        t.forward(self.speed_rocket_mashtab)
        t.color('Red'), t.pendown(), t.hideturtle()
        t.left(self.rocket_sector / 2), t.forward(self.lenght_sector)
        t.left(90), t.circle(self.lenght_sector, - self.rocket_sector)
        t.left(90), t.forward(self.lenght_sector)
        t.left(195), t.penup()
        t2.hideturtle(), t2.forward(self.speed_airplane_mashtab)
        t2.speed(20)
        t2.color('Blue')
        t2.left(self.lov_sector), t2.forward(400), t2.right(270), t2.circle(400, - 2 * self.lov_sector)
        t2.left(90), t2.forward(400), t2.left(self.lov_sector)
        t2.left(self.lov_sector), t2.forward(400), t2.right(270), t2.circle(400, - 2 * self.lov_sector)
        t2.left(90), t2.forward(400), t2.left(self.lov_sector)
        t2.showturtle()
        t.setheading(t.towards(t2.pos()))
        t.showturtle()
        time.sleep(1)
        t4.clear()
        t.clear()
        t2.clear()

    """ТЕКУЩИЕ СЕКТОРА И Кус ЛОВУШКИ В НИХ"""

    def energopot_lov(self):
        if self.current_angle <= float(self.tableWidget.item(1, 0).text().replace(',', '.')) \
                or self.current_angle >= 360 - float(self.tableWidget.item(1, 0).text().replace(',', '.')) \
                or  180 - float(self.tableWidget.item(1, 0).text().replace(',', '.')) <= self.current_angle <= \
                180 + float(self.tableWidget.item(1, 0).text().replace(',', '.')):
            self.G =  10 ** (float(self.tableWidget.item(0, 1).text().replace(',', '.')) / 10)
            self.PxG = float(self.lineEdit.text().replace(',', '.')) * self.G
        elif (float(self.tableWidget.item(2, 0).text().replace(',', '.')) >= self.current_angle >= float(
                self.tableWidget.item(1, 0).text().replace(',', '.'))) \
                or (
                360 - float(self.tableWidget.item(2, 0).text().replace(',', '.')) <= self.current_angle <= 360 - float(
            self.tableWidget.item(1, 0).text().replace(',', '.'))) or \
                (180 + float(self.tableWidget.item(2, 0).text().replace(',', '.')) >= self.current_angle >= 180 + float(
                self.tableWidget.item(1, 0).text().replace(',', '.'))) or \
                (180 - float(self.tableWidget.item(2, 0).text().replace(',', '.')) <= self.current_angle <= 180 - float(
                self.tableWidget.item(1, 0).text().replace(',', '.'))):
            self.G = 10 ** (float(self.tableWidget.item(1, 1).text().replace(',', '.')) / 10)
            self.PxG = float(self.lineEdit.text().replace(',', '.')) * self.G
        elif (float(self.tableWidget.item(3, 0).text().replace(',', '.')) >= self.current_angle >= float(
                self.tableWidget.item(2, 0).text().replace(',', '.'))) \
                or (
                360 - float(self.tableWidget.item(3, 0).text().replace(',', '.')) <= self.current_angle <= 360 - float(
            self.tableWidget.item(2, 0).text().replace(',', '.'))) or \
                (180 + float(self.tableWidget.item(3, 0).text().replace(',', '.')) >= self.current_angle >= 180 + float(
                    self.tableWidget.item(2, 0).text().replace(',', '.'))) or \
                (180 - float(self.tableWidget.item(3, 0).text().replace(',', '.')) <= self.current_angle <= 180 - float(
                    self.tableWidget.item(2, 0).text().replace(',', '.'))):
            self.G = 10 ** (float(self.tableWidget.item(2, 1).text().replace(',', '.')) / 10)
            self.PxG = float(self.lineEdit.text().replace(',', '.')) * self.G
        elif (float(self.tableWidget.item(4, 0).text().replace(',', '.')) >= self.current_angle >= float(
                    self.tableWidget.item(3, 0).text().replace(',', '.'))) \
                    or (
                    360 - float(self.tableWidget.item(4, 0).text().replace(',', '.')) <= self.current_angle <= 360 - float(
                self.tableWidget.item(3, 0).text().replace(',', '.'))) or \
                (180 + float(self.tableWidget.item(4, 0).text().replace(',', '.')) >= self.current_angle >= 180 + float(
                    self.tableWidget.item(3, 0).text().replace(',', '.'))) or \
                (180 - float(self.tableWidget.item(4, 0).text().replace(',', '.')) <= self.current_angle <= 180 - float(
                    self.tableWidget.item(3, 0).text().replace(',', '.'))):
            self.G = 10 ** (float(self.tableWidget.item(3, 1).text().replace(',', '.')) / 10)
            self.PxG = float(self.lineEdit.text().replace(',', '.')) * self.G
        elif (float(self.tableWidget.item(5, 0).text().replace(',', '.')) >= self.current_angle >= float(
                    self.tableWidget.item(4, 0).text().replace(',', '.'))) \
                    or (
                    360 - float(self.tableWidget.item(5, 0).text().replace(',', '.')) <= self.current_angle <= 360 - float(
                self.tableWidget.item(4, 0).text().replace(',', '.'))) or \
                (180 + float(self.tableWidget.item(5, 0).text().replace(',', '.')) >= self.current_angle >= 180 + float(
                    self.tableWidget.item(4, 0).text().replace(',', '.'))) or \
                (180 - float(self.tableWidget.item(5, 0).text().replace(',', '.')) <= self.current_angle <= 180 - float(
                    self.tableWidget.item(4, 0).text().replace(',', '.'))):
            self.G = 10 ** (float(self.tableWidget.item(4, 1).text().replace(',', '.')) / 10)
            self.PxG = float(self.lineEdit.text().replace(',', '.')) * self.G
        else:
            self.PxG = 0
        return self.PxG

    """ЭНЕРГОПОТЕНЦИАЛ ЛОВУШКИ"""
    def get_input_energ_ot_lovywki(self):
        if self.energopot_lov() != 0:
            self.input_energ_lov = 10 * math.log10((self.energopot_lov() * self.G_rocket * (self.Hz
                                     ** 2)) / (((4 * 3.1415) ** 2) *
                                    ((self.current_range * 1000) ** 2)))
        else:
            self.input_energ_lov = 0
        return self.input_energ_lov

    """ТЕКУЩИЕ СЕКТОРА И ЭПР В НИХ"""

    def EPR(self):
        if 60 >= self.current_angle or 300 <= self.current_angle:
            self.epr = float(self.lineEdit_9.text().replace(',', '.'))
        elif 240 >= self.current_angle >= 120:
            self.epr = float(self.lineEdit_11.text().replace(',', '.'))
        else:
            self.epr = float(self.lineEdit_10.text().replace(',', '.'))
        return self.epr

    """ЭНЕРГЕТИКА ОТРАЖЕННОГО СИГНАЛА"""

    def get_input_energ_ot_rocket(self):
        self.rocket_energo = 10 * math.log10((self.P_rocket * (self.G_rocket ** 2) * (self.Hz ** 2) * self.EPR()) / (((4 * 3.1415) ** 3) *
                                                                          ((self.current_range * 1000) ** 4)))
        return round(self.rocket_energo, 1)

    """РАСЧЕТ ЭНЕРГЕТИЧЕСКОГО ЦЕНТРА"""

    def energo_center(self):
        self.center = -(abs(self.input_energ_ot_lovywki) - abs(self.epr_airplane))
        t9.penup()
        t9.goto(450, 0)
        if  self.input_energ_ot_lovywki == 0:
            t9.goto(-100, 0)
        elif self.center > 10:
            t9.goto(-200, 0)
        elif self.center < -10:
            t9.goto(-200, 0)
        else:
            t9.goto(t9.pos()[0] - self.center / 2, 0)

    """ЗАПУСК ФИНАЛЬНОГО УЧАСТКА"""

    def finish(self):
        t2.hideturtle()
        t1.clear(), t1.hideturtle(), t2.clear(), t2.hideturtle(), t5.clear(), t5.hideturtle()
        t6.penup(), t7.penup(), t8.penup(), t9.penup(), t2.pendown(), t5.pendown()
        t6.goto(-100, 0), t6.shapesize(1, 1), t6.showturtle()
        t7.goto(-200, 0), t7.showturtle()
        t8.goto(-150, 0), t8.shape('square'), t8.shapesize(0.1, 5), t8.showturtle()
        t9.goto(-150, 0), t9.shape('circle'), t9.shapesize(0.5, 0.5), t9.showturtle()
        t0.penup(), t0.goto(t9.pos()), t0.color('Grey'), t0.right(270)
        for i in range(8):
            t0.goto(60 * i + t9.pos()[0], t9.pos()[1])
            t0.pendown()
            t0.circle(i * 60, 360)
            t0.write(200 * i)
            t0.penup()
        t1.penup(), t1.pensize(3), t1.goto(-570, 450), t1.pendown(), t1.goto(310, 450), t1.goto(310, -420)
        t1.goto(-570, -420), t1.goto(-570, 450)
        t3.clear(), t3.penup(), t3.goto(-250, 420), t3.write('АЗИМУТ. Масштаб скорости 1:25', font=5)
        t.penup(), t.backward(360 - self.current_range), t.showturtle()
        self.neer_rocket()

    """ПРОВЕРКА ПОПАДАНИЯ РАКЕТЫ В САМОЛЕТ ИЛИ ЛОВУШКУ"""

    def neer_rocket(self):
        self.start_pos_range_km = round((math.sqrt(
            (t.pos()[0] - t9.pos()[0]) ** 2 + (t.pos()[1] - t9.pos()[1]) ** 2)) / 640, 2)
        self.current_range = round(self.start_pos_range_km * 2, 2)
        self.input_energ_ot_lovywki = round(self.get_input_energ_ot_lovywki(), 1)
        self.epr_airplane = self.get_input_energ_ot_rocket()
        if abs(abs(t.pos()[0]) - abs(t6.pos()[0])) * 3 <= 150 and abs(abs(t.pos()[1]) - abs(t6.pos()[1])) * 3 <= 150:
            t0.clear(), t7.hideturtle(), t8.hideturtle(), t9.hideturtle(), t7.clear(), t3.clear(), t3.hideturtle()
            t6.hideturtle(), t.hideturtle(), t.penup(), t. goto(-250, 0), t.write('ПОПАДАНИЕ В САМОЛЕТ', font=8)
            MainWindow.showNormal()
            turtle.done()

        elif abs(abs(t.pos()[0]) - abs(t7.pos()[0])) * 3 <= 150 and abs(abs(t.pos()[1]) - abs(t7.pos()[1])) * 3 <= 150:
            t0.clear(), t7.hideturtle(), t8.hideturtle(), t9.hideturtle(), t7.clear(), t3.clear(), t3.hideturtle()
            t6.hideturtle(), t.hideturtle(), t.penup(), t.goto(-250, 0), t.color('Blue')
            t.write('ПОПАДАНИЕ В ЛОВУШКУ', font=8)
            MainWindow.showNormal()
            turtle.done()

        else:
            self.energo_center()
            self.get_speed_init_near()

    """РАСЧЕТ ТРАЕКТОРИИ ДВИЖЕНИЯ РАКЕТЫ ВБЛИЗИ. ОТРИСОВКА СЕКТОРОВ ЛОВУШКИ """

    def get_speed_init_near(self):
        t.color('Red')
        t.forward(self.speed_rocket_mashtab)
        t.color('Red'), t.pendown(), t.hideturtle()
        t.left(self.rocket_sector / 2), t.forward(self.lenght_sector)
        t.left(90), t.circle(self.lenght_sector, - self.rocket_sector)
        t.left(90), t.forward(self.lenght_sector)
        t.left(195), t.penup()
        t7.color('Blue')
        t7.pendown(), t7.hideturtle()
        t7.left(self.lov_sector), t7.forward(400), t7.right(270), t7.circle(400, - 2 * self.lov_sector)
        t7.left(90), t7.forward(400), t7.left(self.lov_sector)
        t7.left(self.lov_sector), t7.forward(400), t7.right(270), t7.circle(400, - 2 * self.lov_sector)
        t7.left(90), t7.forward(400), t7.left(self.lov_sector)
        t7.showturtle()
        t.setheading(t.towards(t9.pos()))
        t.showturtle()
        time.sleep(1)
        t4.clear()
        t.clear()
        t2.clear()
        t.clear()
        t2.clear()
        self.get_trace()
        self.neer_rocket()





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
