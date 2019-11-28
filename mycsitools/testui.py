# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSIdisplayer2new.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph
import time
import sys
import cmath

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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1436, 868)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 0, 1201, 791))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter_6 = QtGui.QSplitter(self.centralwidget)
        self.splitter_6.setGeometry(QtCore.QRect(10, 60, 182, 351))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.label_4 = QtGui.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.splitter_4 = QtGui.QSplitter(self.splitter_6)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label = QtGui.QLabel(self.splitter_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox_4 = QtGui.QCheckBox(self.splitter_4)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.splitter_4)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.splitter_4)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_6)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_3 = QtGui.QLabel(self.splitter_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(self.splitter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(30)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.splitter_3 = QtGui.QSplitter(self.splitter_6)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.radioButton_2 = QtGui.QRadioButton(self.splitter_3)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton = QtGui.QRadioButton(self.splitter_3)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.splitter_5 = QtGui.QSplitter(self.splitter_6)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.label_5 = QtGui.QLabel(self.splitter_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.spinBox_2 = QtGui.QSpinBox(self.splitter_5)
        self.spinBox_2.setMinimum(100)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setSingleStep(100)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))

        #
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 450, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 450, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        #
        #开始按钮 结束按钮
        self.button_Start = QtGui.QPushButton(self.centralwidget)
        self.button_Start.setGeometry(QtCore.QRect(20, 500, 75, 23))
        self.button_Start.setObjectName(_fromUtf8("button_Start"))
        self.button_end = QtGui.QPushButton(self.centralwidget)
        self.button_end.setGeometry(QtCore.QRect(110, 500, 75, 23))
        self.button_end.setObjectName(_fromUtf8("button_end"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1436, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)


        self.connect(self.checkBox_4, QtCore.SIGNAL('clicked()'), self.checkBoxChange)
        self.connect(self.checkBox_5, QtCore.SIGNAL('clicked()'), self.checkBoxChange)
        self.connect(self.checkBox_6, QtCore.SIGNAL('clicked()'), self.checkBoxChange)
        self.connect(self.spinBox, QtCore.SIGNAL('valueChanged(int)'), self.checkBoxChange)
        self.connect(self.spinBox_2, QtCore.SIGNAL('valueChanged(int)'), self.lineLengthChange)
        self.connect(self.radioButton_2, QtCore.SIGNAL('clicked(bool)'), self.radio_ampClicked)
        self.connect(self.radioButton, QtCore.SIGNAL('clicked(bool)'), self.radio_phaClicked)

        #
        self.connect(self.lineEdit, QtCore.SIGNAL('editingFinished()'), self.editingFinished)
        #
        #连接按钮相应函数
        QtCore.QObject.connect(self.button_Start, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.start_click)
        QtCore.QObject.connect(self.button_end, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.end_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.drawPic(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer.start(0)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Display Setting", None))
        self.label.setText(_translate("MainWindow", "Antenna Setting", None))
        self.checkBox_4.setText(_translate("MainWindow", "Antenna 1", None))
        self.checkBox_5.setText(_translate("MainWindow", "Antenna 2", None))
        self.checkBox_6.setText(_translate("MainWindow", "Antenna 3", None))
        self.label_3.setText(_translate("MainWindow", "Channel Setting", None))
        self.label_2.setText(_translate("MainWindow", "Mod", None))
        self.radioButton_2.setText(_translate("MainWindow", "Amplititude", None))
        self.radioButton.setText(_translate("MainWindow", "Phase", None))
        self.label_5.setText(_translate("MainWindow", "Line Length", None))
        self.lineEdit.setText(_translate("MainWindow", "0", None))
        self.label_6.setText(_translate("MainWindow", "Save Name", None))
        self.button_Start.setText(_translate("MainWindow", "Start", None))
        self.button_end.setText(_translate("MainWindow", "End", None))

    def checkBoxChange(self):
        print("checkBoxChange")

    def editingFinished(self):
        print("editingFinished")

    def radio_ampClicked(self):
        print("radio_ampClicked")

    def lineLengthChange(self):
        print("lineLengthChange")


    def drawPic(self, MainWindow):

        self.pw = pyqtgraph.PlotWidget(name='plots')

        p = self.pw.plot()
        # p.setClipToView(True)

        # curves = [p.plot(pen=(i,nPlots*1.3)) for i in range(nPlots)]

        for i in range(nAntenna * nPlots):
            c = pyqtgraph.PlotCurveItem(pen=(i, nAntenna * nPlots * 1.3))
            # 设置线的颜色
            self.pw.addItem(c)
            c.setPos(0, 0)
            # 设置每根线的基准位置（原点）
            curves.append(c)
        # self.pw.setYRange(0, 60)
        # self.pw.setXRange(0, nSamples)
        # self.pw.resize(1000, 2000)
        MainWindow.verticalLayout.addWidget(self.pw)
        # threading.Thread(target=self.updateData())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateData)

    def updateData(self):
        print("updateData")

        
    def radio_phaClicked(self):
        print("radio_ampClicked")

    def start_click(self):
        print("PyQt4 button click")

    def end_click(self):
        print("PyQt4 button click")


pid = -1
curves = []
nAntenna = 4;
nPlots = 30  # 30个子载波

ptr = 0
lastTime = time.time()
fps = 0
length = 100
debugMode = False
flag = True

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    app.exec_()
