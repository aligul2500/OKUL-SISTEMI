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



@app.route("/puanlari_getir/<int:ogrenci_id>")
def puanlari_getir(ogrenci_id):
    cursor=veritabanı.cursor()
    sorgu="SELECT not_id,ogrenci_id,ders_id ,puan FROM notlar WHERE ogrenci_id = %s"
    bilgi=(ogrenci_id,)
    cursor.execute(sorgu,bilgi)
    notlar=cursor.fetchall()
    cursor.close()

    return render_template('puanlari_getir.html', notlar=notlar)


if __name__ == '__main__':
    app.run(debug=True)