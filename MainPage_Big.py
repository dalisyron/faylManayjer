# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage_Big.ui'
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
        MainWindow.resize(836, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/newFolder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QToolTip\n"
"{\n"
"    border: 1px  #76797C;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 20px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #dddddd;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background: #EB5C74;\n"
"}\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_10 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icon/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(41, 40))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet(_fromUtf8(""))
        self.pushButton_3.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icon/forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(41, 40))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icon/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(41, 40))
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icon/setting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setIconSize(QtCore.QSize(41, 40))
        self.pushButton_9.setAutoRepeat(False)
        self.pushButton_9.setAutoExclusive(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.gridLayout_10.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 264, 479))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_6.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_6, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icon/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icon/burn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icon/preview.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("icon/cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("icon/copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon9)
        self.pushButton_7.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("icon/chat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon10)
        self.pushButton_11.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("icon/paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon11)
        self.pushButton_8.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.gridLayout_10.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(100, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_8.addWidget(self.graphicsView, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_8.addWidget(self.listWidget, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_8.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuChange_View = QtGui.QMenu(self.menuView)
        self.menuChange_View.setObjectName(_fromUtf8("menuChange_View"))
        self.menuShare = QtGui.QMenu(self.menubar)
        self.menuShare.setObjectName(_fromUtf8("menuShare"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionPreview = QtGui.QAction(MainWindow)
        self.actionPreview.setObjectName(_fromUtf8("actionPreview"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSort = QtGui.QAction(MainWindow)
        self.actionSort.setObjectName(_fromUtf8("actionSort"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName(_fromUtf8("actionSelect_All"))
        self.actionProperties = QtGui.QAction(MainWindow)
        self.actionProperties.setObjectName(_fromUtf8("actionProperties"))
        self.actionLayouts = QtGui.QAction(MainWindow)
        self.actionLayouts.setObjectName(_fromUtf8("actionLayouts"))
        self.actionLarge = QtGui.QAction(MainWindow)
        self.actionLarge.setObjectName(_fromUtf8("actionLarge"))
        self.actionMedium = QtGui.QAction(MainWindow)
        self.actionMedium.setObjectName(_fromUtf8("actionMedium"))
        self.actionSmall = QtGui.QAction(MainWindow)
        self.actionSmall.setObjectName(_fromUtf8("actionSmall"))
        self.actionShare_Option = QtGui.QAction(MainWindow)
        self.actionShare_Option.setObjectName(_fromUtf8("actionShare_Option"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionUndo)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addAction(self.actionPreview)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSort)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionProperties)
        self.menuChange_View.addAction(self.actionLarge)
        self.menuChange_View.addAction(self.actionMedium)
        self.menuChange_View.addAction(self.actionSmall)
        self.menuView.addAction(self.actionLayouts)
        self.menuView.addAction(self.menuChange_View.menuAction())
        self.menuShare.addAction(self.actionShare_Option)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuShare.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.treeView)
        MainWindow.setTabOrder(self.treeView, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.pushButton_8)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "File Manger", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Milad Hacker Best</p></body></html>", None))
        self.lineEdit.setText(_translate("MainWindow", "Address...", None))
        self.lineEdit_2.setText(_translate("MainWindow", "Search...", None))
        self.label.setText(_translate("MainWindow", "Qiuck Access", None))
        self.label_2.setText(_translate("MainWindow", "Main Window", None))
        self.label_3.setText(_translate("MainWindow", "Information", None))
        self.label_4.setText(_translate("MainWindow", "Thumbnail", None))
        self.menuFile.setTitle(_translate("MainWindow", "File ", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuChange_View.setTitle(_translate("MainWindow", "Change View", None))
        self.menuShare.setTitle(_translate("MainWindow", "Share", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionPreview.setText(_translate("MainWindow", "Preview", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSort.setText(_translate("MainWindow", "Sort", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All", None))
        self.actionProperties.setText(_translate("MainWindow", "Properties", None))
        self.actionLayouts.setText(_translate("MainWindow", "Layouts", None))
        self.actionLarge.setText(_translate("MainWindow", "Large", None))
        self.actionMedium.setText(_translate("MainWindow", "Medium", None))
        self.actionSmall.setText(_translate("MainWindow", "Small", None))
        self.actionShare_Option.setText(_translate("MainWindow", "Share Option", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
