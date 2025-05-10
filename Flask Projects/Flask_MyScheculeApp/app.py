from flask import Flask, render_template, request, redirect, url_for
from db_config import get_connection
from datetime import datetime, timedelta
from math import floor



app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    selected_date = request.args.get('selected_date')
    start_date2 = None
    
    if selected_date:
        selected_date_dt = datetime.strptime(selected_date, "%Y-%m-%d")

        start_date = selected_date_dt - timedelta(
            days=selected_date_dt.weekday())
        
        end_date = start_date + timedelta(days=6)

    else:
        selected_date_dt = datetime.now()

        start_date = selected_date_dt - timedelta(days=selected_date_dt.weekday())

        end_date = start_date + timedelta(days=6)

    query = """SELECT * FROM teaching_schedule 
                WHERE date BETWEEN %s 
                AND %s 
                ORDER BY date, starttime
    """
    cursor.execute(query, (start_date.date(), end_date.date()))
    teaching_schedule_data = cursor.fetchall()
    
    week_dates = []
    start_date2 = start_date
    for i in range(7):  # 7 days, Monday to Sunday
        week_dates.append({
            'day_name': start_date2.strftime('%A'),
            'day_date': start_date2.strftime('%d.%m.%Y')
        })
        start_date2 += timedelta(days=1)
        
    # Calculate total hours and salary
    query2 = """ SELECT SUM(TIMESTAMPDIFF(MINUTE, starttime, endtime)) AS total_minutes
                FROM teaching_schedule 
                WHERE date BETWEEN %s 
                AND %s 
    """
    cursor.execute(query2, (start_date.date(), end_date.date()))
    result2 = cursor.fetchone()
    total_minutes = result2['total_minutes'] if result2['total_minutes'] is not None else 0
    total_hours = round(total_minutes / 60,2)
    
    query3 = """SELECT RATE as rate_perhour, timestampdiff(minute, starttime, endtime)/60 as total_hour 
                FROM teaching_schedule WHERE date BETWEEN %s
                AND %s;
    """
    cursor.execute(query3, (start_date.date(), end_date.date()))
    result3 = cursor.fetchall()
    total_salary = 0
    for row in result3:
        rate_perhour = row['rate_perhour']
        total_hour = row['total_hour']
        total_salary += rate_perhour * total_hour
    total_salary = round(total_salary*1000, 0)
    total_salary = f"{int(total_salary):,}".replace(",", ".") + " VND"
    total_hours = f"{total_hours:.2f} hours"
    
    query4 = """SELECT distinct SUBSTRING(class,1,3) as class
                FROM teaching_schedule
                WHERE date BETWEEN %s
                AND %s;
    
    """
    cursor.execute(query4, (start_date.date(), end_date.date()))
    result4 = cursor.fetchall()
    classes = []
    for row in result4:
        class_name = row['class']
        classes.append(class_name) 
        
    classes_hours = []
        
    query5 = """SELECT SUM(TIMESTAMPDIFF(MINUTE, starttime, endtime)) AS total_minutes
                FROM teaching_schedule 
                WHERE date BETWEEN %s 
                AND %s AND SUBSTRING(class,1,3) = %s
    """
    for class_name in classes:
        cursor.execute(query5, (start_date.date(), end_date.date(), class_name))
        result5 = cursor.fetchone()
        total_minutes = result5['total_minutes'] if result5['total_minutes'] is not None else 0
        total_hours_weekly = round(total_minutes / 60,2)
        total_hours_weekly = f"{total_hours_weekly:.2f} hours"
        classes_hours.append((class_name, total_hours_weekly))
    
    month = start_date.date().month
    year = start_date.date().year
    query6 = """SELECT RATE as rate_perhour, timestampdiff(minute, starttime, endtime)/60 as total_hour 
                FROM teaching_schedule 
                WHERE MONTH(date) = %s 
                AND YEAR(date) = %s;
    """
    cursor.execute(query6, (month, year))
    result6 = cursor.fetchall()
    total_salary_month = 0
    total_hour_month = 0
    for row in result6:
        rate_perhour = row['rate_perhour']
        total_hour = row['total_hour']
        total_salary_month += rate_perhour * total_hour
        total_hour_month += total_hour
        
    total_hour_month = round(total_hour_month, 2)
    total_hour_month = f"{total_hour_month:.2f} hours"
    
    total_salary_month = round(total_salary_month*1000, 0)
    total_salary_month = f"{int(total_salary_month):,}".replace(",", ".") + " VND"
    

        
    print(total_hour_month)
    
                
    cursor.close()
    conn.close()
    

    return render_template('index.html',
                            teaching_schedule_data=teaching_schedule_data,
                            selected_date=selected_date,
                            start_date=start_date,
                            end_date=end_date,
                            total_hours=total_hours,
                            total_salary=total_salary,
                            classes_hours=classes_hours,
                            total_salary_month=total_salary_month,
                            total_hour_month=total_hour_month,
                            week_dates=week_dates,
                            )

@app.route('/edit/<int:lesson_id>')
def edit_lesson(lesson_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM teaching_schedule WHERE id = %s", (lesson_id,))
    lesson = cursor.fetchone()

    cursor.close()
    conn.close()

    if not lesson:
        return f"Lesson with ID {lesson_id} not found", 404

    return render_template('edit.html', lesson=lesson)

@app.route('/update/<int:lesson_id>', methods=['POST'])
def update_lesson_post(lesson_id):
    # read values from form
    class_name = request.form['class_name']
    date = request.form['date']
    start_hour = int(request.form['start_hour'])
    start_minute = int(request.form['start_minute'])
    end_hour = int(request.form['end_hour'])
    end_minute = int(request.form['end_minute'])
    school = request.form['school']
    rate = request.form['rate']
    paid = request.form['paid']

    # convert to timedelta
    from datetime import timedelta
    start_time = timedelta(hours=start_hour, minutes=start_minute)
    end_time = timedelta(hours=end_hour, minutes=end_minute)

    # update DB
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE teaching_schedule 
        SET class=%s, date=%s, starttime=%s, endtime=%s, school=%s, rate=%s, paid=%s 
        WHERE id=%s
    """, (class_name, date, start_time, end_time, school, rate, paid, lesson_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


@app.route('/duplicate/<int:lesson_id>', methods=['GET'])
def duplicate_form(lesson_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM teaching_schedule WHERE id = %s", (lesson_id,))
    original = cursor.fetchone()

    cursor.close()
    conn.close()

    if not original:
        return f"Lesson with ID {lesson_id} not found", 404

    return render_template('duplicate.html', lesson=original)



@app.route('/duplicate/<int:lesson_id>', methods=['POST'])
def save_duplicate(lesson_id):
    class_name = request.form['class_name']
    date = request.form['date']
    start_hour = int(request.form['start_hour'])
    start_minute = int(request.form['start_minute'])
    end_hour = int(request.form['end_hour'])
    end_minute = int(request.form['end_minute'])
    school = request.form['school']
    rate = request.form['rate']
    paid = request.form['paid']

    start_time = timedelta(hours=start_hour, minutes=start_minute)
    end_time = timedelta(hours=end_hour, minutes=end_minute)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO teaching_schedule (class, date, starttime, endtime, school, rate, paid)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (class_name, date, start_time, end_time, school, rate, paid))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')



@app.route('/toggle_paid/<int:lesson_id>', methods=['POST'])
def toggle_paid(lesson_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Get current status
    cursor.execute("SELECT paid FROM teaching_schedule WHERE id = %s", (lesson_id,))
    lesson = cursor.fetchone()
    print(lesson)

    if lesson:
        new_status = 'no' if lesson['paid'] == 'yes' else 'yes'
        cursor.execute("UPDATE teaching_schedule SET paid = %s WHERE id = %s", (new_status, lesson_id))
        conn.commit()
    print(lesson)
    cursor.close()
    conn.close()

    return '', 204  # No content, success

@app.route('/toggle_delete/<int:lesson_id>', methods=['POST'])
def toggle_delete(lesson_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # update DB
    delete_query = "DELETE FROM teaching_schedule WHERE id = %s"
    cursor.execute(delete_query, (lesson_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return '', 204  # No content, success

@app.route('/detail/<int:lesson_id>')
def detail(lesson_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM teaching_schedule WHERE id = %s", (lesson_id,))
    lesson = cursor.fetchone()

    cursor.close()
    conn.close()

    if not lesson:
        return f"Lesson with ID {lesson_id} not found", 404

    
    return render_template('detail.html', lesson=lesson)

@app.route('/add_lesson', methods=['GET', 'POST'])
def add_lesson():
    if request.method == 'POST':
        class_name = request.form['class_name']
        date = request.form['date']
        start_hour = int(request.form['start_hour'])
        start_minute = int(request.form['start_minute'])
        end_hour = int(request.form['end_hour'])
        end_minute = int(request.form['end_minute'])
        school = request.form['school']
        rate = request.form['rate']
        paid = request.form['paid']

        start_time = timedelta(hours=start_hour, minutes=start_minute)
        end_time = timedelta(hours=end_hour, minutes=end_minute)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO teaching_schedule (class, date, starttime, endtime, school, rate, paid)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (class_name, date, start_time, end_time, school, rate, paid))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/')
    else:
        # On GET, just show the form
        return render_template('add_lesson.html')

@app.route('/calculate_hours', methods=['GET', 'POST'])
def calculate():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT distinct YEAR(date) FROM teaching_schedule"
    cursor.execute(query)
    years = cursor.fetchall()

    years2 = [year['YEAR(date)'] for year in years]

    month_names = {
                1: 'January', 2: 'February', 3: 'March', 4: 'April',
                5: 'May', 6: 'June', 7: 'July', 8: 'August',
                9: 'September', 10: 'October', 11: 'November', 12: 'December'
            }
    
    months = []
    months2 = [] 
    companies = [] 
    schools = []
    summary_result = {}
    selected_year = None
    selected_month = None
    selected_company = None
    selected_school = None

    if request.method == 'POST':
        selected_year = request.form.get('year')
        selected_month = request.form.get('month')
        selected_company = request.form.get('company')
        selected_school = request.form.get('school')

        if selected_year:
            cursor.execute("""
                SELECT DISTINCT MONTH(date) AS month
                FROM teaching_schedule
                WHERE YEAR(date) = %s
            """, (selected_year,))
            months = cursor.fetchall()

            for month in months:
                month_num = month['month']
                month_name = month_names.get(month_num, 'Unknown')
                months2.append(month_name)

        if selected_month:
            selected_month2 = [k for k, v in month_names.items() if v == selected_month]
            if selected_month2:
                selected_month2 = selected_month2[0]
            else:
                selected_month2 = None

            print(selected_month2)
            query = "SELECT distinct school FROM teaching_schedule WHERE MONTH(date) = %s AND YEAR(date) = %s;"
            cursor.execute(query, (selected_month2, selected_year,))
            result = cursor.fetchall()
            for row in result:
                companies.append(row['school'])
            companies.append("ALL")
            
        if selected_company:

            if selected_company == "ALL":
                query = "SELECT distinct SUBSTRING(class,1,3) as class FROM teaching_schedule WHERE MONTH(date) = %s AND YEAR(date) = %s;"
                cursor.execute(query,(selected_month2,selected_year,))
                result = cursor.fetchall()
                for row in result:
                    schools.append(row['class'])
                schools.append("ALL")
            else:
                query = "SELECT distinct SUBSTRING(class,1,3) as class FROM teaching_schedule WHERE MONTH(date) = %s AND school = %s AND YEAR(date) = %s;"
                cursor.execute(query,(selected_month2,selected_company,selected_year,))
                result = cursor.fetchall()
                for row in result:
                    schools.append(row['class'])
                schools.append("ALL")

            print(selected_year, selected_month, selected_company,selected_school)
        action = request.form.get('action')

        if action == 'calculate':
            total_hours = 0

            if selected_company == "ALL" and selected_school == "ALL":
                query = """
                    SELECT SUM(TIMESTAMPDIFF(MINUTE, starttime, endtime)) AS total_minutes
                    FROM teaching_schedule
                    WHERE MONTH(date) = %s 
                    AND YEAR(date) = %s;
                """
                query2 = """SELECT RATE as rate_perhour, timestampdiff(minute, starttime, endtime)/60 as total_hour
                            FROM teaching_schedule 
                            WHERE MONTH(date) = %s
                            AND YEAR(date) = %s;
                """
                query3 = """SELECT AVG(RATE) as avg_rate 
                            FROM teaching_schedule 
                            WHERE MONTH(date) = %s 
                            AND YEAR(date) = %s;
                """
                
                cursor.execute(query, (selected_month2, selected_year))
                result = cursor.fetchone()
                cursor.execute(query2, (selected_month2, selected_year))
                result2 = cursor.fetchall()
                cursor.execute(query3, (selected_month2, selected_year))
                result3 = cursor.fetchone()


            elif selected_school == "ALL":
                query = """
                    SELECT SUM(TIMESTAMPDIFF(MINUTE, starttime, endtime)) AS total_minutes
                    FROM teaching_schedule
                    WHERE MONTH(date) = %s 
                    AND school = %s 
                    AND YEAR(date) = %s;
                """
                query2 = """SELECT RATE as rate_perhour, timestampdiff(minute, starttime, endtime)/60 as total_hour
                            FROM teaching_schedule 
                            WHERE MONTH(date) = %s
                            AND school = %s 
                            AND YEAR(date) = %s;
                """
                
                query3 = """SELECT AVG(RATE) as avg_rate
                            FROM teaching_schedule 
                            WHERE MONTH(date) = %s 
                            AND school = %s 
                            AND YEAR(date) = %s;
                """
                
                cursor.execute(query, (selected_month2, selected_company, selected_year))
                result = cursor.fetchone()
                cursor.execute(query2, (selected_month2, selected_company, selected_year))
                result2 = cursor.fetchall()
                cursor.execute(query3, (selected_month2, selected_company, selected_year))
                result3 = cursor.fetchone()

            elif selected_company == "ALL":
                query = """
                    SELECT SUM(TIMESTAMPDIFF(MINUTE, starttime, endtime)) AS total_minutes
                    FROM teaching_schedule
                    WHERE MONTH(date) = %s 
                    AND SUBSTRING(class,1,3) = %s 
                    AND YEAR(date) = %s;
                """
                query2 = """SELECT RATE as rate_perhour, timestampdiff(minute, starttime, endtime)/60 as total_hour
                            FROM teaching_schedule 
                            WHERE MONTH(date) = %s
                            AND SUBSTRING(class,1,3) = %s 
                            AND YEAR(date) = %s;
                """
                query3 = """SELECT AVG(RATE) as avg_rate
                            FROM teaching_schedule 
                            WHERE MONTH(date) = %s 
                            AND SUBSTRING(class,1,3) = %s 
                            AND YEAR(date) = %s;
                """
                cursor.execute(query, (selected_month2, selected_school, selected_year))
                result = cursor.fetchone()
                cursor.execute(query2, (selected_month2 , selected_school, selected_year))
                result2 = cursor.fetchall()
                cursor.execute(query3, (selected_month2, selected_school, selected_year))
                result3 = cursor.fetchone() 

            else:
                query = """
                    SELECT SUM(TIMESTAMPDIFF(MINUTE, starttime, endtime)) AS total_minutes
                    FROM teaching_schedule
                    WHERE MONTH(date) = %s 
                    AND school = %s 
                    AND SUBSTRING(class,1,3) = %s 
                    AND YEAR(date) = %s;
                """
                query2 = """SELECT RATE as rate_perhour, timestampdiff(minute, starttime, endtime)/60 as total_hour 
                            FROM teaching_schedule WHERE MONTH(date) = %s
                            AND school = %s AND SUBSTRING(class,1,3) = %s AND YEAR(date) = %s;
                """
                query3 = """SELECT AVG(RATE) as avg_rate
                            FROM teaching_schedule 
                            WHERE MONTH(date) = %s 
                            AND school = %s 
                            AND SUBSTRING(class,1,3) = %s 
                            AND YEAR(date) = %s;
                """
                
                cursor.execute(query, (selected_month2, selected_company, selected_school, selected_year))
                result = cursor.fetchone()
                cursor.execute(query2, (selected_month2, selected_company, selected_school, selected_year))
                result2 = cursor.fetchall()
                cursor.execute(query3, (selected_month2, selected_company, selected_school, selected_year))
                result3 = cursor.fetchone()
            
            total_minutes = result['total_minutes'] if result['total_minutes'] is not None else 0
            total_hours = total_minutes / 60
            
            total_salary = 0
            for row in result2:
                rate_perhour = row['rate_perhour']
                total_hour = row['total_hour']
                total_salary += rate_perhour * total_hour
                
            
            
            total_hours = round(total_hours, 2)
            total_salary = round(total_salary*1000, 0) 
            hourly_rate = round(result3['avg_rate']*1000,0) if result3['avg_rate'] is not None else 0
            print(hourly_rate)

            formatted_total_hours = f"{total_hours:.2f} hours"
            formatted_hourly_rate = f"{hourly_rate:,}".replace(",", ".") + " VND/H"
            formatted_total_salary = f"{int(total_salary):,}".replace(",", ".")+ " VND"

            summary_result = {
            'total_hours': formatted_total_hours,
            'hourly_rate': formatted_hourly_rate,
            'total_salary': formatted_total_salary}

            cursor.close()
            conn.close()    

    return render_template('calculate.html',
                        years2=years2,
                        months2=months2,
                        companies=companies,
                        schools=schools,
                        selected_year=selected_year,
                        selected_month=selected_month,
                        selected_company=selected_company,
                        selected_school=selected_school,
                        summary_result=summary_result)
    
@app.route('/update_week', methods=['GET', 'POST'])
def update_week():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    selected_date = request.args.get('selected_date') or request.form.get('selected_date')

    start_date2 = None
    
    if selected_date:
        selected_date_dt = datetime.strptime(selected_date, "%Y-%m-%d")

        start_date = selected_date_dt - timedelta(
            days=selected_date_dt.weekday())
        
        end_date = start_date + timedelta(days=6)

    else:
        selected_date_dt = datetime.now()

        start_date = selected_date_dt - timedelta(days=selected_date_dt.weekday())

        end_date = start_date + timedelta(days=6)
        
    selected_date_str = selected_date_dt.strftime("%Y-%m-%d")
    print("selected_date (raw):", selected_date)
    print("selected_date_str:", selected_date_str)  
    query = """SELECT * FROM teaching_schedule 
                WHERE date BETWEEN %s 
                AND %s 
                ORDER BY date, starttime
    """
    cursor.execute(query, (start_date.date(), end_date.date()))
    teaching_schedule_data = cursor.fetchall()
    
    week_dates = []
    start_date2 = start_date
    for i in range(7):  # 7 days, Monday to Sunday
        week_dates.append({
            'day_name': start_date2.strftime('%A'),
            'day_date': start_date2.strftime('%d.%m.%Y')
        })
        start_date2 += timedelta(days=1)
    
    selected = request.form.get('selected_lessons', '')
    selected_ids = selected.split(',') if selected else []
    
    selected_options = request.form.get('option', '')
    if request.method == 'POST':
        print(selected_options)
        
        if selected_options == "Paid":
            for i in selected_ids:

                query= """ UPDATE teaching_schedule
                            SET paid = 'yes'
                            WHERE id IN (%s)
                """
                cursor.execute(query, (i,))    
                conn.commit()
        
        elif selected_options == "Unpaid":
            for i in selected_ids:

                query= """ UPDATE teaching_schedule
                            SET paid = 'no'
                            WHERE id IN (%s)
                """
                cursor.execute(query, (i,))    
                conn.commit()
    
        elif selected_options == "Delete":
            for i in selected_ids:

                query= """ DELETE FROM teaching_schedule
                            WHERE id IN (%s)
                """
                cursor.execute(query, (i,))    
                conn.commit()
                
        if selected_options == "Copy":
            selected_date2 = request.form.get('copy_target_date', '')
            
            print(selected_date2)
            if selected_date2:

                selected_date2_dt = datetime.strptime(selected_date2, "%Y-%m-%d")
                start_date = selected_date2_dt - timedelta(
                    days=selected_date2_dt.weekday())
                end_date = start_date + timedelta(days=6)
                
                class_list = []
                
                for i in selected_ids:
                    query = """SELECT * FROM teaching_schedule 
                                WHERE id = %s
                    """
                    cursor.execute(query, (i,))
                    result = cursor.fetchone()
                    
                    original_weekday = result['date'].weekday()  # 0 = Monday, 1 = Tuesday, etc.
                    new_date = start_date + timedelta(days=original_weekday)  # align to new week
                    
                    result['date'] = new_date
                    class_list.append(result)

                for i in class_list:
                    query = """INSERT INTO teaching_schedule (class, date, starttime, endtime, school, rate, paid)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (i['class'], i['date'], i['starttime'], i['endtime'], i['school'], i['rate'], i['paid']))
                    conn.commit()
                    
        return redirect(url_for('update_week', selected_date=selected_date_str))
     

    return render_template('update_week.html',
                            selected_date=selected_date_str,
                            teaching_schedule_data=teaching_schedule_data,
                            start_date=start_date,
                            end_date=end_date,
                            week_dates=week_dates,
                            )

@app.route('/about')
def about():
    return render_template('about.html')