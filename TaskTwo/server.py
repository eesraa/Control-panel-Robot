from flask import Flask, render_template, request 
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
   return render_template ('index.html')

@app.route('/forward/', methods=['POST', 'GET'])
def forward():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase5"
    )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO control (direction, value) VALUES (%s, %s)"
    val = ('forward', 'forward')
    mycursor.execute(sql, val)
    
    mydb.commit()

    mycursor.execute("SELECT value FROM control ORDER BY id DESC LIMIT 1")

    myresult = mycursor.fetchone()

    myresult = myresult[0]

    return render_template ('result.html', data=myresult)

@app.route('/backward/', methods=['POST', 'GET'])
def backward():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase5"
    )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO control (direction, value) VALUES (%s, %s)"
    val = ('backward', 'backward')
    mycursor.execute(sql, val)
    
    mydb.commit()

    mycursor.execute("SELECT value FROM control ORDER BY id DESC LIMIT 1")

    myresult = mycursor.fetchone()

    myresult = myresult[0]

    return render_template ('result.html', data=myresult)

@app.route('/left/', methods=['POST', 'GET'])
def left():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase5"
    )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO control (direction, value) VALUES (%s, %s)"
    val = ('left', 'left')
    mycursor.execute(sql, val)
    
    mydb.commit()

    mycursor.execute("SELECT value FROM control ORDER BY id DESC LIMIT 1")

    myresult = mycursor.fetchone()

    myresult = myresult[0]

    return render_template ('result.html', data=myresult)

@app.route('/right/', methods=['POST', 'GET'])
def right():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase5"
    )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO control (direction, value) VALUES (%s, %s)"
    val = ('right', 'right')
    mycursor.execute(sql, val)
    
    mydb.commit()

    mycursor.execute("SELECT value FROM control ORDER BY id DESC LIMIT 1")

    myresult = mycursor.fetchone()

    myresult = myresult[0]

    return render_template ('result.html', data=myresult)

@app.route('/stop/', methods=['POST', 'GET'])
def stop():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase5"
    )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO control (direction, value) VALUES (%s, %s)"
    val = ('stop', 'stop')
    mycursor.execute(sql, val)
    
    mydb.commit()

    mycursor.execute("SELECT value FROM control ORDER BY id DESC LIMIT 1")

    myresult = mycursor.fetchone()

    myresult = myresult[0]

    return render_template ('result.html', data=myresult)


if __name__ == '__main__':
    app.run(debug=True)