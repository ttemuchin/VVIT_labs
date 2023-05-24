import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="manta2",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        if password == '' or login == '' or name == '':
            return render_template('registration.html', reg_err_name="Dear user, insert name, login and password, please")
        else:
            cursor.execute("SELECT * FROM service_users WHERE login='%s'" % (str(login)))
            recordsreg = list(cursor.fetchall())
            if recordsreg != []:
                return render_template('registration.html', reg_err_name="Dear user, this login has already taken")
            else:  
                cursor.execute('INSERT INTO service_users (full_name, login, password) VALUES (%s, %s, %s);',
                               (str(name), str(login), str(password)))
                conn.commit()

                return redirect('/login/')
    return render_template('registration.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            if username == "" or password == "":
                return render_template('login.html', err_name="Insert your Login/Password, pal")
            else:
                cursor.execute("SELECT * FROM service_users WHERE login=%s AND password=%s", (str(username), str(password)))
                records = list(cursor.fetchall())

                if records != []:
                    return render_template('account.html', full_name=records[0][1], log=records[0][2], passw=records[0][3])
                else:
                    return render_template('login.html', err_name="Oups, dear user, wrong password or you aren't registered")
        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')


# @app.route('/login/', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     if username == "" or password == "":
#         return render_template('login.html', null_name="pal")
#     else:
#         cursor.execute("SELECT * FROM service_users WHERE login=%s AND password=%s", (str(username), str(password)))
#         records = list(cursor.fetchall())

#         if records != []:
#             return render_template('account.html', full_name=records[0][1], log=records[0][2], passw=records[0][3])
#         else:
#             return render_template('login.html', losted_name="dear user")
