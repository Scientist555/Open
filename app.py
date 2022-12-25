import psycopg2
import requests
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
conn = psycopg2.connect(database='service_db',user='postgres',password='1643',host='localhost',port='5432')
cursor = conn.cursor()

@app.route('/login/',methods=['GET'])
def welcome():
    return render_template('login.html')

@app.route('/login/',methods=['POST'])
def login():
    if request.form.get('registration'): return redirect('/registration/')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s",(str(username),str(password)))
        records = list(cursor.fetchall())
        if records: 
            return render_template('account.html', full_name=records[0][1], user_name = records[0][2], passwrd = records[0][3])
        else:
            return render_template('login.html',mesg = 'Ошибка, Вы неверно ввели имя пользователя или пароль!')


@app.route('/registration/', methods=['POST'])
def indexreg():
    if request.method =='POST':
        login = request.form.get('login')
        cursor.execute("SELECT * FROM service.users WHERE login='{}';".format(str(login)))
        records = cursor.fetchone()
        if records: 
            return render_template('registration.html',mesg = 'Ошибка, пользователь с таким именем уже существует.') 
        else:
            name = request.form.get('name')
            password = request.form.get('password')
            cursor.execute('INSERT INTO service.users (full_name,login,password) VALUES (%s,%s,%s);',(str(name),str(login),str(password)))
            conn.commit()
            return redirect('/login/')


@app.route('/registration/', methods=['GET'])
def welcomereg():
    return render_template('registration.html')

if __name__ == "__main__" :
    app.run(debug=True)
