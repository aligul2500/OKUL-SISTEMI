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
 




@app.route("/ders_ve_not_guncelle", methods=['GET', 'POST'])
def ders_ve_not_guncelle():
    if request.method == "POST":
        not_id = request.form.get("not_id")
        ogrenci_id = request.form.get("ogrenci_id")
        ders_id = request.form.get("ders_id")
        yeni_puan = request.form.get("yeni_puan")

        cursor = veritabanı.cursor()
        sorgu = "UPDATE notlar SET puan=%s WHERE not_id=%s AND ders_id=%s AND ogrenci_id=%s"
        bilgi = (yeni_puan, not_id, ders_id, ogrenci_id)
        cursor.execute(sorgu, bilgi)
        veritabanı.commit()
        cursor.close()
        return redirect(url_for("ders_ve_not_guncelle"))
    return render_template("ders_ve_not_guncelle.html")

if __name__ == '__main__':
    app.run(debug=True)
