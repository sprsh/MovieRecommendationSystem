# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import urllib.request as url
import bs4


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 809)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, -30, 911, 141))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 100, 361, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 240, 331, 61))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 310, 331, 61))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 380, 331, 61))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 450, 331, 61))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 520, 331, 61))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 320, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 390, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 460, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 530, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 170, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(740, 250, 221, 61))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(740, 330, 221, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(740, 410, 221, 61))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(740, 490, 221, 61))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 250, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 330, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(620, 410, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 490, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 190, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 26))
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
        self.label.setText(_translate("MainWindow", "MOVIE RECOMMENDATION SYSTEM"))
        self.label_2.setText(_translate("MainWindow", "Enter the movie user likes"))
        self.label_3.setText(_translate("MainWindow", "Recommendations"))
        self.pushButton.setText(_translate("MainWindow", "INFO"))
        self.pushButton_2.setText(_translate("MainWindow", "INFO"))
        self.pushButton_3.setText(_translate("MainWindow", "INFO"))
        self.pushButton_4.setText(_translate("MainWindow", "INFO"))
        self.pushButton_5.setText(_translate("MainWindow", "INFO"))
        self.label_4.setText(_translate("MainWindow", "Information"))
        self.label_5.setText(_translate("MainWindow", "Duration"))
        self.label_6.setText(_translate("MainWindow", "Director"))
        self.label_7.setText(_translate("MainWindow", "Stars"))
        self.label_8.setText(_translate("MainWindow", "About"))
        self.pushButton_6.setText(_translate("MainWindow", "ENTER"))
        self.pushButton_6.clicked.connect(self.recommend)
        self.pushButton.clicked.connect(self.crawling)
        self.pushButton_2.clicked.connect(self.crawling1)
        self.pushButton_3.clicked.connect(self.crawling2)
        self.pushButton_4.clicked.connect(self.crawling3)
        self.pushButton_5.clicked.connect(self.crawling4)

    def recommend(self):
        try:
            df = pd.read_csv('E:\Movie Recommendation system\movie_dataset1.csv')
            features = ['keywords','cast','genres','director']
            def combine_features(row):
                return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
            for feature in features:
                df[feature] = df[feature].fillna('')
            df["combined_features"] = df.apply(combine_features,axis=1)
            df.iloc[0].combined_features
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df["combined_features"])
            cosine_sim = cosine_similarity(count_matrix)
            def get_title_from_index(index):
                return df[df.index == index]["title"].values[0]
            def get_index_from_title(title):
                return df[df.title == title]["index"].values[0]
            movie_user_likes = self.lineEdit.text()
            movie_index = get_index_from_title(movie_user_likes)
            similar_movies = list(enumerate(cosine_sim[movie_index]))
            sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
            i=0
            list1 = []
            
            for element in sorted_similar_movies:
                list1.append(get_title_from_index(element[0]))
                i=i+1
                if i>5:
                    break
            x = list1[0]
            self.lineEdit_2.setText(f"{x}")
            y = list1[1]
            self.lineEdit_3.setText(f"{y}")
            z = list1[2]
            self.lineEdit_4.setText(f"{z}")
            m = list1[3]
            self.lineEdit_5.setText(f"{m}")
            n = list1[4]
            self.lineEdit_6.setText(f"{n}")
            
            
        except BaseException as e:
            print(e)

    def crawling(self):
        try:
            df = pd.read_csv('E:\Movie Recommendation system\movie_dataset1.csv')
            features = ['keywords','cast','genres','director']
            def combine_features(row):
                return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
            for feature in features:
                df[feature] = df[feature].fillna('')
            df["combined_features"] = df.apply(combine_features,axis=1)
            df.iloc[0].combined_features
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df["combined_features"])
            cosine_sim = cosine_similarity(count_matrix)
            def get_title_from_index(index):
                return df[df.index == index]["title"].values[0]
            def get_index_from_title(title):
                return df[df.title == title]["index"].values[0]
            movie_user_likes = self.lineEdit.text()
            movie_index = get_index_from_title(movie_user_likes)
            similar_movies = list(enumerate(cosine_sim[movie_index]))
            sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
            i=0
            list1 = []
                
            for element in sorted_similar_movies:
                list1.append(get_title_from_index(element[0]))
                i=i+1
                if i>5:
                    break
            path = "https://www.imdb.com/"
            http_response = url.urlopen(path)
            webpage = bs4.BeautifulSoup(http_response,'lxml')
            newpath = path + "find?ref_=nv_sr_fn&q="
            x = list1[0]
            x = x.replace(" ","")
            newpath1=newpath+x
            http_response = url.urlopen(newpath1)
            webpage1= bs4.BeautifulSoup(http_response,'lxml')
            td = webpage1.find('td',class_='result_text')
            href = td.find('a')['href']
            newpath2 = path+href

            http_response3 = url.urlopen(newpath2)
            webpage2 = bs4.BeautifulSoup(http_response3,'lxml')
            div = webpage2.find('div',class_='subtext')
            time1 = div.find('time')
            a=time1.text
            self.textEdit.setText(f"{a}")
            div = webpage2.find('div',class_='rec-director rec-ellipsis')
            b = div.text
            self.textEdit_2.setText(f"{b}")
            div = webpage2.find('div',class_='rec-actor rec-ellipsis')
            c = div.text
            self.textEdit_3.setText(f"{c}")
            div = webpage2.find('div',class_='rec-outline')
            d = div.text
            self.textEdit_4.setText(f"{d}")
            
            
        except BaseException as e:
            print(e)
    def crawling1(self):
        try:
            df = pd.read_csv('E:\Movie Recommendation system\movie_dataset1.csv')
            features = ['keywords','cast','genres','director']
            def combine_features(row):
                return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
            for feature in features:
                df[feature] = df[feature].fillna('')
            df["combined_features"] = df.apply(combine_features,axis=1)
            df.iloc[0].combined_features
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df["combined_features"])
            cosine_sim = cosine_similarity(count_matrix)
            def get_title_from_index(index):
                return df[df.index == index]["title"].values[0]
            def get_index_from_title(title):
                return df[df.title == title]["index"].values[0]
            movie_user_likes = self.lineEdit.text()
            movie_index = get_index_from_title(movie_user_likes)
            similar_movies = list(enumerate(cosine_sim[movie_index]))
            sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
            i=0
            list1 = []
                
            for element in sorted_similar_movies:
                list1.append(get_title_from_index(element[0]))
                i=i+1
                if i>5:
                    break
            path = "https://www.imdb.com/"
            http_response = url.urlopen(path)
            webpage = bs4.BeautifulSoup(http_response,'lxml')
            newpath = path + "find?ref_=nv_sr_fn&q="
            x = list1[1]
            x = x.replace(" ","")
            newpath1=newpath+x
            http_response = url.urlopen(newpath1)
            webpage1= bs4.BeautifulSoup(http_response,'lxml')
            td = webpage1.find('td',class_='result_text')
            href = td.find('a')['href']
            newpath2 = path+href

            http_response3 = url.urlopen(newpath2)
            webpage2 = bs4.BeautifulSoup(http_response3,'lxml')
            div = webpage2.find('div',class_='subtext')
            time1 = div.find('time')
            a=time1.text
            self.textEdit.setText(f"{a}")
            div = webpage2.find('div',class_='rec-director rec-ellipsis')
            b = div.text
            self.textEdit_2.setText(f"{b}")
            div = webpage2.find('div',class_='rec-actor rec-ellipsis')
            c = div.text
            self.textEdit_3.setText(f"{c}")
            div = webpage2.find('div',class_='rec-outline')
            d = div.text
            self.textEdit_4.setText(f"{d}")
            
            
        except BaseException as e:
            print(e)
    def crawling2(self):
        try:
            df = pd.read_csv('E:\Movie Recommendation system\movie_dataset1.csv')
            features = ['keywords','cast','genres','director']
            def combine_features(row):
                return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
            for feature in features:
                df[feature] = df[feature].fillna('')
            df["combined_features"] = df.apply(combine_features,axis=1)
            df.iloc[0].combined_features
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df["combined_features"])
            cosine_sim = cosine_similarity(count_matrix)
            def get_title_from_index(index):
                return df[df.index == index]["title"].values[0]
            def get_index_from_title(title):
                return df[df.title == title]["index"].values[0]
            movie_user_likes = self.lineEdit.text()
            movie_index = get_index_from_title(movie_user_likes)
            similar_movies = list(enumerate(cosine_sim[movie_index]))
            sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
            i=0
            list1 = []
                
            for element in sorted_similar_movies:
                list1.append(get_title_from_index(element[0]))
                i=i+1
                if i>5:
                    break
            path = "https://www.imdb.com/"
            http_response = url.urlopen(path)
            webpage = bs4.BeautifulSoup(http_response,'lxml')
            newpath = path + "find?ref_=nv_sr_fn&q="
            x = list1[2]
            x = x.replace(" ","")
            newpath1=newpath+x
            http_response = url.urlopen(newpath1)
            webpage1= bs4.BeautifulSoup(http_response,'lxml')
            td = webpage1.find('td',class_='result_text')
            href = td.find('a')['href']
            newpath2 = path+href

            http_response3 = url.urlopen(newpath2)
            webpage2 = bs4.BeautifulSoup(http_response3,'lxml')
            div = webpage2.find('div',class_='subtext')
            time1 = div.find('time')
            a=time1.text
            self.textEdit.setText(f"{a}")
            div = webpage2.find('div',class_='rec-director rec-ellipsis')
            b = div.text
            self.textEdit_2.setText(f"{b}")
            div = webpage2.find('div',class_='rec-actor rec-ellipsis')
            c = div.text
            self.textEdit_3.setText(f"{c}")
            div = webpage2.find('div',class_='rec-outline')
            d = div.text
            self.textEdit_4.setText(f"{d}")
            
            
        except BaseException as e:
            print(e)
    def crawling3(self):
        try:
            df = pd.read_csv('E:\Movie Recommendation system\movie_dataset1.csv')
            features = ['keywords','cast','genres','director']
            def combine_features(row):
                return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
            for feature in features:
                df[feature] = df[feature].fillna('')
            df["combined_features"] = df.apply(combine_features,axis=1)
            df.iloc[0].combined_features
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df["combined_features"])
            cosine_sim = cosine_similarity(count_matrix)
            def get_title_from_index(index):
                return df[df.index == index]["title"].values[0]
            def get_index_from_title(title):
                return df[df.title == title]["index"].values[0]
            movie_user_likes = self.lineEdit.text()
            movie_index = get_index_from_title(movie_user_likes)
            similar_movies = list(enumerate(cosine_sim[movie_index]))
            sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
            i=0
            list1 = []
                
            for element in sorted_similar_movies:
                list1.append(get_title_from_index(element[0]))
                i=i+1
                if i>5:
                    break
            path = "https://www.imdb.com/"
            http_response = url.urlopen(path)
            webpage = bs4.BeautifulSoup(http_response,'lxml')
            newpath = path + "find?ref_=nv_sr_fn&q="
            x = list1[3]
            x = x.replace(" ","")
            newpath1=newpath+x
            http_response = url.urlopen(newpath1)
            webpage1= bs4.BeautifulSoup(http_response,'lxml')
            td = webpage1.find('td',class_='result_text')
            href = td.find('a')['href']
            newpath2 = path+href

            http_response3 = url.urlopen(newpath2)
            webpage2 = bs4.BeautifulSoup(http_response3,'lxml')
            div = webpage2.find('div',class_='subtext')
            time1 = div.find('time')
            a=time1.text
            self.textEdit.setText(f"{a}")
            div = webpage2.find('div',class_='rec-director rec-ellipsis')
            b = div.text
            self.textEdit_2.setText(f"{b}")
            div = webpage2.find('div',class_='rec-actor rec-ellipsis')
            c = div.text
            self.textEdit_3.setText(f"{c}")
            div = webpage2.find('div',class_='rec-outline')
            d = div.text
            self.textEdit_4.setText(f"{d}")
            
            
        except BaseException as e:
            print(e)
    def crawling4(self):
        try:
            df = pd.read_csv('E:\Movie Recommendation system\movie_dataset1.csv')
            features = ['keywords','cast','genres','director']
            def combine_features(row):
                return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
            for feature in features:
                df[feature] = df[feature].fillna('')
            df["combined_features"] = df.apply(combine_features,axis=1)
            df.iloc[0].combined_features
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df["combined_features"])
            cosine_sim = cosine_similarity(count_matrix)
            def get_title_from_index(index):
                return df[df.index == index]["title"].values[0]
            def get_index_from_title(title):
                return df[df.title == title]["index"].values[0]
            movie_user_likes = self.lineEdit.text()
            movie_index = get_index_from_title(movie_user_likes)
            similar_movies = list(enumerate(cosine_sim[movie_index]))
            sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
            i=0
            list1 = []
                
            for element in sorted_similar_movies:
                list1.append(get_title_from_index(element[0]))
                i=i+1
                if i>5:
                    break
            path = "https://www.imdb.com/"
            http_response = url.urlopen(path)
            webpage = bs4.BeautifulSoup(http_response,'lxml')
            newpath = path + "find?ref_=nv_sr_fn&q="
            x = list1[4]
            x = x.replace(" ","")
            newpath1=newpath+x
            http_response = url.urlopen(newpath1)
            webpage1= bs4.BeautifulSoup(http_response,'lxml')
            td = webpage1.find('td',class_='result_text')
            href = td.find('a')['href']
            newpath2 = path+href

            http_response3 = url.urlopen(newpath2)
            webpage2 = bs4.BeautifulSoup(http_response3,'lxml')
            div = webpage2.find('div',class_='subtext')
            time1 = div.find('time')
            a=time1.text
            self.textEdit.setText(f"{a}")
            div = webpage2.find('div',class_='rec-director rec-ellipsis')
            b = div.text
            self.textEdit_2.setText(f"{b}")
            div = webpage2.find('div',class_='rec-actor rec-ellipsis')
            c = div.text
            self.textEdit_3.setText(f"{c}")
            div = webpage2.find('div',class_='rec-outline')
            d = div.text
            self.textEdit_4.setText(f"{d}")
            
            
        except BaseException as e:
            print(e)            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
