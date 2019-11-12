# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSIdisplayer2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph
import time
import csiReader
from multiprocessing import Queue
import os
import multiprocessing
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
    def __init__(self, debugMode=True):
        self.debug = debugMode
        self.timestamps = []
        self.data = [list() for i in range(nAntenna * nPlots)]
        self.draw_amp = True
        super(Ui_MainWindow, self).__init__()
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

    def closeEvent(self, event):
        global pid, e
        e.set()
        if debugMode:
	    pid.kill()
            pid.join()    
	event.accept()

    def radio_ampClicked(self):
        self.data = [list() for i in range(nAntenna * nPlots)]
        self.timestamps = []
        self.draw_amp = True

    def radio_phaClicked(self):
        self.data = [list() for i in range(nAntenna * nPlots)]
        self.timestamps = []
        self.draw_amp = False

    def lineLengthChange(self):
        global length
        length = self.spinBox_2.value()

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

    def checkBoxChange(self):
        if nAntenna < 3:
            self.checkBox_6.setChecked(False)
            self.checkBox_6.setCheckable(False)
        if nAntenna < 2:
            self.checkBox_5.setChecked(False)
            self.checkBox_5.setCheckable(False)
        if nAntenna < 1:
            self.checkBox_4.setChecked(False)
            self.checkBox_4.setCheckable(False)
        for i in range(nAntenna * nPlots):
            if i % self.spinBox.value() != 0:
                curves[i].hide()
            elif i < 30 and not self.checkBox_4.isChecked():
                curves[i].hide()
            elif i >= 30 and i < 60 and not self.checkBox_5.isChecked():
                curves[i].hide()
            elif i >= 60 and i < 90 and not self.checkBox_6.isChecked():
                curves[i].hide()
            else:
                curves[i].show()

    def updateData(self):
        global curves, data, nPlots, nAntenna, flag, lastTime
        # global lastTime, fps, ptr

        # while True:
        try:
            s = q.get_nowait()
        except Exception:
            return
        n = q.qsize()
        # if n % 100 == 99:
        #     print n
        # s = s.split(',')
        timestamp = s[0].real
        if flag:
            lastTime = timestamp
            flag = False
        if n > 400 and timestamp % 14 != 0:
            return
        if n > 300 and timestamp % 10 != 0:
            return
        if n > 200 and timestamp % 4 != 0:
            return
        if n > 100 and timestamp % 2 != 0:
            return
        timestamp -= lastTime
        timestamp /= 1000000.0
        # s = s[1:]
        nAntenna = (len(s) - 1) / 30
        # s = map(complex, s)

        if len(self.timestamps) >= length:
            self.timestamps = self.timestamps[1:]
            self.timestamps.append(timestamp)
            for i in range(nAntenna * nPlots):
                if i % self.spinBox.value() != 0:
                    continue
                elif i < 30 and not self.checkBox_4.isChecked():
                    continue
                elif i >= 30 and i < 60 and not self.checkBox_5.isChecked():
                    continue
                elif i >= 60 and not self.checkBox_6.isChecked():
                    continue
                self.data[i] = self.data[i][1:]
                self.data[i].append(self.comData(s[i + 1]))
                curves[i].setData(x=self.timestamps, y=self.data[i])
                curves[i].setPos(self.timestamps[0], 0)
        else:
            self.timestamps.append(timestamp)
            for i in range(nAntenna * nPlots):
                self.data[i].append(self.comData(s[i + 1]))
                if i % self.spinBox.value() != 0:
                    continue
                elif i < 30 and not self.checkBox_4.isChecked():
                    continue
                elif i >= 30 and i < 60 and not self.checkBox_5.isChecked():
                    continue
                elif i >= 60 and not self.checkBox_6.isChecked():
                    continue
                curves[i].setData(x=self.timestamps, y=self.data[i])
                curves[i].setPos(self.timestamps[0], 0)

    def comData(self, c):
        if self.draw_amp:
            return c.__abs__()
        else:
            r = cmath.phase(c)
            if r < 0:
                return r + 2 * cmath.pi
            return r


def startRcv(debug, reader):
    global pid
    if debug:
        pid = multiprocessing.Process(target=reader.monitor, args=(q, e))
        pid.start()
        # threading.Thread(target=reader.monitor, args=(q,)).start()
    else:
        try:
            pid = os.fork()
            if pid <= 0:
                reader.monitor(q, e)
                print 'monitor process exit'
                os._exit(0)
        finally:
            pass


pid = -1
q = Queue(10000)
curves = []
nAntenna = 4;
nPlots = 30  # 30个子载波

ptr = 0
lastTime = time.time()
fps = 0
length = 100
debugMode = False
flag = True
e = multiprocessing.Event()

if __name__ == "__main__":
    reader = csiReader.csiReader(debugMode=debugMode)
    startRcv(debug=debugMode, reader=reader)
    app = QtGui.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    app.exec_()
