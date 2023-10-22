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




@app.route("/ogrenci_bilgisi/<int:ogrenci_id>", methods=['GET'])
def ogrenci_bilgisi(ogrenci_id):
    cursor =veritabanı.cursor()
    sorgu = "SELECT * FROM ogrenci_bilgileri WHERE ogrenci_id = %s"
    bilgi = (ogrenci_id,)
    cursor.execute(sorgu, bilgi)
    ogrenci = cursor.fetchone()
    cursor.close()

    if ogrenci:
        #Eğer öğrenci varsa html şablonu ile görüntüle
        return render_template("ogrenci_bilgisi.html", ogrenci=ogrenci)
    else:
        return "Öğrenci bulunamadı"


if __name__ == '__main__':
    app.run(debug=True)