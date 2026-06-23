from flask import Flask, render_template, redirect, url_for, request
import pymysql


# connecting to the database.
con = pymysql.connect(host="localhost", user="root", password="", database="mi")
cur = con.cursor()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/registor", methods=["POST", "GET"])
def registeruser():

    if request.method == "POST":
        user = request.form.get("user")
        pass1= request.form.get("pass")

        # if user exist.
        q = "Select usernames, passwords from usertable"
        cur.execute(q)
        for u, p in cur.fetchall():
            if u == user and p == pass1:
                return render_template("index.html", msg="User already Exist")
            
        # if user does not exist.
        q = "insert into usertable (usernames, passwords)  values (%s, %s)"
        cur.execute(q, (user, pass1))
        con.commit()
        return render_template("index.html", msg="Reg. Successfully")
    

@app.route("/login", methods=["POST", "GET"])
def loginuser():
        if request.method == "POST":
            user = request.form.get("user")
            pass1= request.form.get("pass")

            # if user exist.
            q = "Select usernames, passwords from usertable"
            cur.execute(q)
            for u, p in cur.fetchall():
                if u == user and p == pass1:
                    return render_template("index.html", msg="Login successfull")
                
            return render_template("index.html", msg="User doesn't exist")



if __name__ == "__main__":
    app.run(debug=True)
