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




@app.route('/tum_ogrenciler')
def tüm_öğrenciler():
    cursor = veritabanı.cursor()
    cursor.execute('SELECT * FROM ogrenci_bilgileri')#"ogrenci_bilgileri" tablosundaki bütün bilgileri seç
    öğrenciler = cursor.fetchall() # tablodaki tüm bilgileri öğrenciler listesine at
    cursor.close()
    #Arayüz için html sayfasını görüntüle ve html şablonunu öğrenciler listesiyle doldur
    return render_template('tum_ogrenciler.html', öğrenciler=öğrenciler)



if __name__ == '__main__':
    app.run(debug=True)