from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Function to connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yashwanth",
            database="project"
        )
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database:", error)
        return None

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        password = request.form['password']
        
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            if role == 'student':
                cursor.execute("SELECT * FROM student WHERE Email = %s AND Password = %s", (email, password))
                user = cursor.fetchone()
                if user:
                    session['email'] = email
                    session['role'] = role
                    return redirect(url_for('student'))
                else:
                    return render_template('login.html', error='Invalid credentials')
            elif role == 'staff':
                cursor.execute("SELECT * FROM staff WHERE Email = %s AND Password = %s", (email, password))
                user = cursor.fetchone()
                if user:
                    session['email'] = email
                    session['role'] = role
                    return redirect(url_for('staff'))
                else:
                    return render_template('login.html', error='Invalid credentials')
            else:
                return render_template('login.html', error='Invalid role')
    return render_template('login.html')

# Student page
@app.route('/student', methods=['GET', 'POST'])
def student():
    connection = connect_to_database()
    if not connection:
        return "Failed to connect to database"
    
    cursor = connection.cursor(dictionary=True)
    
    if 'question_index' not in session:
        session['question_index'] = 0
        session['score'] = 0

    if request.method == 'POST':
        selected_option = request.form.get('option')
        cursor.execute("SELECT * FROM questions WHERE Quiz_id = 16 LIMIT %s, 1", (session['question_index'],))
        question = cursor.fetchone()
        if question and selected_option == question['Answer']:
            session['score'] += 1
        
        session['question_index'] += 1

    cursor.execute("SELECT * FROM questions WHERE Quiz_id = 16 LIMIT %s, 1", (session['question_index'],))
    question = cursor.fetchone()
    
    if not question:
        email = session['email']
        score = round((session['score'] / 15) * 100, 2)
        cursor.execute("INSERT INTO score (Quiz_id, Mail, TotalScore, Remark) VALUES (%s, %s, %s, %s)",
                       (16, email, score, 'Completed'))
        connection.commit()
        session.pop('question_index', None)
        session.pop('score', None)
        return render_template('results.html', score=score)
    
    return render_template('student.html', question=question)

# Staff page
@app.route('/staff')
def staff():
    connection = connect_to_database()
    if not connection:
        return "Failed to connect to database"
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM score WHERE Quiz_id = 16")
    results = cursor.fetchall()
    return render_template('staff.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
