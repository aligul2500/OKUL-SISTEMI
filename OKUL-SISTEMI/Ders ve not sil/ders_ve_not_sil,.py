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
 



@app.route("/ders_ve_not_sil", methods=['GET', 'POST'])
def ders_ve_not_sil():
    if request.method == "POST":
        not_id = request.form.get("not_id")
        ogrenci_id=request.form.get("ogrenci_id")
        ders_id = request.form.get("ders_id")        
        puan = request.form.get("puan") 

        cursor=veritabanı.cursor()
        ders_sil="DELETE FROM notlar WHERE not_id=%s AND ogrenci_id=%s AND ders_id=%s AND puan=%s"
        bilgiler=(not_id,ogrenci_id,ders_id,puan)
        cursor.execute(ders_sil,bilgiler)
        veritabanı.commit()
        cursor.close()

        return redirect(url_for("ders_ve_not_sil"))
    return render_template("ders_ve_not_sil.html")

if __name__ == '__main__':
    app.run(debug=True)       