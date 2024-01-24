from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
users = []


@app.route("/Sign/", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        conn = sqlite3.connect("site.db")
        username = request.form.get("username")
        password = request.form.get("password")
        conn.execute("INSERT INTO users(username,password) VALUES(?,?)",
                     (username, password))
        conn.commit()
        users = conn.execute("SELECT * FROM users").fetchall()
        return render_template("users.html"
                               , users=users, len_users=len(users))
    else:
        return render_template("Sign.html")


if __name__ == "__main__":
    app.run(debug=True)
