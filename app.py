from flask import Flask, render_template
import pymysql

app = Flask(__name__)


class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.db = "db"

    def __connect__(self):
        self.con = pymysql.connect(
            host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        print(result)
        return result


@app.route("/")
def employees():
    db = Database()
    userlist = db.fetch("SELECT * FROM User LIMIT 50")

    return render_template('userlist.html', result=userlist, content_type='application/json')
