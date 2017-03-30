# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lockscreen.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserText(object):
    def setupUi(self, UserText):
        UserText.setObjectName("UserText")
        UserText.resize(400, 388)
        UserText.setStyleSheet("background-color: rgb(44, 0, 30);")
        self.login = QtWidgets.QPushButton(UserText)
        self.login.setGeometry(QtCore.QRect(179, 350, 75, 27))
        self.login.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Big John\";")
        self.login.setObjectName("login")
        
        self.login.clicked.connect(self.Login)
        
        self.line = QtWidgets.QFrame(UserText)
        self.line.setGeometry(QtCore.QRect(250, 140, 140, 3))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("background-color: rgb(174, 167, 159);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fuzzysystem = QtWidgets.QLabel(UserText)
        self.fuzzysystem.setGeometry(QtCore.QRect(40, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Peace Sans")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fuzzysystem.setFont(font)
        self.fuzzysystem.setStyleSheet("font: 24pt \"Peace Sans\";")
        self.fuzzysystem.setObjectName("fuzzysystem")
        self.message = QtWidgets.QLabel(UserText)
        self.message.setGeometry(QtCore.QRect(100, 330, 221, 20))
        self.message.setStyleSheet("font: 10pt \"Ubuntu Mono\";\n"
"color: rgb(255, 0, 0);")
        self.message.setObjectName("message")

        self.message.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.layoutWidget = QtWidgets.QWidget(UserText)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 150, 171, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.date_icon = QtWidgets.QLabel(self.layoutWidget)
        self.date_icon.setEnabled(False)
        self.date_icon.setObjectName("date_icon")
        self.horizontalLayout.addWidget(self.date_icon)
        self.date = QtWidgets.QLabel(self.layoutWidget)
        self.date.setStyleSheet("font: 12pt \"Ubuntu\";\n"
"color: rgb(174, 167, 159);")
        self.date.setText("")
        self.date.setObjectName("date")

        self.date.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(1000)
        self.timer2.timeout.connect(self.Date)
        self.timer2.start()
        
        self.horizontalLayout.addWidget(self.date)
        self.layoutWidget1 = QtWidgets.QWidget(UserText)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 250, 273, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.username_icon = QtWidgets.QLabel(self.layoutWidget1)
        self.username_icon.setObjectName("username_icon")
        self.horizontalLayout_3.addWidget(self.username_icon)
        self.username = QtWidgets.QLabel(self.layoutWidget1)
        self.username.setStyleSheet("color: rgb(233, 84, 32);\n"
"font: 75 11pt \"Moon\";")
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.usertext = QtWidgets.QLineEdit(self.layoutWidget1)
        self.usertext.setStyleSheet("color: rgb(174, 167, 159);\n"
"background-color: rgb(44, 0, 30);\n"
"selection-background-color: rgb(85, 170, 255);\n"
"border: none")
        self.usertext.setPlaceholderText("Enter Username")
        self.usertext.setObjectName("usertext")

        self.usertext.setMaxLength(10)
        
        self.horizontalLayout_3.addWidget(self.usertext)
        self.layoutWidget2 = QtWidgets.QWidget(UserText)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 290, 278, 34))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.password_icon = QtWidgets.QLabel(self.layoutWidget2)
        self.password_icon.setObjectName("password_icon")
        self.horizontalLayout_4.addWidget(self.password_icon)
        self.password = QtWidgets.QLabel(self.layoutWidget2)
        self.password.setStyleSheet("color: rgb(233, 84, 32);\n"
"font: 25 11pt \"Moon\";")
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.passtext = QtWidgets.QLineEdit(self.layoutWidget2)
        self.passtext.setStyleSheet("color: rgb(174, 167, 159);\n"
"background-color: rgb(44, 0, 30);\n"
"selection-background-color: rgb(85, 170, 255);\n"
"border: none")
        self.passtext.setPlaceholderText("Enter Password")
        
        self.passtext.setObjectName("passtext")

        self.passtext.setMaxLength(10)
        self.passtext.setEchoMode(2)
        
        self.horizontalLayout_4.addWidget(self.passtext)
        self.layoutWidget3 = QtWidgets.QWidget(UserText)
        self.layoutWidget3.setGeometry(QtCore.QRect(290, 100, 101, 34))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.time_icon = QtWidgets.QLabel(self.layoutWidget3)
        self.time_icon.setObjectName("time_icon")
        self.horizontalLayout_5.addWidget(self.time_icon)
        self.time = QtWidgets.QLabel(self.layoutWidget3)
        self.time.setStyleSheet("font: 18pt \"Ubuntu\";\n"
"color: rgb(174, 167, 159);")
        self.time.setText("")
        self.time.setObjectName("time")
        
        self.time.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(1000)
        self.timer1.timeout.connect(self.Time)
        self.timer1.start()

        self.horizontalLayout_5.addWidget(self.time)
        self.layoutWidget.raise_()
        self.login.raise_()
        self.line.raise_()
        self.fuzzysystem.raise_()
        self.message.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(UserText)
        QtCore.QMetaObject.connectSlotsByName(UserText)

    def retranslateUi(self, UserText):
        _translate = QtCore.QCoreApplication.translate
        UserText.setWindowTitle(_translate("UserText", "Dialog"))
        self.login.setText(_translate("UserText", "Login"))
        self.fuzzysystem.setText(_translate("UserText", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#e95420;\">FUZZY SYSTEM</span></p></body></html>"))
        self.message.setText(_translate("UserText", "<html><head/><body><p><br/></p></body></html>"))
        self.date_icon.setText(_translate("UserText", "<html><head/><body><p><img src=\":/icons/Icons/calendar.png\"/></p></body></html>"))
        self.username_icon.setText(_translate("UserText", "<html><head/><body><p><img src=\":/icons/Icons/user.png\"/></p></body></html>"))
        self.username.setText(_translate("UserText", "Username :"))
        self.usertext.setToolTip(_translate("UserText", "<html><head/><body><p><br/></p></body></html>"))
        self.password_icon.setText(_translate("UserText", "<html><head/><body><p><img src=\":/icons/Icons/door-key.png\"/></p></body></html>"))
        self.password.setText(_translate("UserText", "Password :"))
        self.time_icon.setText(_translate("UserText", "<html><head/><body><p><img src=\":/icons/Icons/clock.png\"/></p></body></html>"))

    def Time(self):
        self.time.setText(QtCore.QTime.currentTime().toString("hh:mm"))

    def Date(self):
        self.date.setText(QtCore.QDate.currentDate().toString())
        
    def Login(self):
        username = self.usertext.text()
        password = self.passtext.text()
        allow = ['kunal', 'kamran', 'vidya']
        if(username.lower() == "fyp2017" and password.lower() in allow):
            self.message.setText("Access Granted")
        else:
            self.message.setText("Wrong Password! Try Again")


import lockscreen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserText = QtWidgets.QDialog()
    ui = Ui_UserText()
    ui.setupUi(UserText)
    UserText.show()
    sys.exit(app.exec_())
