from flask import Flask,render_template,request,redirect,url_for,session,flash
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app=Flask(__name__)

app.secret_key= os.getenv("SECRET_KEY")

#database bağlantısı
def get_db_connection():
    conn= sqlite3.connect("agenda.db")
    conn.row_factory= sqlite3.Row #dict erişimi için
    return conn

#Anasayfa
@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn=get_db_connection()
    notes= conn.execute("SELECT * FROM notes ORDER BY date ASC").fetchall()
    conn.close()
    return render_template("index.html",notes=notes)

# --- Yeni Not Ekleme ---
@app.route("/ekle",methods=["GET", "POST"])
def add():
    if request.method== "POST":
        title= request.form["title"]
        content= request.form["content"]
        date= request.form["date"]
        
        conn=get_db_connection()
        conn.execute("INSERT INTO notes (title,content,date) Values (?,?,?)",(title,content,date))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    
    return render_template("ekle.html")

# --- Not Silme ---
@app.route("/delete/<int:note_id>", methods=["POST"])
def delete(note_id):
    conn=get_db_connection()
    conn.execute("DELETE FROM notes WHERE id= ?",(note_id,)) #Burada note_id tek eleman olduğu için sonuna , koyduk birden fazla ise gerek yok 
    conn.commit()
    conn.close()
    return redirect(url_for("home"))
    
# --- Not Güncelleme ---
@app.route("/update/<int:note_id>", methods=["GET","POST"])
def update(note_id):
    conn=get_db_connection()
    if request.method== "POST":
        title= request.form["title"]
        content= request.form["content"]
        date= request.form["date"]
        
        conn.execute("UPDATE notes SET title= ?, content= ?, date=? WHERE id= ?", (title,content,date,note_id))
        conn.commit()
        conn.close()
        
        return redirect(url_for("home"))    
    # GET isteğinde ise güncellenecek notu getir
    note= conn.execute("SELECT * FROM notes WHERE id= ?",(note_id,)).fetchone()
    conn.close()
    
    return render_template("update.html", note=note)
 
# --- Tamamlandı Durumu ---
@app.route("/toggle_done/<int:note_id>",methods=["POST"])
def toggle_done(note_id):
    conn=get_db_connection()
    note=conn.execute("SELECT done FROM notes WHERE id=?", (note_id,)).fetchone()
    new_done=0 if note["done"] else 1
    conn.execute("UPDATE notes SET done=? WHERE id=?",(new_done,note_id))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))
 
#Profil   
@app.route("/profile")
def profil():
    return render_template("profile.html")   
  


#Date Düzenlemesi
@app.template_filter("datetimeformat")
def datetimeformat(value):
    return datetime.strptime(value, "%Y-%m-%d").strftime("%d-%m-%Y")
    

#AUTHENTICATION
#Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_pw = generate_password_hash(password)

        conn = get_db_connection()
        cursor= conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username= ?",(username,))
            existing_user=cursor.fetchone()
            
            if existing_user:
                flash("Bu kullanıcı mevcut, başka bir şey deneyin.","error")
            else:
                cursor.execute("INSERT INTO users (username,password) Values (?,?)",(username,hashed_pw))
                
                conn.commit()
                flash("Kayıt Başarılı","success")
                return redirect(url_for("login"))
            
        except sqlite3.IntegrityError:
            flash("Bu kullanıcı adı zaten alınmış, başka bir tane deneyin.", "error")

        finally:
            conn.close()

    return render_template("register.html")


#Login
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username= request.form["username"]
        password= request.form["password"]
        
        conn=get_db_connection()
        user=conn.execute("SELECT * FROM users WHERE username=?",(username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user["password"],password):
            session["user_id"]=user["id"]
            session["username"]=user["username"]
            return redirect(url_for("home"))
        else:
            flash("Kullanıcı Adı Veya Şifre Hatalı!","error")
    
    return render_template("login.html")

#Logout
@app.route("/logout")
def logout():
    session.clear()
    flash("Çıkış İşlemi Başarıyla Gerçekleşti.")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
