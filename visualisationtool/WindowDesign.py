# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ultimowindow2.ui'
#
# Created: Tue Aug 18 03:18:29 2015
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.resize(998, 771)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.line_raw = QtGui.QLineEdit(self.groupBox_4)
        self.line_raw.setMinimumSize(QtCore.QSize(180, 0))
        self.line_raw.setObjectName(_fromUtf8("line_raw"))
        self.gridLayout_2.addWidget(self.line_raw, 0, 1, 1, 2)
        self.open_raw = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_raw.sizePolicy().hasHeightForWidth())
        self.open_raw.setSizePolicy(sizePolicy)
        self.open_raw.setMaximumSize(QtCore.QSize(30, 30))
        self.open_raw.setObjectName(_fromUtf8("open_raw"))
        self.gridLayout_2.addWidget(self.open_raw, 0, 3, 1, 1)
        self.push_plot = QtGui.QPushButton(self.groupBox_4)
        self.push_plot.setObjectName(_fromUtf8("push_plot"))
        self.gridLayout_2.addWidget(self.push_plot, 1, 2, 1, 2)
        self.run_cluster = QtGui.QPushButton(self.groupBox_4)
        self.run_cluster.setObjectName(_fromUtf8("run_cluster"))
        self.gridLayout_2.addWidget(self.run_cluster, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.widget_4 = MplWidgetT(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 170))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.gridLayout.addWidget(self.widget_4, 0, 0, 1, 3)
        self.line_start = QtGui.QLineEdit(self.groupBox_5)
        self.line_start.setObjectName(_fromUtf8("line_start"))
        self.gridLayout.addWidget(self.line_start, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.line_end = QtGui.QLineEdit(self.groupBox_5)
        self.line_end.setObjectName(_fromUtf8("line_end"))
        self.gridLayout.addWidget(self.line_end, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.widget_6 = QtGui.QWidget(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.pushButton_2 = QtGui.QPushButton(self.widget_6)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 0, 81, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_10 = QtGui.QPushButton(self.widget_6)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 0, 81, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.widget_6, 3, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkbutt = QtGui.QPushButton(self.groupBox_6)
        self.checkbutt.setObjectName(_fromUtf8("checkbutt"))
        self.gridLayout_3.addWidget(self.checkbutt, 2, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.uncheckbutt = QtGui.QPushButton(self.groupBox_6)
        self.uncheckbutt.setObjectName(_fromUtf8("uncheckbutt"))
        self.gridLayout_3.addWidget(self.uncheckbutt, 2, 1, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout_3.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_3.addWidget(self.pushButton_9, 0, 3, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_3.addWidget(self.pushButton_11, 2, 3, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout_3.addWidget(self.pushButton_12, 0, 1, 1, 1)
        self.tableView = QtGui.QTableView(self.groupBox_6)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_3.addWidget(self.tableView, 1, 0, 1, 4)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.textBrowser = QtGui.QTextBrowser(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 50))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_hold2 = QtGui.QWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_hold2.sizePolicy().hasHeightForWidth())
        self.widget_hold2.setSizePolicy(sizePolicy)
        self.widget_hold2.setMinimumSize(QtCore.QSize(0, 35))
        self.widget_hold2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widget_hold2.setObjectName(_fromUtf8("widget_hold2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_hold2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton_2 = QtGui.QRadioButton(self.widget_hold2)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.radioButton = QtGui.QRadioButton(self.widget_hold2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_4.addWidget(self.radioButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_8 = QtGui.QLabel(self.widget_hold2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.pushButton = QtGui.QPushButton(self.widget_hold2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.widget_hold2)
        self.mpl = MplWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setMinimumSize(QtCore.QSize(300, 230))
        self.mpl.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.verticalLayout_2.addWidget(self.mpl)
        self.lineEdit_2 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.widget_11 = MplWidgetT(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 130))
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 130))
        self.widget_11.setObjectName(_fromUtf8("widget_11"))
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_hold = QtGui.QWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_hold.sizePolicy().hasHeightForWidth())
        self.widget_hold.setSizePolicy(sizePolicy)
        self.widget_hold.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_hold.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_hold.setObjectName(_fromUtf8("widget_hold"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_hold)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pushButton_6 = QtGui.QPushButton(self.widget_hold)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_4.addWidget(self.pushButton_6, 0, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.widget_hold)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_4.addWidget(self.pushButton_5, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_hold)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget_2 = QtGui.QWidget(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.radioButton_5 = QtGui.QRadioButton(self.widget_2)
        self.radioButton_5.setGeometry(QtCore.QRect(90, 10, 91, 17))
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(self.widget_2)
        self.radioButton_6.setGeometry(QtCore.QRect(0, 10, 81, 16))
        self.radioButton_6.setMinimumSize(QtCore.QSize(0, 0))
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget_5 = MplWidgetPCA(self.groupBox_3)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.verticalLayout_3.addWidget(self.widget_5)
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.widget_9 = MplWidgetT(self.groupBox_3)
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.verticalLayout_3.addWidget(self.widget_9)
        self.widget_3 = QtGui.QWidget(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 35))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.widget_3)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        self.radioButton_3 = QtGui.QRadioButton(self.widget_3)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget_3)
        self.lineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.widget_12 = MplWidget3(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setMinimumSize(QtCore.QSize(0, 120))
        self.widget_12.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget_12.setObjectName(_fromUtf8("widget_12"))
        self.verticalLayout_3.addWidget(self.widget_12)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Settings", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "File settings", None))
        self.label_4.setText(_translate("MainWindow", "Path:", None))
        self.open_raw.setText(_translate("MainWindow", "...", None))
        self.push_plot.setText(_translate("MainWindow", "Load data", None))
        self.run_cluster.setText(_translate("MainWindow", "Cluster", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Time settings", None))
        self.label_3.setText(_translate("MainWindow", "End", None))
        self.label_2.setText(_translate("MainWindow", "Start", None))
        self.label_6.setText(_translate("MainWindow", "sec.", None))
        self.label_7.setText(_translate("MainWindow", "sec.", None))
        self.pushButton_2.setText(_translate("MainWindow", "Filter Segment", None))
        self.pushButton_10.setText(_translate("MainWindow", "All session", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Filtered clusters", None))
        self.checkbutt.setText(_translate("MainWindow", "Check all", None))
        self.pushButton_3.setText(_translate("MainWindow", "Flag all", None))
        self.uncheckbutt.setText(_translate("MainWindow", "Unckeck all", None))
        self.pushButton_8.setText(_translate("MainWindow", "Filter", None))
        self.pushButton_9.setText(_translate("MainWindow", "Save", None))
        self.pushButton_11.setText(_translate("MainWindow", "Unflag all", None))
        self.pushButton_12.setText(_translate("MainWindow", "Zoom", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Map", None))
        self.radioButton_2.setText(_translate("MainWindow", "Cluster view", None))
        self.radioButton.setText(_translate("MainWindow", "Spike view", None))
        self.label_8.setText(_translate("MainWindow", "Spike color:", None))
        self.pushButton_6.setText(_translate("MainWindow", ">>", None))
        self.pushButton_5.setText(_translate("MainWindow", "<<", None))
        self.pushButton_4.setText(_translate("MainWindow", "Hide time window", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Selected clusters", None))
        self.radioButton_5.setText(_translate("MainWindow", "Complete view", None))
        self.radioButton_6.setText(_translate("MainWindow", "Filtered view", None))
        self.pushButton_7.setText(_translate("MainWindow", "Calculate PCA", None))
        self.radioButton_4.setText(_translate("MainWindow", "Log", None))
        self.radioButton_3.setText(_translate("MainWindow", "Linear", None))
        self.label.setText(_translate("MainWindow", "Bins:", None))
        self.lineEdit.setText(_translate("MainWindow", "10", None))

from mplwidget import MplWidgetT, MplWidget, MplWidget3, MplWidgetPCA
