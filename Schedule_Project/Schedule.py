import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import datetime
from tkinter import messagebox
from time import strftime

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ahmed.4091",
    database="teaching_schedule_db"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a Tkinter window
window = tk.Tk()
window.title("Teaching Schedule")

# Add the rowheight
s=ttk.Style()
s.theme_use('clam')
s.configure('Treeview',font=("Times New Roman ", 10), rowheight=55)

# Create a Treeview widget
tree = ttk.Treeview(window)

# Define the columns
tree["columns"] = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

# Format the columns
tree.column("#0", width=0, stretch=tk.NO)  # Hide the first (default) column
for day in range(7):
    tree.column(day, anchor=tk.CENTER)

# Create the column headings
tree.heading("#0", text="")
tree.heading("monday", text="Monday")
tree.heading("tuesday", text="Tuesday")
tree.heading("wednesday", text="Wednesday")
tree.heading("thursday", text="Thursday")
tree.heading("friday", text="Friday")
tree.heading("saturday", text="Saturday")
tree.heading("sunday", text="Sunday")

# Pack the Treeview widget
tree.pack(pady=10)
 
# Create labels for total hours and total money
total_hours_label = ttk.Label(window, text="Total Hours Worked: ")
total_hours_label.configure(font=("Times New Roman", 14), foreground="green")
total_hours_label.pack(pady=10)

total_money_label = ttk.Label(window, text="Total Expected Money: $")
total_money_label.configure(font=("Times New Roman", 14), foreground="green")
total_money_label.pack(pady=10)

# Create a calendar frame
calendar_frame = tk.Frame(window)
calendar_frame.pack()

# Create a calendar widget
cal = Calendar(calendar_frame, selectmode="day", date_pattern="yyyy-mm-dd", font="Arial 12")
cal.pack(pady=10)

# Create a function to filter classes based on the selected week
def filter_classes():
    selected_date = cal.get_date()
    selected_datetime = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
    start_date = selected_datetime - datetime.timedelta(days=selected_datetime.weekday())
    end_date = start_date + datetime.timedelta(days=6)
    
    # Execute a SELECT query to retrieve the teaching schedule data for the entire week
    query = "SELECT * FROM teaching_schedule WHERE date >= %s AND date <= %s"
    cursor.execute(query, (start_date.date(), end_date.date()))
    
    # Fetch all the rows returned by the query
    teaching_schedule_data = cursor.fetchall()

    # Clear existing rows in the treeview
    tree.delete(*tree.get_children())

    # Create a dictionary to hold the schedule data for each day
    schedule_data = {day: [] for day in range(7)}

    # Populate the dictionary with the schedule data
    for row in teaching_schedule_data:
        class_id = row[0]
        class_name = row[1]
        date = row[2]
        starttime = row[3]
        endtime = row[4]
        school = row[5]
        rate = row[6]

        day = (date.weekday()) % 7  # Adjust day index to start from Monday
        schedule_data[day].append((class_id, class_name, date, starttime, endtime, school, rate))

    # Sort the classes for each day based on the start time
    for day in range(7):
        schedule_data[day].sort(key=lambda x: x[3])
    # Populate the treeview with data for the entire week
    for row in range(max(len(schedule_data[day]) for day in range(7))):
        values = []
        for day in range(7):
            if row < len(schedule_data[day]):
                class_id, class_name, date, starttime, endtime, school, _ = schedule_data[day][row]
                formatted_date = date.strftime("%d-%m-%y")
                values.append(f"{class_id}/{class_name}\n{school}\n{formatted_date}-{starttime}-{endtime}")
            else:
                values.append("")
        tree.insert("", index=tk.END, text="", values=values)
    calculate_totals()

class_name_entry = None
date_entry = None
start_time_entry = None
end_time_entry = None
school_entry = None
rate_entry = None
new_class_window = None
calculate_window = None

def submit_new_class():
    global class_name_entry, date_entry, start_time_entry, end_time_entry, school_entry, rate_entry,new_class_window
    
    class_name = class_name_entry.get()
    date = date_entry.get_date().strftime("%Y-%m-%d")
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    school = school_entry.get()
    rate = rate_entry.get()
    
    # Insert the new class data into the SQL database
    insert_query = "INSERT INTO teaching_schedule (class, date, starttime, endtime, school, rate) VALUES (%s, %s, %s, %s, %s, %s)"
    
    cursor.execute(insert_query, (class_name, date, start_time, end_time, school, rate))
    connection.commit()
    
    # Show a success message
    messagebox.showinfo("New Class", "Class has been added successfully.")
    
    # Close the new class window
    new_class_window.destroy()
    
    # Filter the classes again to update the schedule
    filter_classes()

def open_new_class_window():
    global class_name_entry, date_entry, start_time_entry, end_time_entry, school_entry, rate_entry,new_class_window
    new_class_window = tk.Toplevel(window)
    new_class_window.title("New Class")
    new_class_window.geometry('300x300')
    
    # Create and grid the class name label and entry widgets
    class_name_label = tk.Label(new_class_window, text="Class Name:")
    class_name_label.grid(row=0, column=0, padx=10, pady=10)
    class_name_entry = tk.Entry(new_class_window)
    class_name_entry.grid(row=0, column=1, padx=10, pady=10)
    
    # Create and grid the date label and entry widgets
    date_label = tk.Label(new_class_window, text="Date:")
    date_label.grid(row=1, column=0, padx=10, pady=10)
    date_entry = DateEntry(new_class_window, width=12, date_pattern="yyyy-mm-dd", font="Arial 12")
    date_entry.set_date(datetime.datetime.now().date())
    date_entry.grid(row=1, column=1, padx=10, pady=10)
    
    # Create and grid the start time label and entry widgets
    start_time_label = tk.Label(new_class_window, text="Start Time (HH:MM:SS):")
    start_time_label.grid(row=2, column=0, padx=10, pady=10)
    start_time_entry = tk.Entry(new_class_window)
    start_time_entry.grid(row=2, column=1, padx=10, pady=10)
    
    # Create and grid the end time label and entry widgets
    end_time_label = tk.Label(new_class_window, text="End Time (HH:MM:SS):")
    end_time_label.grid(row=3, column=0, padx=10, pady=10)
    end_time_entry = tk.Entry(new_class_window)
    end_time_entry.grid(row=3, column=1, padx=10, pady=10)
    
    # Create and grid the school label and entry widgets
    school_label = tk.Label(new_class_window, text="School:")
    school_label.grid(row=4, column=0, padx=10, pady=10)
    school_entry = tk.Entry(new_class_window)
    school_entry.grid(row=4, column=1, padx=10, pady=10)
    
    # Create and grid the rate label and entry widgets
    rate_label = tk.Label(new_class_window, text="Rate:")
    rate_label.grid(row=5, column=0, padx=10, pady=10)
    rate_entry = tk.Entry(new_class_window)
    rate_entry.insert(tk.END, "450")
    rate_entry.grid(row=5, column=1, padx=10, pady=10)
    
    # Create and grid the submit button
    submit_button = tk.Button(new_class_window, text="Submit", command=submit_new_class)
    submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

def delete_class():
    # Create a new window for deleting a class
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Class")
    delete_window.geometry('300x200')
    
    # Create and pack the class ID label and entry widgets
    class_id_label = tk.Label(delete_window, text="Class ID (use comma for multiple entry):")
    class_id_label.pack(pady = 20)
    class_id_entry = tk.Entry(delete_window)
    class_id_entry.pack(pady = 20)
    
    def delete():
        # Get the class IDs from the entry box
        class_ids = class_id_entry.get().split(",")
        
        for class_id in class_ids:
            # Delete each class with the given IDs from the database

            try:
                # Execute the DELETE query
                delete_query = "DELETE FROM teaching_schedule WHERE id = %s"
                cursor.execute(delete_query, (class_id,))
                connection.commit()
                messagebox.showinfo("Class Deletion", "Class deleted successfully")
            
            except mysql.connector.Error as error:
                # Display an error message
                messagebox.showerror("Class Deletion", f"Error deleting class: {error}")
        
        # Close the delete window
        delete_window.destroy()
    
    # Create and pack the delete button
    delete_button = tk.Button(delete_window, text="Delete", command=delete)
    delete_button.pack(pady = 20)


def edit_class():
    # Create a new window for editing
    edit_window = tk.Toplevel(window)
    edit_window.title("Edit Class")
    edit_window.geometry('400x500')
    

    # Create and pack the class ID label and entry widgets
    class_id_label = tk.Label(edit_window, text="Class ID:")
    class_id_label.pack()
    class_id_entry = tk.Entry(edit_window)
    class_id_entry.pack()

    def get_class_info():
        # Retrieve the class ID entered by the user
        class_id = class_id_entry.get()

        # Fetch the class information from the database based on the class ID
        query = "SELECT * FROM teaching_schedule WHERE id = %s"
        cursor.execute(query, (class_id,))
        class_info = cursor.fetchone()

        if class_info:
            # Create and pack the class name label and entry widgets
            class_name_label = tk.Label(edit_window, text="Class Name:")
            class_name_label.pack()
            class_name_entry = tk.Entry(edit_window)
            class_name_entry.insert(tk.END, class_info[1])
            class_name_entry.pack()

            # Create and pack the date label and entry widgets
            date_label = tk.Label(edit_window, text="Date:")
            date_label.pack()
            date_entry = DateEntry(edit_window, width=12, date_pattern="dd-mm-yy", font="Arial 12")
            date_entry.set_date(class_info[2])
            date_entry.pack()

            # Create and pack the start time label and entry widgets
            start_time_label = tk.Label(edit_window, text="Start Time:")
            start_time_label.pack()
            start_time_entry = tk.Entry(edit_window)
            start_time_entry.insert(tk.END, class_info[3])
            start_time_entry.pack()

            # Create and pack the end time label and entry widgets
            end_time_label = tk.Label(edit_window, text="End Time:")
            end_time_label.pack()
            end_time_entry = tk.Entry(edit_window)
            end_time_entry.insert(tk.END, class_info[4])
            end_time_entry.pack()

            # Create and pack the school label and entry widgets
            school_label = tk.Label(edit_window, text="School:")
            school_label.pack()
            school_entry = tk.Entry(edit_window)
            school_entry.insert(tk.END, class_info[5])
            school_entry.pack()

            # Create and pack the rate label and entry widgets
            rate_label = tk.Label(edit_window, text="Rate:")
            rate_label.pack()
            rate_entry = tk.Entry(edit_window)
            rate_entry.insert(tk.END, class_info[6])
            rate_entry.pack()

            def update_class():
                # Retrieve the updated values from the entry widgets
                class_name = class_name_entry.get()
                date = date_entry.get_date()
                start_time = start_time_entry.get()
                end_time = end_time_entry.get()
                school = school_entry.get()
                rate = rate_entry.get()

                # Update the class information in the database
                query = "UPDATE teaching_schedule SET class = %s, date = %s, starttime = %s, endtime = %s, school = %s, rate = %s WHERE id = %s"
                cursor.execute(query, (class_name, date, start_time, end_time, school, rate, class_id))
                connection.commit()

                # Close the edit window
                edit_window.destroy()

                # Refresh the class schedule display
                filter_classes()

            # Create and pack the update button
            update_button = tk.Button(edit_window, text="Update", command=update_class)
            update_button.pack()
        else:
            messagebox.showerror("Error", "Invalid Class ID")

    # Create and pack the get info button
    get_info_button = tk.Button(edit_window, text="Get Info", command=get_class_info)
    get_info_button.pack()


def duplicate_classes():
    # Create a new window for editing
    duplicate_window = tk.Toplevel(window)
    duplicate_window.title("Edit Class")
    duplicate_window.geometry('400x500')
    

    # Create and pack the class ID label and entry widgets
    class_id_label = tk.Label(duplicate_window, text="Class ID:")
    class_id_label.pack()
    class_id_entry = tk.Entry(duplicate_window)
    class_id_entry.pack()

    def get_class_info():
        # Retrieve the class ID entered by the user
        class_id = class_id_entry.get()

        # Fetch the class information from the database based on the class ID
        query = "SELECT * FROM teaching_schedule WHERE id = %s"
        cursor.execute(query, (class_id,))
        class_info = cursor.fetchone()

        if class_info:
            # Create and pack the class name label and entry widgets
            class_name_label = tk.Label(duplicate_window, text="Class Name:")
            class_name_label.pack()
            class_name_entry = tk.Entry(duplicate_window)
            class_name_entry.insert(tk.END, class_info[1])
            class_name_entry.pack()

            # Create and pack the date label and entry widgets
            date_label = tk.Label(duplicate_window, text="Date:")
            date_label.pack()
            date_entry = DateEntry(duplicate_window, width=12, date_pattern="dd-mm-yy", font="Arial 12")
            date_entry.set_date(class_info[2])
            date_entry.pack()

            # Create and pack the start time label and entry widgets
            start_time_label = tk.Label(duplicate_window, text="Start Time:")
            start_time_label.pack()
            start_time_entry = tk.Entry(duplicate_window)
            start_time_entry.insert(tk.END, class_info[3])
            start_time_entry.pack()

            # Create and pack the end time label and entry widgets
            end_time_label = tk.Label(duplicate_window, text="End Time:")
            end_time_label.pack()
            end_time_entry = tk.Entry(duplicate_window)
            end_time_entry.insert(tk.END, class_info[4])
            end_time_entry.pack()

            # Create and pack the school label and entry widgets
            school_label = tk.Label(duplicate_window, text="School:")
            school_label.pack()
            school_entry = tk.Entry(duplicate_window)
            school_entry.insert(tk.END, class_info[5])
            school_entry.pack()

            # Create and pack the rate label and entry widgets
            rate_label = tk.Label(duplicate_window, text="Rate:")
            rate_label.pack()
            rate_entry = tk.Entry(duplicate_window)
            rate_entry.insert(tk.END, class_info[6])
            rate_entry.pack()

            def duplicate_new_class():
                # Retrieve the updated values from the entry widgets
                class_name = class_name_entry.get()
                date = date_entry.get_date()
                start_time = start_time_entry.get()
                end_time = end_time_entry.get()
                school = school_entry.get()
                rate = rate_entry.get()

                # Update the class information in the database
                query = "INSERT INTO teaching_schedule (class, date, starttime, endtime, school, rate) VALUES (%s, %s, %s, %s, %s, %s)"
                
                cursor.execute(query, (class_name, date, start_time, end_time, school, rate))
                connection.commit()

                # Close the edit window
                duplicate_window.destroy()

                # Refresh the class schedule display
                filter_classes()

            # Create and pack the update button
            duplicate_button = tk.Button(duplicate_window, text="Update", command=duplicate_new_class)
            duplicate_button.pack()
        else:
            messagebox.showerror("Error", "Invalid Class ID")

    # Create and pack the get info button
    get_info_button = tk.Button(duplicate_window, text="Get Info", command=get_class_info)
    get_info_button.pack()
    
def calculate_hours():
    global calculate_window
    calculate_window = tk.Toplevel(window)
    calculate_window.title("Calculate Hours")
    calculate_window.geometry('400x300')
    
    # Create a label and combobox for selecting the month
    month_label = tk.Label(calculate_window, text="Select Month:")
    month_label.pack()
    
    month_var = tk.StringVar()
    month_combobox = ttk.Combobox(calculate_window, textvariable=month_var, state="readonly")
    month_combobox['values'] = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    month_combobox.pack(pady = 5)
    
    query = "SELECT DISTINCT school FROM teaching_schedule"
    cursor.execute(query)
    schools = cursor.fetchall()
    
    school_var = tk.StringVar()
    school_combobox = ttk.Combobox(calculate_window, textvariable=school_var, state="readonly")
    school_combobox['values'] = schools
    school_combobox.pack(pady = 5)

    
    # Create a button to calculate the hours
    calculate_button = tk.Button(calculate_window, text="Calculate", command=lambda: calculate_hours_worked(month_var.get(),school_var.get()))
    calculate_button.pack(pady = 10)

import datetime

total_monthly_hours = None
avg_rate_label = None
salary_label = None

def calculate_hours_worked(selected_month, selected_school):
    global total_monthly_hours, avg_rate_label, salary_label,calculate_window
    
    # Extract the month from the selected month string
    month_number = datetime.datetime.strptime(selected_month, "%B").month
    
    # Perform SQL query to fetch classes from the selected month and school
    query = "SELECT * FROM teaching_schedule WHERE MONTH(date) = %s AND school = %s"
    cursor.execute(query, (month_number, selected_school))
    classes = cursor.fetchall()
    
    total_hours = 0
    
    # Calculate total hours worked
    for class_data in classes:
        start_time = class_data[3]
        end_time = class_data[4]
        
        # Calculate the difference in hours between start and end times
        hours_worked = (end_time - start_time).total_seconds() / 3600
        total_hours += hours_worked
        total_hours = round(total_hours,2)
    
    # Update the total monthly hours label
    if total_monthly_hours:
        total_monthly_hours["text"] = f"Total Hours Worked in {selected_month}: {total_hours} hours"
    else:
        total_monthly_hours = tk.Label(calculate_window, text=f"Total Hours Worked in {selected_month}: {total_hours} hours")
        total_monthly_hours.pack(pady=10)
    
    # Calculate the average rate (if applicable)
    avg_rate = int(classes[0][-1]) if classes else 0
    
    # Update the average rate label
    if avg_rate_label:
        avg_rate_label["text"] = f"The Average Rate is {avg_rate}.000 /1hr"
    else:
        avg_rate_label = tk.Label(calculate_window, text=f"The Average Rate is {avg_rate}.000 /1hr")
        avg_rate_label.pack(pady=10)
    
    # Calculate the salary
    salary = avg_rate * total_hours
    
    # Update the salary label
    if salary_label:
        salary_label["text"] = f"The salary of {selected_month} from {selected_school} is {salary:,} VND"
    else:
        salary_label = tk.Label(calculate_window, text=f"The salary of {selected_month} from {selected_school} is {salary:,} VND")
        salary_label.pack(pady=10)


def copy_classes():
    def get_classes():
        selected_date = calendar.get_date()
        selected_datetime = datetime.datetime.strptime(selected_date, "%m/%d/%y")
        start_date = selected_datetime - datetime.timedelta(days=selected_datetime.weekday())
        end_date = start_date + datetime.timedelta(days=6)
        query = "SELECT * FROM teaching_schedule WHERE date >= %s AND date <= %s"
        cursor.execute(query, (start_date.date(), end_date.date()))
        classes = cursor.fetchall()
        display_classes(classes)

    def display_classes(classes):
        class_frame = ttk.Frame(new_window)
        class_frame.pack(pady=10)

        for i, class_info in enumerate(classes):
            class_name = class_info[0:3]
            class_checkbox = ttk.Checkbutton(class_frame, text=class_name)
            class_checkbox.grid(row=i, column=0, sticky='w')
            class_checkboxes.append((class_info, class_checkbox))

    def copy_selected_classes():
        selected_date = calendar.get_date()
        selected_datetime = datetime.datetime.strptime(selected_date, "%m/%d/%y")
        start_date = selected_datetime - datetime.timedelta(days=selected_datetime.weekday())
        end_date = start_date + datetime.timedelta(days=6)
        selected_classes = []
        for class_info, checkbox in class_checkboxes:
            if checkbox.instate(['selected']):
                selected_classes.append(class_info)
        copy_to_second_week(selected_classes, start_date, end_date)

    def copy_to_second_week(classes, start_date, end_date):
        for class_info in classes:
            *_, class_name, date, start_time, end_time, school, rate = class_info
            class_date_str = date.strftime("%Y-%m-%d")  # Convert the date to string format
            class_date = datetime.datetime.strptime(class_date_str, "%Y-%m-%d")
            day_difference = (class_date - start_date).days
            new_date = start_date + datetime.timedelta(days=day_difference + 7)  # Add 7 days to the original class date
            new_date_str = new_date.strftime("%Y-%m-%d")  # Convert the new date to string format
            query = "INSERT INTO teaching_schedule (class, date, starttime, endtime, school, rate) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (class_name, new_date_str, start_time, end_time, school, rate))
            # Commit the changes to the database
            connection.commit()

    new_window = tk.Toplevel()
    new_window.title("New Window")

    calendar_frame = ttk.Frame(new_window)
    calendar_frame.pack(pady=10)

    calendar = Calendar(calendar_frame, selectmode='day')
    calendar.grid(row=0, column=0, padx=10)

    button_frame = ttk.Frame(new_window)
    button_frame.pack(pady=10)

    get_classes_button = ttk.Button(button_frame, text="Get Classes", command=get_classes)
    get_classes_button.grid(row=0, column=0, padx=5)

    copy_classes_button = ttk.Button(button_frame, text="Copy", command=copy_selected_classes)
    copy_classes_button.grid(row=0, column=1, padx=5)

    class_checkboxes = []

def calculate_totals():
    selected_date = cal.get_date()
    selected_date_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
    month = selected_date_obj.month

    total_hours = 0
    total_money = 0
    
    # Perform SQL query to fetch classes from the selected month
    query = "SELECT * FROM teaching_schedule WHERE MONTH(date) = %s"
    cursor.execute(query, (month,))
    classes = cursor.fetchall()
    
    # Calculate total hours worked and total expected money
    for class_data in classes:
        start_time = class_data[3]
        end_time = class_data[4]

        # Calculate the difference in hours between start and end times
        hours_worked = (end_time - start_time).total_seconds() / 3600
        total_hours += hours_worked
    
    total_money = total_hours * 450000
    total_hours = round(total_hours,2)

    # Update the labels with the calculated values
    total_hours_label.config(text=f"Total Hours Worked: {total_hours}")
    total_money_label.config(text=f"Total Expected Money: {total_money:,} VND")

filter_classes()

# Create a button to filter classes for the selected week
filter_button = tk.Button(window, text="Filter", command=filter_classes, width=10, height=2)
filter_button.pack(pady=10)
 
# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=window.destroy)

# Create a "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add a "New Class" option to the "File" menu
edit_menu.add_command(label="New Class", command=open_new_class_window)

edit_menu.add_command(label="Delete Class", command=delete_class)

edit_menu.add_command(label="Edit Class", command=edit_class)  # Add the Edit Class option



edit_menu.add_separator()

edit_menu.add_command(label = "Copy Classes",command = copy_classes)
edit_menu.add_command(label = "Duplicate Classes",command = duplicate_classes)

edit_menu.add_separator()

edit_menu.add_command(label="Calculate Hours", command=calculate_hours)


# Bind the F5 key event to trigger the filter button's command
window.bind("<F5>", lambda event: filter_classes())
filter_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()

# Close the cursor and connection
# cursor.close()
# connection.close()
