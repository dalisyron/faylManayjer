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
import functools

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

        self.removeFavoriteButton = QtWidgets.QToolButton(self.centralwidget)
        self.removeFavoriteButton.setGeometry(QtCore.QRect(0, 430, 161, 21))
        self.removeFavoriteButton.setObjectName("removeFavoriteButton")
        self.removeFavoriteButton.setText("Remove from favorites")
        self.removeFavoriteButton.clicked.connect(self.removeFavoriteEvent)
        #self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuChange_View = QtWidgets.QMenu(self.menuView)
        self.menuChange_View.setObjectName("menuChange_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionPreview = QtWidgets.QAction(MainWindow)
        self.actionPreview.setObjectName("actionPreview")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionProperties = QtWidgets.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.actionLayouts = QtWidgets.QAction(MainWindow)
        self.actionLayouts.setObjectName("actionLayouts")
        self.actionLarge = QtWidgets.QAction(MainWindow)
        self.actionLarge.setObjectName("actionLarge")
        self.actionMedium = QtWidgets.QAction(MainWindow)
        self.actionMedium.setObjectName("actionMedium")
        self.actionSmall = QtWidgets.QAction(MainWindow)
        self.actionSmall.setObjectName("actionSmall")
        self.actionSort = QtWidgets.QAction(MainWindow)
        self.actionSort.setObjectName("actionSort")
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSort)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuChange_View.addAction(self.actionLarge)
        self.menuChange_View.addAction(self.actionMedium)
        self.menuChange_View.addAction(self.actionSmall)
        self.menuView.addAction(self.menuChange_View.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.actionSort.triggered.connect(self.sortRefresh)
        self.actionExit.triggered.connect(self.exitApp)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exitApp(self):
        sys.exit()
        
    def deleteEvent(self):
        try:
            self.selected_items = []
            for i in self.itemsView.selectedItems():
                self.selected_items.append(
                    item.Item(main.current_path, i.text(), time.ctime(os.path.getmtime(main.current_path + '/' + i.text())),
                              os.path.getsize(main.current_path + '/' + i.text())))
            for i in self.selected_items:
                i.delete()
            main.file_list = item.getItemList(main.current_path)
            self.showDirectoryContent(main.file_list)
        except PermissionError:
            self.showError("Permission denied!")
        except:
            self.showError()

    def removeFavoriteEvent(self):
        s_i =[]
        new_favorites = []
        for i in self.favoriteView.selectedItems():
            s_i.append(i.row())

        for i in range(len(self.favorite_list)):
            if i not in s_i:
                new_favorites.append(self.favorite_list[i])
        self.favorite_list = new_favorites
        self.showFavorites()


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
              i.copy(main.current_path, False)
          if self.cut_selected_items and main.current_path != self.cut_selected_items[0].path:
              for i in self.cut_selected_items:
                  i.copy(main.current_path, True)
                  i.delete()
          main.file_list = item.getItemList(main.current_path)
          self.showDirectoryContent(main.file_list)
        except PermissionError:
            self.showError("Permission denied!")
        except :
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

    def compare(self, item1):
        slash = '/'
        if (item1.path == '/'):
            slash = ''
        val1 = item1.name
        if os.path.isdir(item1.path+slash+item1.name):
            val1 = '+' + val1
        return val1 

    def sortData(self):
        main.file_list = sorted(main.file_list, key = lambda item : self.compare(item))
    
    def sortRefresh(self):
        self.sortData()
        self.showDirectoryContent(main.file_list)

    def showDirectoryContent(self,item_list):
        self.itemsView.setRowCount(len(item_list))
        self.itemsView.setColumnCount(3)
        self.itemsView.setHorizontalHeaderLabels(("Name","Date Modified","Size"))
        self.itemsView.autoFillBackground()
        fileIcon = QtGui.QIcon(QtGui.QPixmap("fileIcon.png"))
        folderIcon = QtGui.QIcon(QtGui.QPixmap("folderIcon.png"))

        for i in range(len(item_list)):
            icon = fileIcon
            slash = '/'
            if (item_list[i].path == '/'):
                slash = ''
            if os.path.isdir(item_list[i].path+slash+item_list[i].name):
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
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuChange_View.setTitle(_translate("MainWindow", "Change View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionPreview.setText(_translate("MainWindow", "Preview"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionProperties.setText(_translate("MainWindow", "Properties"))
        self.actionLayouts.setText(_translate("MainWindow", "Layouts"))
        self.actionLarge.setText(_translate("MainWindow", "Large"))
        self.actionMedium.setText(_translate("MainWindow", "Medium"))
        self.actionSmall.setText(_translate("MainWindow", "Small"))
        self.actionSort.setText(_translate("MainWindow", "Sort"))

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

