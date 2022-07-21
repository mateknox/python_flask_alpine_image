from flask import render_template, request, Flask
import db
import logging

app = Flask(__name__, template_folder='templates')


# main endpoint
@app.route('/')
@app.route('/index')
def index():
    # Select last user info from db
    statement = "select * from clients order by id desc limit 1;"
    last_user = db.select_from_db(statement, True)
    return render_template("index.html", title='Home', last_user=last_user)


@app.route('/insert_to_db')
def insert():
    name = request.args.get('name')
    mail = request.args.get('mail')
    date = request.args.get('date')
    db.insert_to_db(name, mail, date)
    return render_template("insert.html", name=name, mail=mail, date=date)


@app.route('/select_from_db')
def select():
    name = request.args.get('name')
    statement = "select * from clients where name = " + name
    logging.info(statement)
    processed_request = db.select_from_db(statement, False)
    return render_template("select.html", processed_request=processed_request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5003')
    logging.info("App is running")
