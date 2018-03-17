# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import item,main,os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 493)
        self.history = ['/']
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 50, 531, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.itemsView = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.itemsView.setObjectName("itemsView")
        self.itemsView.clicked.connect(self.tableClicked)
        self.verticalLayout.addWidget(self.itemsView)
        self.favoriteView = QtWidgets.QTableView(self.centralwidget)
        self.favoriteView.setGeometry(QtCore.QRect(0, 50, 161, 381))
        self.favoriteView.setObjectName("FavoriteView")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.insertPlainText('hamidreza')
        self.textEdit.setGeometry(QtCore.QRect(170, 10, 401, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.onClickGoTo)
        #self.pushButton.clicked.connect("kose nanat",self)
        self.pushButton.setGeometry(QtCore.QRect(580, 10, 110, 32))
       # self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton('back',self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 10, 110, 32))
        self.pushButton_2.clicked.connect(self.onClickBack)
        #self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showDirectoryContent(self,item_list):
        self.itemsView.setRowCount(len(item_list))
        self.itemsView.setColumnCount(2)
        self.itemsView.autoFillBackground()
        fileIcon = QtGui.QIcon(QtGui.QPixmap("fileIcon.png"))
        folderIcon = QtGui.QIcon(QtGui.QPixmap("folderIcon.png"))
        for i in range(len(item_list)):
            icon = fileIcon
            if os.path.isdir(item_list[i].path+"/"+item_list[i].name):
                icon = folderIcon
            self.itemsView.setItem(i, 0, QTableWidgetItem(icon,item_list[i].name))
            self.itemsView.setItem(i,1 , QTableWidgetItem(item_list[i].date))
        self.itemsView.move(0,0)
    def tableClicked(self,itemm):
        if main.current_path == '/':
            main.current_path += str(itemm.data())
        else:
            main.current_path += '/'+str(itemm.data())
        if os.path.isdir(main.current_path):
            main.file_list=item.getItemList(main.current_path)
            self.showDirectoryContent(main.file_list)
            self.history.append(main.current_path)
        else:
            os.system("open "+ main.current_path)
            main.current_path = self.history[-1]


    def onClickBack(self,MainWindow):
        self.history.pop()
        main.current_path = self.history[-1]
        main.file_list = item.getItemList(main.current_path)
        self.showDirectoryContent(main.file_list)
        self.textEdit.setText(main.current_path)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter Directory</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Go to"))
        self.pushButton_2.setText(_translate("MainWindow", "Back"))
        self.textEdit.setText(main.current_path)
    def onClickGoTo(self,MainWindow):
        mytext = self.textEdit.toPlainText()
        main.current_path = mytext
        if os.path.isdir(mytext):
            main.file_list=item.getItemList(mytext)
            self.showDirectoryContent(main.file_list)
            self.history.append(main.current_path)
        else:
            os.system("open "+ main.current_path)
            main.current_path = self.history[-1]



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #default path show

    ui.setupUi(MainWindow)
    ui.showDirectoryContent(main.file_list)

    MainWindow.show()
    #print(main.current_path)
    sys.exit(app.exec_())

