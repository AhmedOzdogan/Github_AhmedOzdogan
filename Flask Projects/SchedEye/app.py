from datetime import datetime, timedelta
import time
from flask import Flask, render_template, request, redirect, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from db_config import get_connection



app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, id, username, email, password_hash, user_type):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.user_type = user_type
        
def get_user(field, value):
    conn =  get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, username, email, password_hash, user_type FROM users  WHERE {field} = %s", (value,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(*row)
    return None


def get_user_by_email(email):
    return get_user("email", email)

@login_manager.user_loader
def load_user(user_id):
    return get_user("id", user_id)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)

        if not user or not check_password_hash(user.password_hash, password):
            flash('Your email or password is incorrect.', 'danger')
            return redirect(url_for('login'))

        else:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if get_user_by_email(email):
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))
        elif len(password) < 8:
            flash('Password must be at least 8 characters long.', 'danger')
            return redirect(url_for('register'))
        elif not any(char.isdigit() for char in password):
            flash('Password must contain at least one digit.', 'danger')
            return redirect(url_for('register'))
        
        password_hash = generate_password_hash(password)
        conn = get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO users (username, email, password_hash) 
                    VALUES (%s,%s, %s)
        """
        cursor.execute(query, (username, email, password_hash))
        conn.commit()
        conn.close()

        flash('Registration successful! You can now log in.', 'success')
        time.sleep(2)
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    # selected_date = datetime.now()

    # start_date = selected_date - timedelta(
    #     days=selected_date.weekday())
    
    # end_date = start_date + timedelta(days=6)
    
    conn = get_connection()
    cursor = conn.cursor()
    selected_date = request.args.get('selected_date')
    
    if selected_date:
        selected_date_dt = datetime.strptime(selected_date, "%Y-%m-%d")

        start_date = selected_date_dt - timedelta(
            days=selected_date_dt.weekday())
        
        end_date = start_date + timedelta(days=6)

    else:
        selected_date_dt = datetime.now()

        start_date = selected_date_dt - timedelta(days=selected_date_dt.weekday())

        end_date = start_date + timedelta(days=6)
        
    cursor.execute("SELECT * FROM teaching_schedule WHERE teacher_id = %s", (current_user.id,))
    
    query = """SELECT * FROM teaching_schedule 
                WHERE date BETWEEN %s 
                AND %s 
                AND teacher_id = %s
                ORDER BY date, starttime
    """
    cursor.execute(query, (start_date.date(), end_date.date(), current_user.id))
    teaching_schedule_data = cursor.fetchall()
    
    
    week_dates = []
    start_date2 = start_date
    for i in range(7):  # 7 days, Monday to Sunday
        week_dates.append({
            'day_name': start_date2.strftime('%A'),
            'day_date': start_date2.strftime('%d.%m.%Y')
        })
        start_date2 += timedelta(days=1)
        
    

    return render_template('dashboard.html',
                           teaching_schedule_data = teaching_schedule_data,
                           week_dates = week_dates,
                           start_date = start_date,
                           end_date = end_date,
                           selected_date = selected_date
)
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('_flashes', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/toggle_paid/<int:lesson_id>', methods=['POST'])
@login_required
def toggle_paid(lesson_id):
    conn = get_connection()
    cursor = conn.cursor()

    # Get current status
    cursor.execute("""SELECT paid 
                   FROM teaching_schedule 
                   WHERE id = %s
                   AND teacher_id = %s
                   """, (lesson_id, current_user.id))
    lesson = cursor.fetchone()
    print(lesson)

    if lesson:
        new_status = 'no' if lesson == 'yes' else 'no'
        cursor.execute("UPDATE teaching_schedule SET paid = %s WHERE id = %s AND teacher_id = %s", (new_status, lesson_id, current_user.id))
        conn.commit()
    print(lesson)
    cursor.close()
    conn.close()

    return '', 204  # No content, success