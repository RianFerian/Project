from flask import Flask, render_template, request, redirect, url_for, g, flash
import sqlite3
import os


app = Flask(__name__)
app.secret_key = "flash message"

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

# Take the index.html template
@app.route('/')
def Index():
    return render_template('index.html')

# Take the dashboard.html template
@app.route('/dashboard')
def dashboard():
    # Showing all data
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()

    return render_template('dashboard.html', employees = data)

# Insert for a new data
@app.route('/insert', methods = ['POST'])
def insert():

    # Post the form data to database
    if request.method == "POST":
        flash("Data Inserted Success")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO employee (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        db.commit()

        return redirect(url_for('dashboard'))

# Update/edit data
@app.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
        UPDATE employee
        SET name =?, email=?, phone=?
        WHERE id=?
        """, (name, email, phone, id_data))
        flash("Data Updated Sucessfully")
        db.commit()
        return redirect(url_for('dashboard'))

# Delete data
@app.route('/delete/<string:id_data>', methods=['POST', 'GET'])
def delete(id_data):
    # connect to database
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM employee WHERE id =?", (id_data))
    flash("Data Delete Sucessfully")
    db.commit()
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)