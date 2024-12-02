from flask import Flask, request, render_template
from database import DB
import bcrypt



# Creează o instanță a aplicației Flask
app = Flask(__name__)

database=DB("database.db")



@app.route('/', methods=['GET','POST'])
def home():
    database.open_db()
    if request.method == "POST":
        name=request.form["name"]
        firstname=request.form["firstname"]
        email=request.form["email"]
        password=request.form["pass"].encode('utf-8')
        salt=bcrypt.gensalt()
        hashed_password=bcrypt.hashpw(password, salt)
        database.cursor.execute("INSERT INTO clients (nume, prenume, email, parola) VALUES (?, ?, ?, ?)", (name, firstname, email, hashed_password, ))
        database.conection.commit()
        
    
    return render_template ('index.html')

# Pornește aplicația
if __name__ == '__main__':
    app.run(debug=True)
