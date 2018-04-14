# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QShortcut, QMainWindow,QMessageBox, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QAbstractItemView,QMenu,QInputDialog,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import item,main,os,time
import socket,json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, _host ,_port ):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 503)
        QShortcut(QtGui.QKeySequence("Backspace"), MainWindow, self.onClickBack)
        QShortcut(QtGui.QKeySequence("Return"), MainWindow, self.onClickGoTo)
        QShortcut(QtGui.QKeySequence("CTRL+c"), MainWindow, self.copyEvent)
        QShortcut(QtGui.QKeySequence("CTRL+v"), MainWindow, self.pasteEvent)
        QShortcut(QtGui.QKeySequence("CTRL+x"), MainWindow, self.cutEvent)
        QShortcut(QtGui.QKeySequence("CTRL+n"), MainWindow, self.newFolderEvent)
        QShortcut(QtGui.QKeySequence("CTRL+Backspace"), MainWindow, self.deleteEvent)
        self.MAX_BUFFER_SIZE = 4098
        self.current_path = '/'
        self.client_socket = socket.socket()
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = _host
        self.port = _port
        print(self.host,self.port)
        self.client_socket.connect((self.host,self.port))
        self.history = [self.current_path]
        self.selected_items = []
        self.file_list = []
        self.cut_selected_items = []
        self.favorite_list = []
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
        self.favoriteView = QtWidgets.QTableWidget(self.centralwidget)
        self.favoriteView.setGeometry(QtCore.QRect(0, 70, 161, 341))
        self.favoriteView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.favoriteView.setVerticalHeaderLabels(())
        self.favoriteView.doubleClicked.connect(self.favoriteTableClicked)
        self.favoriteView.setObjectName("FavoriteView")
        self.directoryTextView = QtWidgets.QTextEdit(self.centralwidget)
        self.directoryTextView.insertPlainText('hamidreza')
        self.directoryTextView.setGeometry(QtCore.QRect(170, 10, 401, 31))
        self.directoryTextView.setObjectName("directoryTextView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.onClickGoTo)
        self.pushButton.setGeometry(QtCore.QRect(580, 10, 110, 32))
        self.pushButton_2 = QtWidgets.QPushButton('back',self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 10, 110, 32))
        self.pushButton_2.clicked.connect(self.onClickBack)
        self.newFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.newFolderButton.setGeometry(QtCore.QRect(170, 430, 110, 32))
        self.newFolderButton.setObjectName("newFolderButton")
        self.newFolderButton.setText("New Folder")
        self.newFolderButton.clicked.connect(self.newFolderEvent)
        self.copyButton = QtWidgets.QPushButton(self.centralwidget)
        self.copyButton.setGeometry(QtCore.QRect(300, 430, 110, 32))
        self.copyButton.setObjectName("copyButton")
        self.copyButton.setText("Copy")
        self.copyButton.clicked.connect(self.copyEvent)
        self.cutButton = QtWidgets.QPushButton(self.centralwidget)
        self.cutButton.setGeometry(QtCore.QRect(430, 430, 110, 32))
        self.cutButton.setObjectName("cutButton")
        self.cutButton.setText("Cut")
        self.cutButton.clicked.connect(self.cutEvent)
        self.pasteButton = QtWidgets.QPushButton(self.centralwidget)
        self.pasteButton.setGeometry(QtCore.QRect(550, 430, 110, 32))
        self.pasteButton.setObjectName("pasteButton")
        self.pasteButton.setText("Paste")
        self.pasteButton.clicked.connect(self.pasteEvent)
        self.favoriteLabel = QtWidgets.QLabel(self.centralwidget)
        self.favoriteLabel.setGeometry(QtCore.QRect(55, 50, 81, 16))
        self.favoriteLabel.setObjectName("favoriteLabel")
        self.favoriteLabel.setText("Favorites")
        self.addButton = QtWidgets.QToolButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(0, 410, 161, 21))
        self.addButton.setObjectName("addButton")
        self.addButton.setText("Add to favorites")
        self.addButton.clicked.connect(self.addEvent)

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

    def deleteEvent(self):
        selected_names = []
        for i in self.itemsView.selectedItems():
            selected_names.append(i.text())
        delete_names = ',&*^'.join(selected_names)
        delete_names_bytes = ("delete:"+delete_names).encode('utf_8')
        self.client_socket.sendall(delete_names_bytes)

        answer = self.client_socket.recv(self.MAX_BUFFER_SIZE)
        dict = json.loads(answer)
        print(dict)
        self.file_list = []
        for i in range(len(dict)):
            itemm = dict[str(i)].split(',')
            self.file_list.append(item.Item(itemm[0],itemm[1],itemm[2],int(itemm[3])))
        self.showDirectoryContent(self.file_list)


    def newFolderEvent(self):
        try:
            name = "New Folder"
            text, okPressed = QInputDialog.getText(MainWindow, "Get Name", "Name:", QLineEdit.Normal, name)
            if okPressed and text != '':
                name  = text
                if os.path.exists(self.current_path+'/'+name):
                    i = 1
                    while os.path.exists(self.current_path + '/' + name+ ' (' + str(i) + ')'):
                        i+=1
                    os.makedirs(self.current_path + '/' + name+ ' (' + str(i) + ')')
                else:
                    os.makedirs(self.current_path+'/'+name)
                self.file_list = item.getItemList(self.current_path)
                self.showDirectoryContent(self.file_list)
        except PermissionError:
            self.showError("Permission denied!")
        except:
            self.showError()
    def copyEvent(self):
        selected_names = []
        for i in self.itemsView.selectedItems():
            selected_names.append(i.text())
        copy_names = ',&*^'.join(selected_names)
        copy_names_bytes = ("copy:"+copy_names).encode('utf_8')
        self.client_socket.sendall(copy_names_bytes)

        # except PermissionError:
        #     self.showError("Permission denied!")
        # except :
        #     self.showError()

        #print(self.itemsView.selectedItems()[0].text())
    def pasteEvent(self):
        self.client_socket.sendall("paste".encode("utf_8"))
        answer = self.client_socket.recv(self.MAX_BUFFER_SIZE)
        dict = json.loads(answer)
        print(dict)
        self.file_list = []
        for i in range(len(dict)):
            itemm = dict[str(i)].split(',')
            self.file_list.append(item.Item(itemm[0],itemm[1],itemm[2],int(itemm[3])))
        self.showDirectoryContent(self.file_list)


    def cutEvent(self):
        try:
            selected_names = []
            for i in self.itemsView.selectedItems():
                selected_names.append(i.text())
            cut_names = ',&*^'.join(selected_names)
            cut_names_bytes = ("cut:"+cut_names).encode('utf_8')
            self.client_socket.sendall(cut_names_bytes)
        except PermissionError:
            self.showError("Permission denied!")
        except :
            self.showError()

    def refreshDirectory(self,path):
        self.directoryTextView.setText(self.current_path)

    def showError(self,errorText = None):
        error_dialog = QMessageBox()
        error_dialog.setText("An error has occurred.")
        if errorText != None:
            error_dialog.setText(errorText)
        error_dialog.exec()

    def favoriteTableClicked(self,itemm):
        path = self.favorite_list[itemm.row()]
        if os.path.exists(path):
            try:
                mytext = path
                self.current_path = mytext
                self.file_list=item.getItemList(mytext)
                self.showDirectoryContent(self.file_list)
                self.directoryTextView.setText(self.current_path)
                self.history.append(self.current_path)
            except PermissionError:
                self.showError("Permission denied!")
            except:
                self.showError()
        else:
            self.showError(path+" does not exist!")

    def addEvent(self):
        self.favorite_list.append(self.current_path)
        self.showFavorites()

    def showFavorites(self):
        self.favoriteView.setRowCount(len(self.favorite_list))
        self.favoriteView.setColumnCount(1)
        self.favoriteView.setHorizontalHeaderLabels(["Name"])
        icon = QtGui.QIcon(QtGui.QPixmap("favorite.png"))
        for i in range(len(self.favorite_list)):
            self.favoriteView.setItem(i,0,QTableWidgetItem(icon,self.favorite_list[i].split('/')[-1]))
        self.itemsView.move(0, 0)


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
        c_path = self.current_path
        try:
            if itemm.column() == 0:
                if self.current_path == '/':
                    self.current_path += str(itemm.data())
                else:
                    self.current_path += '/'+str(itemm.data())
                req = "isdir:"+self.current_path
                req = req.encode("utf_8")
                self.client_socket.sendall(req)
                ans = self.client_socket.recv(self.MAX_BUFFER_SIZE)
                ans = ans.decode('utf_8')
                if ans=="T":
                    self.makeFileList()
                    self.showDirectoryContent(self.file_list)
                    self.history.append(self.current_path)
                else:
                    req = "file:" + self.current_path
                    req = req.encode("utf_8")
                    data = []
                    self.client_socket.sendall(req)
                    file = open(self.current_path.split('/')[-1],"wb")
                    while True:
                        input = self.client_socket.recv(self.MAX_BUFFER_SIZE)
                        if input !="finish,&*^".encode("utf_8"):
                            data.append(input)
                        else:
                            break
                    file.writelines(data)
                    file.close()
                    self.current_path = self.history[-1]
                self.refreshDirectory(self.current_path)
        except PermissionError:
            self.showError("Permission denied!")
            self.current_path = c_path
            self.file_list = item.getItemList(self.current_path)

        except :
            self.showError()
            self.current_path = c_path
            self.file_list = item.getItemList(self.current_path)

    def onClickBack(self):#for back button
        if len(self.history)!= 1:
            self.history.pop()
            self.current_path = self.history[-1]
            self.makeFileList()
            self.showDirectoryContent(self.file_list)
            self.directoryTextView.setText(self.current_path)

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
        self.directoryTextView.setText(self.current_path)

    def onClickGoTo(self):#for go to button
        req = "exist:" + self.directoryTextView.toPlainText()
        req = req.encode("utf_8")
        self.client_socket.sendall(req)
        ans = self.client_socket.recv(self.MAX_BUFFER_SIZE)
        ans = ans.decode('utf_8')
        if ans == "T":
            try:
                self.current_path = self.directoryTextView.toPlainText()
                req = "isdir:" + self.current_path
                req = req.encode("utf_8")
                self.client_socket.sendall(req)
                ans = self.client_socket.recv(self.MAX_BUFFER_SIZE)
                ans = ans.decode('utf_8')

                if ans=="T":
                    self.makeFileList()
                    self.showDirectoryContent(self.file_list)
                    if self.current_path.split('/')[-1] == "..":
                        self.current_path = '/'.join(self.current_path.split('/')[:-2])
                        if self.current_path == '':
                            self.current_path = '/'
                        self.directoryTextView.setText(self.current_path)
                    self.history.append(self.current_path)
                else:
                    req = "file:" + self.current_path
                    req = req.encode("utf_8")
                    data = []
                    self.client_socket.sendall(req)
                    file = open(self.current_path.split('/')[-1], "wb")
                    while True:
                        input = self.client_socket.recv(self.MAX_BUFFER_SIZE)
                        if input != "finish,&*^".encode("utf_8"):
                            data.append(input)
                        else:
                            break
                    file.writelines(data)
                    file.close()
                    self.current_path = self.history[-1]
            except PermissionError:
                self.showError("Permission denied!")
            except:
                self.showError()
        else:
            self.showError(self.directoryTextView.toPlainText()+" does not exist!")
    def makeFileList(self):
        req = "get:"+self.current_path
        req = req.encode("utf_8")
        print(req)
        self.client_socket.sendall(req)
        answer = self.client_socket.recv(self.MAX_BUFFER_SIZE)
        dict = json.loads(answer)
        print(dict)
        self.file_list = []
        for i in range(len(dict)):
            itemm = dict[str(i)].split(',')
            self.file_list.append(item.Item(itemm[0],itemm[1],itemm[2],int(itemm[3])))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #default path show
    file = open("t.txt" , "r")
    data = file.readline().split(',&*^')
    ip =data[0]
    port = int(data[1])
    ui.setupUi(MainWindow,ip ,port)
    ui.makeFileList()
    ui.showDirectoryContent(ui.file_list)

    MainWindow.show()
    #print(self.current_path)
    sys.exit(app.exec_())

'''
def makeNewUI(host, port):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #default path show

    ui.setupUi(MainWindow,host, port)
    ui.makeFileList()
    ui.showDirectoryContent(ui.file_list)

    MainWindow.show()
    #print(main.current_path)
    sys.exit(app.exec_())'''