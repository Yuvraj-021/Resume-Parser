# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# # spaCy
# !python -m spacy download en_core_web_sm

# # nltk
# !python -m nltk.downloader words
# !python -m nltk.downloader stopwords
# !pip install pyresparser
# !pip install PyPDF2

from PyQt5 import QtCore, QtGui, QtWidgets

from aboutusnew import Ui_MainWindow
from extract import Extract_Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap

import os

import PyPDF2

import spacy

import spacy
import re
from spacy import displacy
from spacy.matcher import Matcher
import csv

#nlp = spacy.load("en")



class Ui_main(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        main.hide();
        self.window.show()




    def openExtracteDataWindow(self):
        #print("Hello")
        self.window = QtWidgets.QMainWindow()
        self.ui = Extract_Ui_MainWindow()
        self.ui.setupUi(self.window)
        #main.hide();
        self.window.show()

        
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(742, 600)
        main.setAutoFillBackground(False)
        main.setStyleSheet("background-color: rgb(255, 245, 245);")
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 30, 411, 61))
        self.label.setStyleSheet("font: 28pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(170, 90, 381, 16))
        self.line.setStyleSheet("color: rgb(255, 0, 0);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 240, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"selection-background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius:20px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/personal-information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openExcel)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 240, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"Times New Roman\";\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius:20px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openFolder)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 40, 65, 65))
        self.pushButton_4.setStyleSheet("background-image: url(Images/user.png)")
        self.pushButton_4.setText("")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.openWindow) 

        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 30))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "main"))
        self.label.setText(_translate("main", "Joining Letter Parser"))
        self.pushButton_2.setText(_translate("main", "Extracted Data"))
        #self.pushButton.setText(_translate("main", "Select Files"))
        self.pushButton_3.setText(_translate("main", "Select Folders"))



########################## ML Code ########################################################
    def extractResume (self, filepath):
        data = ResumeParser(filepath).get_extracted_data()
        return data


    def writeToCSV (self, data ):
        data_file = open('../output/output.csv', 'a+', newline='')
        csv_writer = csv.writer(data_file)

        # Writing data into csv file
        # header = data.keys()
        # if(self.first_time_csv_write):
        #     csv_writer.writerow(header)
        #     self.first_time_csv_write = False
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

    
    def extractPDF (self, filePath):
        pdfFileObj = open(filePath, 'rb')
        content = ""
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        numberOfPages = pdfReader.numPages
        for pageNum in range(0,1):
                page = pdfReader.getPage(pageNum)
                content += page.extractText()
                contents = ''.join(content.split('\n'))
        return contents


    def replace_canadian_period(self, mail):
        mail = mail.replace(u"\u1427", ".")
        return mail
    
    
    def replace_fancy_hyphens(self, mail):
        hlist = [u"\u002d", u"\u058a", u"\u058b", u"\u2010",   u"\u2011", u"\u2012", u"\u2013", u"\u2014", u"\u2015", u"\u2e3a", u"\u2e3b", u"\ufe58", u"\ufe63", u"\uff0d"]
        for h in hlist:
                mail = mail.replace(h, "-")
        return mail


    def lexical_processor(self, mail):
        mail = self.replace_canadian_period(mail)
        mail = self.replace_fancy_hyphens(mail)
        return mail

    
    def email_preprocessor(self, mail):
        entities = {}
        mail = self.lexical_processor(contents)     #mail is unicode
        #mail = cut_greetings(email)        #mail is unicode
        doc = nlp(mail)                    # doc is of spacy.doc type
        entities['emails'] = extract_emails(doc)
   

    def extract_emails(self, doc):
        resultlis = []
        for token in doc:
                if token.like_email:
                        resultlis.append((token.text))
        return resultlis


    def findDesignation (self, persons):
        designations = ["Software Engineer Intern", "Graduate Engineer Trainee", "Software Engineer", "Application Developer", "Project Intern"]
        for person in persons:
                if person in designations:
                        return person

        
    def extractInformation (self, contents):
        NER = spacy.load("en_core_web_sm")
        texts = NER(contents)

        data = {}
        data.setdefault('DESIGNATION', [])
        data.setdefault('CITY', [])
        persons = []
        organizations = {""}

        for word in texts.ents:
                if word.label_ == 'PERSON':
                        persons.append(word.text)
                if word.label_ == 'ORG':
                        organizations.add(word.text)
                if word.label_ == 'GPE':
                        data['CITY'].append(word.text)

        desig = self.findDesignation(persons)
        print(persons)
        data['DESIGNATION'] = [desig]
        # persons.remove(desig)
        data['PERSON'] = persons

        data['ORG'] = list (organizations)

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(contents)

        # Email matcher

        emails = self.extract_emails(doc)
        data['EMAIL'] = emails

        #Phone Number Matcher \d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}

        matcher = Matcher(nlp.vocab)
        pattern = [{'LIKE_NUM': True}, {'LOWER': {'REGEX' : '\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}'}}]
        matcher.add('PHONE', None, pattern)

        matches = matcher(doc)
        data['PHONE'] = [doc[start:end] for match_id, start, end in matches]

        #Salary matcher
        salary_start = re.compile(r'\ INR | Rs.')
        salary_init = salary_start.findall(contents)
        #print(salary_init)
        # if salary_init[0] in [' Rs.']:
        #         salary_pattern = re.compile(r' Rs.+/-')
        #         salaries = salary_pattern.findall(contents)
        #         data['SALARY'] = salaries
        # elif salary_init[0] in [' INR ']:
        #         salary_pattern = re.compile(r'\ INR [0-9,\.]*')
        #         salaries = salary_pattern.findall(contents)
        #         data['SALARY'] = salaries
        # else:
        #         data['SALARY'] = "NA"

        # date matcher

        date_pattern = re.compile(r'((January|February|March|April|May|June|July|August|September|October|November|December)\s([\d]{4}|[\d]{2}))')
        dates = date_pattern.findall(contents)
        data['JOINING DATE'] = dates

        return data




#########################################################################################		
        # def extractDataUsingFolders(self, path):

        # 	# Extract data from resume
        # 	extracted_text = extractPDF(path)

        # 	extracted_Data = extractInformation(extracted_text)
        # 	# Write extracted data to CSV file
        # 	writeToCSV(extracted_Data)
############################################################################################
    def openFolder(self):
                #print("Hello")
        # path = QtWidgets.QFileDialog.getOpenFileName(None, 'Open a file', '', 'All Files (*.*)')
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(main, 'Select Folder')
                #print("Hello2")
                #if path != ('', ''):
                #print(path[0])
        # Extract data from resume

        os.chdir(folderpath)
    
            # iterate through all file
        for file in os.listdir():
                # Check whether file is in text format or not
           # if file.endswith(".pdf"):
                print("File selected for reading")    
                file_path = f"{folderpath}\{file}"
                extracted_text = self.extractPDF(file_path)
                extracted_Data = self.extractInformation(extracted_text)
                # Write extracted data to CSV file
                self.writeToCSV(extracted_Data)
        showMessage()           
        print("done")


    def openExcel(self):
        os.system("start EXCEL.EXE ./output/output.csv")

    
def showMessage():
    msg= QMessageBox()
    msg.setWindowTitle("");
    msg.setText("Data Inserted Successfully!!")
    msg.setIconPixmap(QPixmap("Images/check.png"))
    msg.setStyleSheet("background-color: rgb(255,248,220);")
    x=msg.exec_()




            
######################### ML code END ###################################################

       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.first_time_csv_write = True
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())