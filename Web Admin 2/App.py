from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

app = Flask(__name__)

# Get the directory containing the currently executing Python script
folder_path = os.path.dirname(os.path.abspath(__file__))

# Connect to the database file inside the specified folder
db_path = os.path.join(folder_path, 'mydatabase.db')
DEBUG = True

# Function to connect to the database
def connect_db():
    return sqlite3.connect(db_path)

# Get the database connection
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Close the database connection when the request is finished
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/insert', methods = ['POST'])
def insert():
    print("Reached the /insert route")

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        print(f"Received form data: {name}, {email}, {phone}")

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO employee (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        db.commit()

        return redirect(url_for('dashboard'))




if __name__ == "__main__":
    app.run(debug=True)