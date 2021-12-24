import sys
from mysql.connector import connect, Error
from PyQt5 import QtCore, QtGui, QtWidgets
class WindowConnect(object):
    def ConnDB(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 265)
        self.lineHost = QtWidgets.QLineEdit(Form)
        self.lineHost.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.lineHost.setObjectName("lineHost")
        self.lineUser = QtWidgets.QLineEdit(Form)
        self.lineUser.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.lineUser.setObjectName("lineUser")
        self.linePass = QtWidgets.QLineEdit(Form)
        self.linePass.setGeometry(QtCore.QRect(20, 130, 113, 20))
        self.linePass.setObjectName("linePass")
        self.lineDB = QtWidgets.QLineEdit(Form)
        self.lineDB.setGeometry(QtCore.QRect(20, 180, 113, 20))
        self.lineDB.setObjectName("lineDB")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.ConnectButton = QtWidgets.QPushButton(Form)


        self.buttoncon = QtWidgets.QPushButton(Form)
        self.buttoncon.setText("DFSSFSD")
        self.buttoncon.setGeometry(QtCore.QRect(100, 220, 75, 23))

        self.ConnectButton.setGeometry(QtCore.QRect(20, 220, 75, 23))
        self.ndicatorDB = QtWidgets.QLabel(Form)
        self.ndicatorDB.setGeometry(QtCore.QRect(170, 110, 171, 16))
        self.ndicatorDB.setObjectName("ndicatorDB")
        Form.setWindowTitle("Connect to Database")
        self.label.setText("host")
        self.label_2.setText("login")
        self.label_3.setText("password")
        self.label_4.setText("name DB")
        self.ConnectButton.setText("CONNECT")
        self.ndicatorDB.setText("INDICATOR")

class OtherWindow(object):
    def Detail(self, Window):
        Window.resize(400, 300)
        self.Layout = QtWidgets.QWidget(Window)
        self.fioLabel = QtWidgets.QLabel(self.Layout)
        self.fioLabel = QtWidgets.QLabel(self.Layout)
        self.ClientLayout = QtWidgets.QFormLayout()
        self.ClientLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fioLabel)
    def graph1(self, Form2):
        import test
        Form2.setObjectName("Graphic")
        Form2.resize(760, 422)
        self.label = QtWidgets.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 411))
        self.label.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Form2)
        Form2.setWindowTitle("Form")
        self.label.setText("<html><head/><body><p><img src=\":/newPrefix/2021-12-23_01-42-59.png\"/></p></body></html>")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 399)
        self.centralwidgetLayout = QtWidgets.QWidget(MainWindow)
        self.centralwidgetLayout.setObjectName("centralwidgetLayout")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidgetLayout)
        self.gridLayout.setObjectName("gridLayout")
        self.ClientLayout = QtWidgets.QFormLayout()
        self.ClientLayout.setObjectName("ClientLayout")
        self.fioLabel = QtWidgets.QLabel(self.centralwidgetLayout)
        self.fioLabel.setObjectName("fioLabel")
        self.ClientLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fioLabel)
        self.fioLine = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.fioLine.setObjectName("fioLine")
        self.ClientLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fioLine)
        self.emailLabel = QtWidgets.QLabel(self.centralwidgetLayout)
        self.emailLabel.setObjectName("emailLabel")
        self.ClientLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        self.emailLine = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.emailLine.setObjectName("emailLine")
        self.ClientLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.emailLine)
        self.phoneLabel = QtWidgets.QLabel(self.centralwidgetLayout)
        self.phoneLabel.setObjectName("phoneLabel")
        self.ClientLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phoneLabel)
        self.phoneLine = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.phoneLine.setObjectName("phoneLine")
        self.ClientLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phoneLine)
        self.gridLayout.addLayout(self.ClientLayout, 2, 0, 1, 1)
        self.LayoutData = QtWidgets.QGridLayout()
        self.LayoutData.setObjectName("LayoutData")
        self.comboBoxRisk = QtWidgets.QComboBox(self.centralwidgetLayout)
        self.comboBoxRisk.addItem("")
        self.comboBoxRisk.addItem("Высокий")
        self.comboBoxRisk.addItem("Средний")
        self.comboBoxRisk.addItem("Низкий")
        self.comboBoxRisk.currentIndexChanged.connect(self.addComboStrategy)
        self.LayoutData.addWidget(self.comboBoxRisk, 0, 1, 1, 1)
        self.labelRisk = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelRisk.setObjectName("labelRisk")
        self.LayoutData.addWidget(self.labelRisk, 0, 0, 1, 1)
        self.comboBoxStrategy = QtWidgets.QComboBox(self.centralwidgetLayout)
        self.comboBoxStrategy.currentIndexChanged.connect(self.change)
        self.LayoutData.addWidget(self.comboBoxStrategy, 2, 1, 1, 1)
        self.lineDuration = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.lineDuration.setObjectName("lineDuration")
        self.LayoutData.addWidget(self.lineDuration, 6, 3, 1, 1)
        self.labelSrokDeystviya = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelSrokDeystviya.setObjectName("labelSrokDeystviya")
        self.LayoutData.addWidget(self.labelSrokDeystviya, 6, 2, 1, 1)
        self.labelStrategy = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelStrategy.setObjectName("labelStrategy")
        self.LayoutData.addWidget(self.labelStrategy, 2, 0, 1, 1)
        self.riskDetailButton = QtWidgets.QPushButton(self.centralwidgetLayout)
        self.riskDetailButton.setObjectName("riskDetailButton")
        self.riskDetailButton.clicked.connect(self.showDetail)
        self.LayoutData.addWidget(self.riskDetailButton, 0, 2, 1, 1)
        self.labelSumInvest = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelSumInvest.setObjectName("labelSumInvest")
        self.LayoutData.addWidget(self.labelSumInvest, 4, 0, 1, 1)
        self.lineSumInvest = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.lineSumInvest.setObjectName("lineSumInvest")
        self.LayoutData.addWidget(self.lineSumInvest, 4, 1, 1, 1)
        self.labelPercentDohod_2 = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelPercentDohod_2.setObjectName("labelPercentDohod_2")
        self.LayoutData.addWidget(self.labelPercentDohod_2, 6, 0, 1, 1)
        self.labelMinSum_2 = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelMinSum_2.setObjectName("labelMinSum_2")
        self.LayoutData.addWidget(self.labelMinSum_2, 3, 0, 1, 1)
        self.labelMinSumOutput = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelMinSumOutput.setObjectName("labelMinSumOutput")
        self.LayoutData.addWidget(self.labelMinSumOutput, 3, 1, 1, 1)
        self.GraphicButton = QtWidgets.QPushButton(self.centralwidgetLayout)

        self.GraphicButton.clicked.connect(self.showGraphic)

        self.LayoutData.addWidget(self.GraphicButton, 2, 2, 1, 1)
        self.labelPercentDohod = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelPercentDohod.setObjectName("labelPercentDohod")
        self.LayoutData.addWidget(self.labelPercentDohod, 6, 1, 1, 1)
        self.gridLayout.addLayout(self.LayoutData, 3, 0, 1, 1)
        self.ButtonConnect = QtWidgets.QPushButton(self.centralwidgetLayout)

        self.ButtonConnect.clicked.connect(self.connect_database)

        self.gridLayout.addWidget(self.ButtonConnect, 0, 1, 1, 1)
        self.AddButton = QtWidgets.QPushButton(self.centralwidgetLayout)
        self.AddButton.clicked.connect(self.addDataBase)

        self.gridLayout.addWidget(self.AddButton, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelindicator = QtWidgets.QLabel(self.centralwidgetLayout)
        self.gridLayout.addWidget(self.labelindicator, 4, 0, 1, 1)
        #.ClientLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelindicator)
        self.gridLayout.addLayout(self.ClientLayout, 2, 0, 1, 1)
        self.LayoutConnDB = QtWidgets.QGridLayout()
        self.lineHost = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.lineHost.setObjectName("lineHost")
        self.LayoutConnDB.addWidget(self.lineHost, 0, 1, 1, 1)
        self.labelUser = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelUser.setObjectName("labelUser")
        self.LayoutConnDB.addWidget(self.labelUser, 1, 0, 1, 1)
        self.labelHost = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelHost.setObjectName("labelHost")
        self.LayoutConnDB.addWidget(self.labelHost, 0, 0, 1, 1)
        self.linePass = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.linePass.setObjectName("linePass")
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LayoutConnDB.addWidget(self.linePass, 2, 1, 1, 1)
        self.lineUser = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.lineUser.setObjectName("lineUser")
        self.LayoutConnDB.addWidget(self.lineUser, 1, 1, 1, 1)
        self.lineDataBase = QtWidgets.QLineEdit(self.centralwidgetLayout)
        self.lineDataBase.setObjectName("lineDataBase")
        self.LayoutConnDB.addWidget(self.lineDataBase, 3, 1, 1, 1)
        self.labelPass = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelPass.setObjectName("labelPass")
        self.LayoutConnDB.addWidget(self.labelPass, 2, 0, 1, 1)
        self.labelDataBase = QtWidgets.QLabel(self.centralwidgetLayout)
        self.labelDataBase.setObjectName("labelDataBase")
        self.LayoutConnDB.addWidget(self.labelDataBase, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.LayoutConnDB, 2, 1, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(True)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidgetLayout)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showDetail(self):
        self.w = QtWidgets.QWidget()
        ui = OtherWindow()
        ui.Detail(self.w)
        if self.comboBoxStrategy.currentText()=="Видеоигры":
            ui.fioLabel.setText("Инвестирование в рост компаний игровой отрасли с диверсификацией\n"
                                "по странам (США,Китай, Япония) и профилю компаний (программное обеспечение, оборудование, онлайн-платформы и т.д.)")
        if self.comboBoxStrategy.currentText()=="Рублевые облигации":
            ui.fioLabel.setText("Инвестирование в рост компаний игровой отрасли с диверсификацией\n"
                                "по странам (США,Китай, Япония) и профилю компаний (программное обеспечение, оборудование, онлайн-платформы и т.д.)")
        if self.comboBoxStrategy.currentText() == "Еврооблигации":
            ui.fioLabel.setText("Инвестирование в рост компаний игровой отрасли с диверсификацией\n"
                                "по странам (США,Китай, Япония) и профилю компаний (программное обеспечение, оборудование, онлайн-платформы и т.д.)")
            #ui.fioLabel.set
        self.w.show()
       # w.exec_()
    def addComboStrategy(self):
        self.comboBoxStrategy.clear()
        if self.comboBoxRisk.currentText()=="Средний":
            self.comboBoxStrategy.addItem("Видеоигры")
            self.comboBoxStrategy.addItem("Технологии 100")
            self.comboBoxStrategy.addItem("Китайские акции")
        if self.comboBoxRisk.currentText()=="Низкий":
            self.comboBoxStrategy.addItem("Еврооблигации")
            self.comboBoxStrategy.addItem("Долларовые облигации")
        if self.comboBoxRisk.currentText()=="Высокий":
            self.comboBoxStrategy.addItem("Рублевые облигации")
    def addDataBase(self):
        insert_knownFace_query = "INSERT INTO db.doverapp (id, fio, email, phone_number, risk_level, strategy) VALUES ( %s, %s, %s, %s, %s, %s )"
        selectLastId = "SELECT id FROM db.doverapp ORDER BY id DESC LIMIT 1" #select last ID in DB
        cursor = conn.cursor()
        cursor.execute(selectLastId)
        _id = 0
        for row in cursor:
            _id = row[0]+1
        _fio = self.fioLine.text()
        _email = self.emailLine.text()
        _phone = self.phoneLine.text()
        _risk = self.comboBoxRisk.currentText()
        _strategy = self.comboBoxStrategy.currentText()
        knownFace_records = (_id, _fio, _email, _phone, _risk, _strategy)
        try:
            cursor.execute(insert_knownFace_query, knownFace_records)
            conn.commit()
            self.labelindicator.setText("CORRECT addition")
        except Error as er:
            self.labelindicator.setText(str(er))
        self.fioLine.clear()
        self.emailLine.clear()
        self.phoneLine.clear()
        self.lineSumInvest.clear()
        self.lineDuration.clear()
        self.comboBoxRisk.setCurrentIndex(0)
        self.labelMinSumOutput.clear()
        self.labelPercentDohod.clear()
    #def showWindowConnect(self):
     #   self.WinCon = QtWidgets.QWidget()
      #  ui2 = WindowConnect()
       # ui2.ConnDB(self.WinCon)
        #ui2.ConnectButton.clicked.connect(ui2.connect_database)
       # self.WinCon.show()

    def showGraphic(self):
        self.WinGraph = QtWidgets.QWidget()
        ui3 = OtherWindow()
        ui3.graph1(self.WinGraph)
        if self.comboBoxStrategy.currentText()=="Видеоигры":
            ui3.label.setText("<html><head/><body><p><img src=\":/newPrefix/2.png\"/></p></body></html>")
        if self.comboBoxStrategy.currentText()=="Еврооблигации":
            ui3.label.setText("<html><head/><body><p><img src=\":/newPrefix/3.png\"/></p></body></html>")
        self.WinGraph.show()
    def connect_database(self):
        global conn
        try:
            conn = connect(host=self.lineHost.text(),
                           user=self.lineUser.text(),  # input("Имя пользователя: )"
                           password=self.linePass.text(),  # getpass("Пароль ")
                           database=self.lineDataBase.text(),
                           auth_plugin='mysql_native_password')
            self.labelindicator.setText("CORRECT\n" + str(conn))  # print("CORRECT",conn) #input("DB: ")
        except Error as e:
            self.labelindicator.setText("Connection DB error\n" + str(e))
    def change(self):
        if self.comboBoxStrategy.currentText()=="Видеоигры":
            self.labelPercentDohod.setText("15,9%")
            self.labelMinSumOutput.setText("200 руб")
        elif self.comboBoxStrategy.currentText()=="Технологии 100":
            self.labelPercentDohod.setText("12,72%")
            self.labelMinSumOutput.setText("300$")
        elif self.comboBoxStrategy.currentText()=="Китайские акции":
            self.labelPercentDohod.setText("12,6%")
            self.labelMinSumOutput.setText("200 руб")
        elif self.comboBoxStrategy.currentText()=="Еврооблгации":
            self.labelPercentDohod.setText("15,8%")
            self.labelMinSumOutput.setText("300$")
        elif self.comboBoxStrategy.currentText()=="Долларовые облигации":
            self.labelPercentDohod.setText("6,9%")
            self.labelMinSumOutput.setText("5000$")
        elif self.comboBoxStrategy.currentText()=="Рублевые облигации":
            self.labelPercentDohod.setText("3,9%")
            self.labelMinSumOutput.setText("200 руб")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fioLabel.setText(_translate("MainWindow", "ФИО"))
        self.emailLabel.setText(_translate("MainWindow", "Email"))
        self.phoneLabel.setText(_translate("MainWindow", "Номер телефона"))
       # self.comboBoxRisk.setItemText(0, _translate("MainWindow", "Высокий"))
       # self.comboBoxRisk.setItemText(1, _translate("MainWindow", "Средний"))
       # self.comboBoxRisk.setItemText(2, _translate("MainWindow", "Низкий"))
       # self.comboBoxRisk.setItemText(3, _translate("MainWindow", "Консервативный"))
        self.labelRisk.setText(_translate("MainWindow", "Уровень риска"))
        self.labelSrokDeystviya.setText(_translate("MainWindow", "Срок действия"))
        self.labelStrategy.setText(_translate("MainWindow", "Стратегия"))
        self.riskDetailButton.setText(_translate("MainWindow", "Подробнее"))
        self.labelSumInvest.setText(_translate("MainWindow", "Сумма инвестирования"))
        self.labelPercentDohod_2.setText(_translate("MainWindow", "Ожидаемая доходность"))
        self.labelMinSum_2.setText(_translate("MainWindow", "Минимальная сумма"))
        self.labelMinSumOutput.setText(_translate("MainWindow", "."))
        self.GraphicButton.setText(_translate("MainWindow", "График"))
        self.labelPercentDohod.setText(_translate("MainWindow", "."))
        self.ButtonConnect.setText(_translate("MainWindow", "Подключение к БД"))
        self.AddButton.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.label.setText(_translate("MainWindow", "Доверительное управление имуществом"))
        self.labelindicator.setText(_translate("MainWindow", "Indicator"))
        self.labelUser.setText(_translate("MainWindow", "user"))
        self.labelHost.setText(_translate("MainWindow", "localhost"))
        self.labelPass.setText(_translate("MainWindow", "password"))
        self.labelDataBase.setText(_translate("MainWindow", "database"))




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
