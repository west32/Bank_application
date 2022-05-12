from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Required
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "dupa123"
app.config["MYSQL_DB"] = "trans_acc"
app.config["MYSQL_PORT"] = 3307 
# Extra configs, optional:
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)

@app.route("/")
def users():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM `account` """)
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":
    app.run(debug=True)