from flask import Flask, request, render_template, url_for, redirect
import pymysql

# Establishing connection with database.
con = pymysql.connect(host="localhost", user="root", password="", database="mi")
cur = con.cursor()

app = Flask(__name__)


# Home or index or landing page 
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


# Registeration
@app.route("/Registeration", methods=["POST", "GET"])
def registor():
    if request.method == "POST":

        user = request.form.get("user")
        upass = request.form.get("passworder")

        q= "select usernames, passwords from usertable"
        cur.execute(q)
        for name, pass1 in cur.fetchall():
            if name == user and pass1 == upass:
                return render_template("index.html", msg="User already exist")


        q = "insert into usertable (usernames, passwords) values (%s, %s)"
        cur.execute(q, (user, upass))
        con.commit()

        # return redirect(url_for("home"))
        return render_template("index.html", msg="Registeration Successful")

        
    

# Login
@app.route("/Login", methods=["POST","GET"])
def logins():
    if request.method == "POST":

        user = request.form.get("user")
        upass= request.form.get("passworder")

        q= "select usernames, passwords from usertable"
        cur.execute(q)
        for name, pass1 in cur.fetchall():
            if name == user and pass1 == upass:
                return f"Welcome {name}"
            
        return render_template("index.html", msg="user doesn't exist")
        
        # return f"use does not exist."

        # name = "Shalu"
        # pass1 = "123"
        
        # if name == user and pass1 == upass:
        #     return f"Welcome {name}"
        # else:
        #     return f"User does not exist..."
        

if __name__ == "__main__":
    app.run(debug=True)


