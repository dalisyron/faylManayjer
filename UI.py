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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 503)
        QShortcut(QtGui.QKeySequence("Backspace"), MainWindow, self.onClickBack)
        QShortcut(QtGui.QKeySequence("Return"), MainWindow, self.onClickGoTo)
        QShortcut(QtGui.QKeySequence("CTRL+c"), MainWindow, self.copyEvent)
        QShortcut(QtGui.QKeySequence("CTRL+v"), MainWindow, self.pasteEvent)
        QShortcut(QtGui.QKeySequence("CTRL+x"), MainWindow, self.cutEvent)
        QShortcut(QtGui.QKeySequence("CTRL+n"), MainWindow, self.newFolderEvent)
        QShortcut(QtGui.QKeySequence("CTRL+Backspace"), MainWindow, self.deleteEvent)
        self.history = [main.current_path]
        self.selected_items = []
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
        self.selected_items = []
        for i in self.itemsView.selectedItems():
            self.selected_items.append(
                item.Item(main.current_path, i.text(), time.ctime(os.path.getmtime(main.current_path + '/' + i.text())),
                          os.path.getsize(main.current_path + '/' + i.text())))
        for i in self.selected_items:
            i.delete()
        main.file_list = item.getItemList(main.current_path)
        self.showDirectoryContent(main.file_list)


    def newFolderEvent(self):
        try:
            name = "New Folder"
            text, okPressed = QInputDialog.getText(MainWindow, "Get Name", "Name:", QLineEdit.Normal, name)
            if okPressed and text != '':
                name  = text
                if os.path.exists(main.current_path+'/'+name):
                    i = 1
                    while os.path.exists(main.current_path + '/' + name+ ' (' + str(i) + ')'):
                        i+=1
                    os.makedirs(main.current_path + '/' + name+ ' (' + str(i) + ')')
                else:
                    os.makedirs(main.current_path+'/'+name)
                main.file_list = item.getItemList(main.current_path)
                self.showDirectoryContent(main.file_list)
        except PermissionError:
            self.showError("Permission denied!")
        except:
            self.showError()
    def copyEvent(self):
        try:
            self.selected_items = []
            self.cut_selected_items = []
            for i in self.itemsView.selectedItems():
                self.selected_items.append(item.Item(main.current_path , i.text(), time.ctime(os.path.getmtime(main.current_path + '/' +i.text())), os.path.getsize(main.current_path + '/' + i.text())))
        except PermissionError:
            self.showError("Permission denied!")
        except :
            self.showError()

        #print(self.itemsView.selectedItems()[0].text())
    def pasteEvent(self):
        try:
            for i in self.selected_items:
                i.copy(main.current_path)
            if self.cut_selected_items and main.current_path != self.cut_selected_items[0].path:
                for i in self.cut_selected_items:
                    i.copy(main.current_path)
                    i.delete()
            main.file_list = item.getItemList(main.current_path)
            self.showDirectoryContent(main.file_list)
        except:
            self.showError()

    def cutEvent(self):
        try:
            self.selected_items = []
            self.cut_selected_items = []
            for i in self.itemsView.selectedItems():
                self.cut_selected_items.append(
                    item.Item(main.current_path, i.text(), time.ctime(os.path.getmtime(main.current_path + '/' + i.text())),
                              os.path.getsize(main.current_path + '/' + i.text())))
        except PermissionError:
            self.showError("Permission denied!")
        except :
            self.showError()

    def refreshDirectory(self,path):
        self.directoryTextView.setText(main.current_path)

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
                main.current_path = mytext
                main.file_list=item.getItemList(mytext)
                self.showDirectoryContent(main.file_list)
                self.directoryTextView.setText(main.current_path)
                self.history.append(main.current_path)
            except PermissionError:
                self.showError("Permission denied!")
            except:
                self.showError()
        else:
            self.showError(path+" does not exist!")

    def addEvent(self):
        self.favorite_list.append(main.current_path)
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
        c_path = main.current_path
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
                    if sys.platform == 'darwin':
                        c_p = main.current_path.split(' ')
                        c_p='\\ '.join(c_p)
                        print(c_p)
                        os.system("open " + c_p)
                    if sys.platform == 'win32' or sys.platform=='cygwin':
                        os.system("start "+ main.current_path)
                    if sys.platform == 'linux2':
                        os.system(".\\ '"+main.current_path+"'")
                    main.current_path = self.history[-1]
                self.refreshDirectory(main.current_path)
        except PermissionError:
            self.showError("Permission denied!")
            main.current_path = c_path
            main.file_list = item.getItemList(main.current_path)

        except :
            raise
            self.showError()
            main.current_path = c_path
            main.file_list = item.getItemList(main.current_path)

    def onClickBack(self):#for back button
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

    def onClickGoTo(self):#for go to button
        if os.path.exists(self.directoryTextView.toPlainText()):
            try:
                mytext = self.directoryTextView.toPlainText()
                main.current_path = mytext
                if os.path.isdir(mytext):
                    main.file_list=item.getItemList(mytext)
                    self.showDirectoryContent(main.file_list)
                    if main.current_path.split('/')[-1] == "..":
                        main.current_path = '/'.joint(main.current_path.split('/')[:-2])
                        if main.current_path == '':
                            main.current_path = '/'
                        self.directoryTextView.setText(main.current_path)
                    self.history.append(main.current_path)
                else:
                    if sys.platform == 'darwin':
                        c_p = main.current_path.split(' ')
                        c_p='\\ '.join(c_p)
                        print(c_p)
                        os.system("open " + c_p)
                    if sys.platform == 'win32' or sys.platform=='cygwin':
                        os.startfile(main.current_path)
                    if sys.platform == 'linux2':
                        os.system(".\\ '"+main.current_path+"'")
                    main.current_path = self.history[-1]
            except PermissionError:
                self.showError("Permission denied!")
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

