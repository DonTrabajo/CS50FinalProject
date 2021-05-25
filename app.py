import os
import sqlite3
from flask import Flask,flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)
app.secret_key = 'many random bytes'

#Post email input to Database
@app.route("/", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        email_address = request.form.get("email_address")
        with sqlite3.connect("FinalProject.db") as con:
            crsr = con.cursor()
            crsr.execute("INSERT INTO Fans (email) VALUES (?)", (email_address,))
            con.commit()
            con.close
        flash("Welcome to the Fam! Your email's registered.", "info")
        return redirect("/")
    else:
        return render_template("layout.html")
   