
from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)
db = pymysql.connect(host="localhost", user="root", password="Patna@1234", database="film_casting", cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/films')
def films():
    cursor.execute("SELECT * FROM Film")
    films = cursor.fetchall()
    return render_template('films.html', films=films)

@app.route('/actors')
def actors():
    cursor.execute("SELECT * FROM Actor")
    actors = cursor.fetchall()
    return render_template('actors.html', actors=actors)

@app.route('/add_actor', methods=['GET', 'POST'])
def add_actor():
    if request.method == 'POST':
        data = (
            request.form['name'],
            request.form['age'],
            request.form['gender'],
            request.form['experience'],
            request.form['contact_info']
        )
        cursor.execute("INSERT INTO Actor (name, age, gender, experience, contact_info) VALUES (%s, %s, %s, %s, %s)", data)
        db.commit()
        return redirect('/actors')
    return render_template('add_actor.html')

@app.route('/search_actor', methods=['GET', 'POST'])
def search_actor():
    actors = []
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        experience = request.form['experience']
        query = "SELECT * FROM Actor WHERE age <= %s AND gender = %s AND experience >= %s"
        cursor.execute(query, (age, gender, experience))
        actors = cursor.fetchall()
    return render_template('search.html', actors=actors)

if __name__ == '__main__':
    app.run(debug=True)
