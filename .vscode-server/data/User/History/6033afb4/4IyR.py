import boto3 
import datetime
from boto3.dynamodb.conditions import Attr, Key
from botocore.exceptions import ClientError 

from flask import Flask, render_template, request, url_for, flash, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '3bUXIGVBPsfA3UsqbOk/E8LSazhUDAdxzWTB0c5k'


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/user', methods=('GET', 'POST'))
def user():
    dynamodb=boto3.resource('dynamodb')
    subscriptions = dynamodb.Table('Subscriptions')
    music = dynamodb.Table('Music')
    subResponse = subscriptions.query(KeyConditionExpression=Key('User').eq(session['username']))
    songList=[]
    for item in subResponse['Items']:
        songList.append([item['Song']])
    musResponse = music.scan(FilterExpression=Attr('title').is_in(songList))
    return render_template('user.html', music=musResponse)
    # return str(songList)






@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dynamodb=boto3.resource('dynamodb')
        table = dynamodb.Table('login')
        response = table.scan(FilterExpression=Attr('username').eq(username) and Attr('password').eq(password) )
        data = response['Items']
        if len(data) == 0 or data[0]["username"] != username or data[0]["password"] != password:
            flash("Incorrect Username/Password!")
        else:
            session['username'] = username
            session['password'] = password
            session['email'] = data[0]["email"]
            return redirect(url_for('user'))

    return render_template('login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email=request.form['email']
        dynamodb=boto3.resource('dynamodb')
        table = dynamodb.Table('login')
        if not username or not password or not email:
            flash("Fields are required!")
        response = table.scan(FilterExpression = Attr('email').eq(email))
        if len(response['Items']) > 0:
            flash("User email already taken!")
        else:
            table.put_item(Item={
            'lgn': '0',
            'num':str(datetime.datetime.now()),
            'username': username,
            'password': password,
            'email': email
        })
            return  redirect(url_for('root'))
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)