from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
import mysql.connector

#Flask uygulaması oluştur
app = Flask(__name__)    

veritabanı = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="okul_sistemi"
)
 
#Anasayfayı oluştur
@app.route('/')
def anasayfa():
    #Arayüz için html sayfasını görüntüle
    return render_template('anasayfa.html')

if __name__ == '__main__':
    app.run(debug=True)