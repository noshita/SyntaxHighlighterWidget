# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.hLayoutWhole = QtWidgets.QHBoxLayout()
        self.hLayoutWhole.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.hLayoutWhole.setObjectName("hLayoutWhole")
        self.vLayoutInput = QtWidgets.QVBoxLayout()
        self.vLayoutInput.setObjectName("vLayoutInput")
        self.pTxtEdtrInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pTxtEdtrInput.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.pTxtEdtrInput.setObjectName("pTxtEdtrInput")
        self.vLayoutInput.addWidget(self.pTxtEdtrInput)
        self.hLayoutLang = QtWidgets.QHBoxLayout()
        self.hLayoutLang.setObjectName("hLayoutLang")
        self.lblLang = QtWidgets.QLabel(self.centralwidget)
        self.lblLang.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLang.setObjectName("lblLang")
        self.hLayoutLang.addWidget(self.lblLang)
        self.cmbBox = QtWidgets.QComboBox(self.centralwidget)
        self.cmbBox.setEditable(False)
        self.cmbBox.setObjectName("cmbBox")
        self.hLayoutLang.addWidget(self.cmbBox)
        self.hLayoutLang.setStretch(0, 1)
        self.hLayoutLang.setStretch(1, 2)
        self.vLayoutInput.addLayout(self.hLayoutLang)
        self.hLayoutWhole.addLayout(self.vLayoutInput)
        self.webVOutput = QtWebKitWidgets.QWebView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webVOutput.sizePolicy().hasHeightForWidth())
        self.webVOutput.setSizePolicy(sizePolicy)
        self.webVOutput.setUrl(QtCore.QUrl("about:blank"))
        self.webVOutput.setObjectName("webVOutput")
        self.hLayoutWhole.addWidget(self.webVOutput)
        self.hLayoutWhole.setStretch(0, 2)
        self.hLayoutWhole.setStretch(1, 3)
        self.gridLayout.addLayout(self.hLayoutWhole, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 22))
        self.menubar.setObjectName("menubar")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPreferences.menuAction())

        self.retranslateUi(MainWindow)
        self.cmbBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Syntax Highlighter Widget"))
        self.lblLang.setText(_translate("MainWindow", "Language: "))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))

from PyQt5 import QtWebKitWidgets
