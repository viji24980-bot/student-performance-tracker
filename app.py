from flask import Flask, render_template, request
import sqlite3
from database import create_table

app = Flask(__name__)
create_table()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/add_student', methods=['GET','POST'])
def add_student():

    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']

        conn = sqlite3.connect("student_tracker.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO students(roll_number,name,math,science,english) VALUES(?,?,?,?,?)",
            (roll,name,0,0,0)
        )

        conn.commit()
        conn.close()

        return "Student Added Successfully"

    return render_template("add_student.html")


@app.route('/add_grades', methods=['GET','POST'])
def add_grades():

    if request.method == 'POST':
        roll = request.form['roll']
        math = request.form['math']
        science = request.form['science']
        english = request.form['english']

        conn = sqlite3.connect("student_tracker.db")
        cur = conn.cursor()

        cur.execute("""
        UPDATE students
        SET math=?,science=?,english=?
        WHERE roll_number=?
        """,(math,science,english,roll))

        conn.commit()
        conn.close()

        return "Grades Updated"

    return render_template("add_grades.html")


@app.route('/view_student', methods=['GET','POST'])
def view_student():

    student = None

    if request.method == 'POST':
        roll = request.form['roll']

        conn = sqlite3.connect("student_tracker.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM students WHERE roll_number=?",
            (roll,)
        )

        student = cur.fetchone()

        conn.close()

    return render_template("view_student.html", student=student)


@app.route('/averages')
def averages():

    conn = sqlite3.connect("student_tracker.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    result = []

    for s in students:
        avg = (s[2]+s[3]+s[4])/3
        result.append([s[0],s[1],avg])

    conn.close()

    return render_template("averages.html", data=result)


if __name__ == "__main__":
    app.run(debug=True)
