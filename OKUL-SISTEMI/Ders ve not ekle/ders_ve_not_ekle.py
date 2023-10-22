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
 




#Öğrencinin ders ve notlarının kaydolacağı sayfayı oluştur
@app.route("/ders_ve_not_ekle", methods=['GET', 'POST'])
def ders_ve_not_ekle():
    if request.method == 'POST': #Eğer istek "POST" isteği ise aşağıdaki işlemleri yap
        ogrenci_id=request.form.get("ogrenci_id")
        ders_id = request.form.get("ders_id")
        not_id = request.form.get("not_id")
        puan = request.form.get("puan")       
        #Veritabanı bğlantısı üzerinden işlem yap
        cursor=veritabanı.cursor()
        #Veritabanı sorgusu oluştur
        ders_ekle = "INSERT INTO notlar ( ogrenci_id, ders_id, not_id, puan) VALUES (%s, %s, %s, %s)"
        bilgiler = (ogrenci_id , ders_id, not_id, puan)
        #Sorguyu çalıştır
        cursor.execute(ders_ekle,bilgiler )
        #Veritabanında ki değişiklikleri kaydet        
        veritabanı.commit()
        #Veritabanını kapat   
        veritabanı.close()   
        return redirect(url_for('ders_ve_not_ekle'))
    #Arayüz için html sayfasını görüntüle            
    return render_template('ders_ve_not_ekle.html')



if __name__ == '__main__':
    app.run(debug=True)
