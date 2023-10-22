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


@app.route("/ogrenci_id_sorgula", methods=['GET', 'POST'])
def ogrenci_id_sorgula():
    if request.method == 'POST':
        ogrenci_id = request.form.get("ogrenci_id")
        if ogrenci_id:
            return redirect(url_for("ogrenci_bilgisi", ogrenci_id=ogrenci_id))
    return render_template("ogrenci_id_sorgula.html")


if __name__ == '__main__':
    app.run(debug=True)