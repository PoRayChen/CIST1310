from flask import Flask, request, redirect,url_for, render_template
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/additem/")
def additem():
    return render_template("Product.html")

@app.route("/product/", methods= ["POST", "GET"])
def product():
    if request.method == "POST":
        data = request.form
        date = data['date']
        productname = data['productname']
        description = data['description']
        quantity = data['quantity']

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("Insert into product(date,productname,description,quantity) VALUES ('{0}', '{1}', '{2}', '{3}')".format(date,productname,description,quantity))
        con.commit()
        message = "Data added"
    return redirect(url_for('list'))

@app.route("/list/")
def list():
    con= sql.connect("database.db")
    con.row_factory = sql.Row

    cur= con.cursor()
    cur.execute("Select * From product")

    rows= cur.fetchall()
    return render_template("Summary.html", rows = rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

