import sys
import sqlite3
from PyQt5 import QtWidgets,QtGui
import random

class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("database.db")
        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table If Not Exists Üyeler (kullanıcı_adı TEXT, parola TEXT, kimlik TEXT)")

        self.baglanti.commit()
        
    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password) #şifreyi gizler
        self.giris = QtWidgets.QPushButton("Login")
        self.register = QtWidgets.QPushButton("Register")
        self.yazi_alani = QtWidgets.QLabel("")
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.register)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("User Login")
        self.setWindowIcon(QtGui.QIcon("login.jpg"))
        self.giris.clicked.connect(self.login)
        self.register.clicked.connect(self.reg)
        self.show()

    def login(self):
        isim = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From Üyeler where kullanıcı_adı = ? and parola = ?",(isim, par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen Tekrar Deneyin.")

        else:
            self.yazi_alani.setText("Welcome " + isim + " .")

    def user_id(self):
        maks = 10000
        i = 1
        while(True):
            self.uid = random.randint(1,maks)
            self.cursor.execute("Select * From Üyeler Where kimlik = ?", (self.uid,))
            bilgi = self.cursor.fetchall()
            
            if len(bilgi) == 0:
                return self.uid
            else:
                if i > maks:
                    return False
                else:
                    i += 1
                
            

        
    def reg(self):
        try:
            isim = self.kullanici_adi.text()
            par = self.parola.text()
            usid = str(pencere.user_id())
            if usid == "False":
                raise IndexError
            else:
                self.cursor.execute("INSERT INTO Üyeler VALUES(?, ?, ?)", (isim, par, usid))
                self.baglanti.commit()
                self.yazi_alani.setText("Successfully registered.")
        except IndexError:
            self.yazi_alani.setText("Maximum identity limit reached.")
            return False
        except:
            self.yazi_alani.setText("Something went wrong!")

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
