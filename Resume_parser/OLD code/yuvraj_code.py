# -- coding: utf-8 --

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from pyresparser import ResumeParser

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 518)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(238, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 331, 161))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 220, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(171, 255, 206);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius:20px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("folders.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        # self.first_time_csv_write = True
        self.pushButton.clicked.connect(self.open)
        #self.pushButton.show()
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 220, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(171, 255, 206);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius:20px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("personal-information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Resume Parser"))
        self.pushButton.setText(_translate("MainWindow", "Select Files"))
        self.pushButton_2.setText(_translate("MainWindow", "Extracted Data"))

    def extractResume (self, filepath):
        data = ResumeParser(filepath).get_extracted_data()
        return data


    def writeToCSV (self, data ):
        data_file = open('output.csv', 'a+', newline='')
        csv_writer = csv.writer(data_file)

        # Writing data into csv file
        header = data.keys()
        if(self.first_time_csv_write):
            csv_writer.writerow(header)
            self.first_time_csv_write = False
        csv_writer.writerow(data.values())   # Sejal Resume      <-- data
        print("Data inserted successfully...!  :)")
        print(data)
        data_file.close()

    def open(self):
        #print("Hello")
        path = QFileDialog.getOpenFileName(None, 'Open a file', '', 'All Files (*.*)')
        #print("Hello2")
        #if path != ('', ''):
        #print(path[0])
        print("Hello3")
        extracted_Data = self.extractResume(path[0]) # Write extracted data to CSV file
        print("Processing....")
         
        self.writeToCSV(extracted_Data)
        print("File written successfully")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.first_time_csv_write = True
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())