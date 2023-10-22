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


#Öğrencinin ekleneceği sayfayı oluştur
@app.route("/ogrenci_ekle", methods=["GET", "POST"])
def öğrenci_ekle():
    if request.method == "POST":#Eğer method "POST" ise aşağdakı kodu çalıştır
        ogrenci_id = request.form.get("ogrenci_id")
        ad = request.form.get("ad")
        soyad = request.form.get("soyad")
        dogum_tarihi = request.form.get("dogum_tarihi")        
        #Veritabanı bağlantısı üzerinden işlem yap
        cursor = veritabanı.cursor()
        ogrenci_ekle = "INSERT INTO ogrenci_bilgileri (ogrenci_id, ad, soyad, dogum_tarihi) VALUES (%s, %s, %s, %s)"
        eklenen_ogrencinin_bilgileri = (ogrenci_id, ad, soyad, dogum_tarihi)
        #Sorguyu çalıştır
        cursor.execute(ogrenci_ekle, eklenen_ogrencinin_bilgileri)
        #Veritabanındaki değişiklikleri kaydet
        veritabanı.commit()
        #Veritabanı bağlantısını kapat
        cursor.close()
        #İşlem başarılıysa diğer sayfaya yönlendir
        return redirect(url_for("ders_ve_not_ekle"))
       
    #Arayüz için HTML sayfasını görüntüle
    return render_template("ogrenci_ekle.html")

if __name__ == '__main__':
    app.run(debug=True)