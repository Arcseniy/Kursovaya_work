import pypyodbc as p

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)

connection = p.connect(
    'DRIVER={SQL Server};SERVER=vm-as35.staff.corp.local;''DATABASE=kursach_2022_ne_trogayte_plz_125;UID=student;PWD=sql2020')

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class Ui_Form(QMainWindow):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1042, 792)
        Form.setStyleSheet("background-color: rgba(218, 231, 230, 1);")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(170, 280, 721, 501))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(300, 140, 451, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setToolTip("При вводе данных, записывайте поля через знак ',',"
                                 "строковые значения в '', а даты в формате: 'YYYY-MM-DD'")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(410, 20, 256, 51))
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(670, 180, 77, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 1, 0, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout.addWidget(self.pushButton1, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(300, 180, 104, 56))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox1 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(255, 255, 255);")
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.verticalLayout.addWidget(self.comboBox1)
        self.comboBox2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border-color: rgb(255, 255, 255);")
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.verticalLayout.addWidget(self.comboBox2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.tableWidget.clear()
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("Form", "FID"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("Form", "Nationality"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("Form", "Birthday"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("Form", "New Column"))
        # item = self.tableWidget.horizontalHeaderItem(4)
        # item.setText(_translate("Form", "Name"))
        # item = self.tableWidget.horizontalHeaderItem(5)
        # item.setText(_translate("Form", "MiddleName"))
        # item = self.tableWidget.horizontalHeaderItem(6)
        # item.setText(_translate("Form", "LastName"))
        # item = self.tableWidget.horizontalHeaderItem(7)
        # item.setText(_translate("Form", "Role"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:24pt; color:#a2a2a2;\">FOOTBALL TEAM</span></p></body></html>"))

        self.pushButton2.setText(_translate("Form", "DELETE"))
        self.pushButton2.clicked.connect(self.delete_data_from_footballer)
        self.pushButton1.setText(_translate("Form", "ADD"))
        self.pushButton1.clicked.connect(self.add_data_to_footballer)
        self.comboBox1.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.comboBox1.setItemText(0, _translate("Form", "Список таблиц"))
        self.comboBox1.setItemText(1, _translate("Form", "Footballer"))
        self.comboBox1.setItemText(2, _translate("Form", "Injury"))
        self.comboBox1.setItemText(3, _translate("Form", "Trainer"))
        self.comboBox1.setItemText(4, _translate("Form", "Training"))
        self.comboBox1.setItemText(5, _translate("Form", "Competiton"))
        self.comboBox1.setItemText(6, _translate("Form", "Stadion"))
        self.comboBox1.setItemText(7, _translate("Form", "Match"))
        self.comboBox1.setItemText(8, _translate("Form", "Statistic"))
        self.comboBox1.setItemText(9, _translate("Form", "Trainer_SquadForTheMatch"))
        self.comboBox1.setItemText(10, _translate("Form", "Footballer_SquadForTheMatch"))
        self.comboBox1.setItemText(11, _translate("Form", "SquadForTheMatch"))
        self.comboBox1.setItemText(12, _translate("Form", "Footballer_Training"))
        self.comboBox2.setItemText(0, _translate("Form", "Список запросов"))
        self.comboBox2.setItemText(1, _translate("Form", "Травмированные игроки"))
        self.comboBox2.setItemText(2, _translate("Form", "Информация о матче"))
        self.comboBox2.setItemText(3, _translate("Form", "Информация о матче"))
        self.comboBox2.setItemText(4, _translate("Form", "Информация о матче"))
        self.comboBox2.setItemText(5, _translate("Form", "Информация о матче"))
        self.comboBox1.activated.connect(self.do_something1)
        self.comboBox2.activated.connect(self.do_something2)

    def do_something1(self):
        if self.comboBox1.currentText() == "Footballer":
            self.Footballer()
        elif self.comboBox1.currentText() == "Injury":
            self.Injury()
        else:
            self.tableWidget.clear()

    def do_something2(self):
        if self.comboBox2.currentText() == "Травмированные игроки":
            self.query_1()
        elif self.comboBox2.currentText() == "Информация о матче":
            self.query_2()
        else:
            self.tableWidget.clear()

    def Footballer(self):
        self.view_data("Footballer", 8, 30,
                       ["FID", "Nationality", "Birthday", "Name",
                        "MiddleName", "LastName", "IID",
                        "Role"])

    def Injury(self):
        self.view_data("Injury", 5, 4,
                       ["IID", "DateOfInjury", "RecoveryPeriod", "CanStartTraining", "Diagnosis"])

    def query_1(self):
        cursor = connection.cursor()
        cursor.execute("SELECT FID as [Айди футболсита], Name as [Имя], MiddleName as [Отчество], LastName as [Фамилия] "
                    "FROM dbo.Footballer WHERE IID IS NOT NULL")
        row = cursor.fetchone()
        tablerow = 0
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(3)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setHorizontalHeaderLabels(["Айди футболиста", "Имя", "Отчество", "Фамилия"])
        while row is not None:
            for i in range(4):
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            row = cursor.fetchone()
            tablerow += 1

    def query_2(self):
        cursor = connection.cursor()
        cursor.execute("SELECT [Match].MID as [Айди матча], [SquadForTheMatch].SID as [Номер состава], "
                    "CAST([Match].[Date] as DATE) as [Дата матча], "
                    "CAST([Match].[Time] as TIME) as [Время начала матча], "
                    "[Stadion].StadionName as [Место проведения матча], "
                    "[Competition].CompetitionName as [Название соревнования] "
                    "FROM ([Match] INNER JOIN Stadion on [Match].StadID = Stadion.StadID "
                    "INNER JOIN Competition on [Match].CID = Competition.CID "
                    "INNER JOIN SquadForTheMatch on [Match].SID = SquadForTheMatch.SID)")
        row = cursor.fetchone()
        tablerow = 0
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(3)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setHorizontalHeaderLabels(["Айди матча", "Номер состава", "Дата матча",
                                                    "Время начала матча", "Место проведения матча",
                                                    "Название соревнования"])
        while row is not None:
            for i in range(6):
                self.tableWidget.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            row = cursor.fetchone()
            tablerow += 1

    def add_data_to_footballer(self):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Footballer(FID, Nationality, Birthday, Name, MiddleName, LastName, IID, Role) VALUES "
                    "(%s)" % self.lineEdit.text())
        QMessageBox.about(self, 'Connection', 'Данные добавлены в таблицу!')
        cursor.commit()
        self.update()
        # QMessageBox.about(self, 'Connection', 'Ошибка при вводе данных, проверьте формат!')

    def delete_data_from_footballer(self):
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM Footballer WHERE FID = {int(self.lineEdit.text())}")
        QMessageBox.about(self, 'Connection', f'Строка с FID = {self.lineEdit.text()} удалена!')
        cursor.commit()
        self.update()

    def view_data(self, Name, Column, Row, Head):
        cursor = connection.cursor()
        cursor.execute(f'select * from {Name}')
        row = cursor.fetchone()
        tablerow = 0
        self.tableWidget.setColumnCount(Column)
        self.tableWidget.setRowCount(Row)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setHorizontalHeaderLabels(Head)
        while row is not None:
            for i in range(Column):
                self.tableWidget.setItem(tablerow, i,
                                         QtWidgets.QTableWidgetItem(str(row[i])))
            row = cursor.fetchone()
            tablerow += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
