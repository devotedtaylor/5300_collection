# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSItransimitter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
import thread
import threading
import sys
import signal
import os
import multiprocessing
import subprocess
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
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.debug = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(561, 282)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 112, 471, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.radioButton_3 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 32, 471, 71))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.radioButton = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(150, 169, 195, 51))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.btnStartClicked)
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.btnStopClicked)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit.setDisabled)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit.setEnabled)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")),
                               self.lineEdit_2.setDisabled)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")),
                               self.lineEdit_2.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CSI Transimitter", None))
        self.label_2.setText(_translate("MainWindow", "发射频率：", None))
        self.radioButton_3.setText(_translate("MainWindow", "最高速", None))
        self.radioButton_4.setText(_translate("MainWindow", "每秒", None))
        self.label_4.setText(_translate("MainWindow", "个包", None))
        self.label.setText(_translate("MainWindow", "发射模式：", None))
        self.radioButton.setText(_translate("MainWindow", "不间断", None))
        self.radioButton_2.setText(_translate("MainWindow", "仅发送", None))
        self.label_3.setText(_translate("MainWindow", "个包", None))
        self.pushButton.setText(_translate("MainWindow", "START", None))
        self.pushButton_2.setText(_translate("MainWindow", "STOP", None))

    def btnStartClicked(self):
        s = ""
        if self.radioButton.isChecked():
            s += "send the packets still you stop"
            packet_num = 1000000000
        else:
            packet_num = int(self.lineEdit.text())
            s += "send %d packets" % packet_num
        if self.radioButton_3.isChecked():
            s += ",and within the maxmaze speed"
            delay_us = 0
        else:
            delay_us = 1000000 / float(self.lineEdit_2.text())
            s += ",and within the speed of {:g} Hz".format(float(self.lineEdit_2.text()))

        #self.t = threading.Thread(target=self.startSender,args=(packet_num,delay_us))
        #self.t.start()
        # self.p = multiprocessing.Process(target=self.startSender,args=(packet_num,delay_us))
        try:
            self.pid = os.fork()
            if self.pid<=0:
                self.startSender(packet_num,delay_us)
		os._exit(0)
        finally:
            pass
        # self.p.start()
        #thread.start_new_thread(self.startSender, (packet_num, delay_us))
        self.statusBar().showMessage(s)
    def closeEvent(self,event):
        if not self.debug:
            os.popen('sudo ifconfig mon0 down')
	event.accept()        
	exit(0)

    def btnStopClicked(self):
        if not self.debug:
            os.popen('kill -15 '+str(self.pid))
	    print "\nsending process stoped"
	    self.statusBar().showMessage("sending process stoped")

    def startSender(self, packet_num, delay_us):

        if not self.debug:
            path = os.popen('sudo find / -path */linux-80211n-csitool-supplementary/injection').read().strip()
            print 'get path:',path
	    os.popen('sudo ifconfig mon0 down')
            cmd = 'sudo %s/setup_inject.sh 64 HT20'%path
            os.popen(cmd)
            print cmd
            os.popen('sudo ifconfig wlan0 down')
            print 'sudo ifconfig wlan0 down'
            os.popen('sudo iw mon0 set channel 64 HT20')
            print 'sudo iw mon0 set channel 64 HT20'
            os.popen('sudo ifconfig mon0 up')
            print 'sudo ifconfig mon0 up'
            print os.popen('sudo echo 0x4101 |sudo tee /sys/kernel/debug/ieee80211/phy0/iwlwifi/debug/monitor_tx_rate').read()
            print 'sudo echo 0x4101 |sudo tee /sys/kernel/debug/ieee80211/phy0/iwlwifi/debug/monitor_tx_rate'
            cmd = 'sudo %s/random_packets' % path
            cmd += ' %d 100 1 %d' % (packet_num, delay_us)
	    print cmd
        else:
            cmd = "ping baidu.com -t"

        # 新建子线程运行random_packet 程序，并将其显示传递给父进程
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        #子进程还没死时
        while subprocess.Popen.poll(process) == None:
            output = process.stdout.read(1).strip(' ')
            if output:
                sys.stdout.write(output)
		sys.stdout.flush()
        print(process.stdout.read().strip())



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    app.exec_()
