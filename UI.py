# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow,QMessageBox, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QAbstractItemView,QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import item,main,os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 503)
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
        self.itemsView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.itemsView.doubleClicked.connect(self.tableClicked)
        self.verticalLayout.addWidget(self.itemsView)
        self.favoriteView = QtWidgets.QTableView(self.centralwidget)
        self.favoriteView.setGeometry(QtCore.QRect(0, 50, 161, 381))
        self.favoriteView.setObjectName("FavoriteView")
        self.directoryTextView = QtWidgets.QTextEdit(self.centralwidget)
        self.directoryTextView.insertPlainText('hamidreza')
        self.directoryTextView.setGeometry(QtCore.QRect(170, 10, 401, 31))
        self.directoryTextView.setObjectName("directoryTextView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.onClickGoTo)
        #self.pushButton.clicked.connect("kose nanat",self)
        self.pushButton.setGeometry(QtCore.QRect(580, 10, 110, 32))
       # self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton('back',self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 10, 110, 32))
        self.pushButton_2.clicked.connect(self.onClickBack)
        self.newFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.newFolderButton.setGeometry(QtCore.QRect(170, 430, 110, 32))
        self.newFolderButton.setObjectName("newFolderButton")
        self.newFolderButton.setText("New Folder")
        self.copyButton = QtWidgets.QPushButton(self.centralwidget)
        self.copyButton.setGeometry(QtCore.QRect(300, 430, 110, 32))
        self.copyButton.setObjectName("copyButton")
        self.copyButton.setText("Copy")
        self.cutButton = QtWidgets.QPushButton(self.centralwidget)
        self.cutButton.setGeometry(QtCore.QRect(430, 430, 110, 32))
        self.cutButton.setObjectName("cutButton")
        self.cutButton.setText("Cut")
        self.pasteButton = QtWidgets.QPushButton(self.centralwidget)
        self.pasteButton.setGeometry(QtCore.QRect(550, 430, 110, 32))
        self.pasteButton.setObjectName("pasteButton")
        self.pasteButton.setText("Paste")
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

    def refreshDirectory(self,path):
        self.directoryTextView.setText(main.current_path)

    def showError(self,errorText = None):
        error_dialog = QMessageBox()
        error_dialog.setText("ERROR")
        if errorText != None:
            error_dialog.setText(errorText)
        error_dialog.exec()

    def showDirectoryContent(self,item_list):
        self.itemsView.setRowCount(len(item_list))
        self.itemsView.setColumnCount(3)
        self.itemsView.setHorizontalHeaderLabels(("Name","Date Modified","Size"))
        self.itemsView.autoFillBackground()
        fileIcon = QtGui.QIcon(QtGui.QPixmap("fileIcon.png"))
        folderIcon = QtGui.QIcon(QtGui.QPixmap("folderIcon.png"))
        for i in range(len(item_list)):
            icon = fileIcon
            if os.path.isdir(item_list[i].path+"/"+item_list[i].name):
                icon = folderIcon
            self.itemsView.setItem(i, 0, QTableWidgetItem(icon,item_list[i].name))
            self.itemsView.setItem(i,1 , QTableWidgetItem(item_list[i].date))
            if icon == folderIcon:
                self.itemsView.setItem(i,2,QTableWidgetItem("--"))
            else:
                if item_list[i].size // 1000000000 != 0:
                    size = str(round(item_list[i].size/1000000000,2)) + " GB"
                elif item_list[i].size // 1000000 != 0:
                    size = str(round(item_list[i].size/1000000,2)) + " MB"
                elif item_list[i].size // 1000 != 0:
                    size = str(round(item_list[i].size /1000,2)) + " KB"
                else :
                    size = str(item_list[i].size) + " B"
                self.itemsView.setItem(i,2,QTableWidgetItem(size))
        self.itemsView.resizeColumnsToContents()
        self.itemsView.move(0,0)

    def tableClicked(self,itemm):
        try:
            if itemm.column() == 0:
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
                self.refreshDirectory(main.current_path)
        except PermissionError:
            self.showError("Permission denied!")
        except :
            self.showError()

    def onClickBack(self,MainWindow):#for back button
        if len(self.history)!= 1:
            self.history.pop()
            main.current_path = self.history[-1]
            main.file_list = item.getItemList(main.current_path)
            self.showDirectoryContent(main.file_list)
            self.directoryTextView.setText(main.current_path)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.directoryTextView.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter Directory</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Go to"))
        self.pushButton_2.setText(_translate("MainWindow", "Back"))
        self.directoryTextView.setText(main.current_path)
    def onClickGoTo(self,MainWindow):#for go to button
        if os.path.exists(self.directoryTextView.toPlainText()):
            try:
                mytext = self.directoryTextView.toPlainText()
                main.current_path = mytext
                if os.path.isdir(mytext):
                    main.file_list=item.getItemList(mytext)
                    self.showDirectoryContent(main.file_list)
                    if main.current_path.split('/')[-1] == "..":
                        main.current_path = '/'.join(main.current_path.split('/')[:-2])
                        if main.current_path == '':
                            main.current_path = '/'
                        self.directoryTextView.setText(main.current_path)
                    self.history.append(main.current_path)
                else:
                    os.system("open "+ main.current_path)
                    main.current_path = self.history[-1]
            except:
                self.showError()
        else:
            self.showError(self.directoryTextView.toPlainText()+" does not exist!")




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

