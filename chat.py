# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(604, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/chat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout_2.addWidget(self.textEdit_2, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #A11F42;\n"
"  font-size: 20px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"  border-width: 1px;\n"
"  border-color: #76797C;\n"
"  border-style: solid;\n"
"  padding: 5px;\n"
"  border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #f4efd2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #EB5C74;\n"
"}\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icon/right-arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 4)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #A11F42;\n"
"  font-size: 20px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"  border-width: 1px;\n"
"  border-color: #76797C;\n"
"  border-style: solid;\n"
"  padding: 5px;\n"
"  border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #f4efd2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #EB5C74;\n"
"}\n"
""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icon/computer-monitor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(23, 23))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.gridLayout_3.addLayout(self.formLayout, 1, 0, 1, 3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 3, 2, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icon/chawt.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cooper Black"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.textEdit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat", None))
        self.label_6.setText(_translate("MainWindow", "Send Message :", None))
        self.pushButton_2.setText(_translate("MainWindow", "Send", None))
        self.label_3.setText(_translate("MainWindow", "Name : ", None))
        self.label_4.setText(_translate("MainWindow", "IP :", None))
        self.label_5.setText(_translate("MainWindow", "Port :", None))
        self.pushButton.setText(_translate("MainWindow", "Connect", None))
        self.label_7.setText(_translate("MainWindow", "Recv Message :", None))
        self.label.setText(_translate("MainWindow", "Chat", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

