from flask import Flask, render_template, request, url_for, redirect
import mysql.connector

def get_connect_db():
    db = mysql.connector.connect(
        host = 'my_mysql_db',
        user = 'pasha',
        password = '2901',
        database = 'my_data'
    )
    return db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    db = get_connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM works')
    works = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template('home.html', works = works)

@app.route('/admin2901', methods = ['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        name = request.form.get('name')
        describe = request.form.get('describe')
        photo = request.form.get('photo')
        photo2 = request.form.get('photo2')
        photo3 = request.form.get('photo3')
        link = request.form.get('link')
        db = get_connect_db()
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO works (name, decribe, photo, link, photo2, photo3) VALUES ('{name}', '{describe}', '{photo}', '{link}', '{photo2}', '{photo3}')")
        db.commit()

        cursor.close()
        db.close()

    db = get_connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM works')
    works = cursor.fetchall()
    cursor.close()
    db.close()


    return render_template('admin_panel.html', works=works)

@app.route('/delete_photo/<int:id>', methods = ['POST'])
def delete_photo(id):
    db = get_connect_db()
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM works WHERE id = {id}")
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('admin_panel'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)