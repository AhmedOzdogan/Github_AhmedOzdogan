import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
from time import strftime
from tkcalendar import DateEntry
import re
import datetime
import math
from PIL import ImageTk, Image 
import time
import subprocess




# Replace these values with your actual database credentials
db_config = {
    'user': 'root',
    'password': 'Maltepe1997',
    'host': '34.143.170.115',
    'database': 'myschedule'
}

bgcolor = "Black"
fgheadingcolor = "White"
fgcolor = "White"

# Establish the connection
connection = mysql.connector.connect(**db_config)

def login():
    username = str(username_entry.get())
    password = str(password_entry.get())
    
    cursor = connection.cursor()
    query = f"SELECT pin FROM users WHERE username = %s and password = %s"

    cursor.execute(query, (username,password))
    try:
        pin = str(cursor.fetchall()[0][0])
        pin = "`"+pin+"`"
    except:
        pin = None
    if pin is not None:
        
        succesfull_label.configure(text="Succesfull!!") 
        # Run the other Python script
        login_window.destroy()
        main_window()
        
        
    else:
        succesfull_label.configure(text="Username or password is not correct!") 

    
    
cal = None

def signup():
    # Add your sign up logic here
    pass

# Create a Tkinter window
window = tk.Tk()
window.title("Teaching Schedule")
window.resizable(width=False, height=False)
window.configure(bg = bgcolor)

window_height = 930
window_width = 1430

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))-50

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Set the icon for the program (replace 'icon.ico' with your image file)
window.iconbitmap("C:\\Users\\ahmed\\Desktop\\Schedule_Project\\icon.ico")

# Add the rowheight
ttk.Style().theme_use("clam")
ttk.Style().configure("Treeview", 
                      font=("Times New Roman ", 10), 
                      rowheight=80,
)

# Create a Treeview widget
tree = ttk.Treeview(
    window,
    columns=(
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ),
    height=7,
)

# Format the columns
tree.column("#0", width=0, stretch=tk.NO)  # Hide the first (default) column
for day, heading in enumerate(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
):
    tree.column(day, anchor=tk.W)
    tree.heading(day, text=heading)

# Pack the Treeview widget
tree.grid(row=0, 
          column=0, 
          columnspan=7, 
          padx=10, 
          pady=10)

# Create payment frames
money_frame = tk.Frame(window, bg = bgcolor)
money_frame.grid(row=1, 
                 column=1, 
                 columnspan=2, 
                 padx=10, 
                 pady=10)

money_month_frame = tk.Frame(window,bg = bgcolor)
money_month_frame.grid(row=1, 
                       column=4, 
                       columnspan=2, 
                       padx=10, 
                       pady=10)

# Create labels for total hours and total money (weekly)
weekly_label = ttk.Label(
    money_frame, text="Weekly Hours", 
    font=("Times New Roman", 15), 
    foreground=fgheadingcolor, 
    background= bgcolor
)
weekly_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

total_hours_label = ttk.Label(
    money_frame,
    text="Total Hours Worked: ",
    font=("Times New Roman", 12),
    foreground=fgcolor,
    background= bgcolor
)
total_hours_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")

total_money_label = ttk.Label(
    money_frame,
    text="Total Expected Money: $",
    font=("Times New Roman", 12),
    foreground=fgcolor,
    background= bgcolor
)
total_money_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w")

paid_label = ttk.Label(
    money_frame,
    text="Total Received Money: $",
    font=("Times New Roman", 12),
    foreground=fgcolor,
    background= bgcolor
)
paid_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="w")

expected_label = ttk.Label(
    money_frame,
    text="Expected Payment: $",
    font=("Times New Roman", 12),
    foreground=fgcolor,
    background= bgcolor
)
expected_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Create labels for total hours and total money (monthly)
monthly_label = ttk.Label(
    money_month_frame,
    text="Monthly Hours",
    font=("Times New Roman", 15),
    foreground=fgheadingcolor,
    background= bgcolor
)
monthly_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

total_hours_label_month = ttk.Label(
    money_month_frame,
    text="Total Hours Worked: ",
    font=("Times New Roman", 12),
    foreground=fgcolor,
    background= bgcolor
)
total_hours_label_month.grid(
    row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w"
)

total_money_label_month = ttk.Label(
    money_month_frame,
    text="Total Expected Money: $",
    font=("Times New Roman", 12),
    foreground=fgcolor,
    background= bgcolor
)
total_money_label_month.grid(
    row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w"
)

paid_label_month = ttk.Label(
    money_month_frame,
    text="Total Received Money: $",
    font=("Times New Roman", 12),
    foreground=fgcolor,
    background= bgcolor
)
paid_label_month.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="w")

expected_label_month = ttk.Label(
    money_month_frame,
    text="Expected Payment: $",
    font=("Times New Roman", 12),
    foreground=fgcolor,
    background= bgcolor
)
expected_label_month.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Create a calendar frame
calendar_frame = tk.Frame(window,
                          background = bgcolor)
calendar_frame.grid(row=1, 
                    column=2, 
                    columnspan=3, 
                    padx=10, 
                    pady=10)

window.withdraw() 


    
def filter_classes(cal):
    selected_date = cal.get_date()
    selected_datetime = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
    start_date = selected_datetime - datetime.timedelta(
        days=selected_datetime.weekday()
    )
    end_date = start_date + datetime.timedelta(days=6)


    query = "SELECT * FROM {} WHERE date BETWEEN %s AND %s".format(pin)
    cursor.execute(query, (start_date.date(), end_date.date()))


    teaching_schedule_data = cursor.fetchall()
    print(teaching_schedule_data)

    tree.delete(*tree.get_children())

    schedule_data = {day: [] for day in range(7)}

    for row in teaching_schedule_data:
        class_id, class_name, date, starttime, endtime, school, rate, paid = row[:8]
        paid = paid.upper() + " !! " if paid.lower() == "no" else paid.upper()

        day = (date.weekday()) % 7
        schedule_data[day].append(
            (class_id, class_name, date, starttime, endtime, school, rate, paid)
        )

    for day in range(7):
        schedule_data[day].sort(key=lambda x: x[3])

    for row in range(max(len(schedule_data[day]) for day in range(7))):
        values = []

        for day in range(7):
            if row < len(schedule_data[day]):
                (
                    class_id,
                    class_name,
                    date,
                    starttime,
                    endtime,
                    school,
                    rate,
                    paid,
                ) = schedule_data[day][row]
                formatted_date = date.strftime("%d-%m-%y")
                values.append(
                    f"{class_id}~{class_name}~{school}\n{formatted_date} | {starttime} | {endtime}\n{paid}\n{rate}"
                )
            else:
                values.append("")
        tree.insert("", index=tk.END, text="", values=values)

    calculate_totals()

    # Get the column names
    columns = tree["columns"]

    # Get the column names
    columns = tree["columns"]


    
login_py = 10
login_font = "Ink Free"
login_bg = "black"
login_fg = "white"
login_window = tk.Tk()

login_window.title("MySchedule")
login_window.resizable(width=False, height=False)
login_window.configure(bg = login_bg)

login_window_height = 600
login_window_width = 500

screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (login_window_width/2))
y_cordinate = int((screen_height/2) - (login_window_height/2))-50

login_window.geometry("{}x{}+{}+{}".format(login_window_width, login_window_height, x_cordinate, y_cordinate))
# Welcome Label
welcome_label = tk.Label(login_window, text="Welcome to My Schedule", font=(login_font, 25),background=login_bg,fg = login_fg)
welcome_label.pack(pady=(100, 10))

# Username Label and Entry
username_frame = tk.Frame(login_window,background=login_bg)
username_frame.pack(pady = login_py)
username_label = tk.Label(username_frame, text="Username:",font=(login_font, 17),background=login_bg,fg = login_fg)
username_label.pack(pady = login_py,side=tk.LEFT)
username_entry = tk.Entry(username_frame,font=(login_font, 17), width=25,background=login_bg,fg = login_fg)
username_entry.insert(0,"ahmedozdogan")
username_entry.pack(pady = login_py,side=tk.LEFT)

# Password Label and Entry
password_frame = tk.Frame(login_window,background=login_bg)
password_frame.pack(pady = login_py)
password_label = tk.Label(password_frame, text="Password:",font=(login_font, 17),background=login_bg,fg = login_fg)
password_label.pack(pady = login_py,side=tk.LEFT)
password_entry = tk.Entry(password_frame, show="*",font=(login_font, 17), width=25,background=login_bg,fg = login_fg)
password_entry.insert(0,"Ahmed12345")
password_entry.pack(pady = login_py,side=tk.LEFT)

# Login Button
login_btn= tk.PhotoImage(file='C:\\Users\\ahmed\\Desktop\\Schedule_Project\\icons\\login.png')
login_label = ttk.Label(login_window,image=login_btn)
# login_label.pack(pady = login_py)


login_button= tk.Button(login_window, image=login_btn, command = login,
                      borderwidth=0,bg="black")

login_button.pack(pady = login_py)

# Sign Up Button

signup_btn= tk.PhotoImage(file='C:\\Users\\ahmed\\Desktop\\Schedule_Project\\icons\\signup.png')
signup_label = ttk.Label(login_window,image=login_btn)


signup_button= tk.Button(login_window, image=signup_btn,
                      borderwidth=0,bg="black")

signup_button.pack(pady = login_py)

succesfull_label = tk.Label(login_window, font=(login_font, 15),background=login_bg,fg = "red")
succesfull_label.pack(pady=login_py)



refresh_btn= tk.PhotoImage(file='C:\\Users\\ahmed\\Desktop\\Schedule_Project\\refresh.png')
refresh_label = ttk.Label(window,image=refresh_btn)

refres_button= tk.Button(window, image=refresh_btn,command= filter_classes,
                      borderwidth=0,bg="white")
refres_button.grid(row=2, column=2, columnspan=3, padx=10, pady=10)


# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Connection Settings", command=db_info_update)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

# Create "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add options to "Edit" menu
edit_menu.add_command(label="New Class (F1)", command=open_new_class_window)
edit_menu.add_separator()
edit_menu.add_command(label="Copy Classes(F4)", command=copy_classes)
edit_menu.add_separator()
edit_menu.add_command(label="Calculate Hours(F10)", command=calculate_hours)

# Bind key events
key_events = [
    ("<F5>", filter_classes),
    ("<F1>", open_new_class_window),
    ("<F4>", copy_classes),
    ("<F10>", calculate_hours),
]

for event, command in key_events:
    window.bind(event, lambda e, cmd=command: cmd())

tree.bind("<Button-3>", open_info_window)


if __name__ == '__main__':
    login_window.mainloop()



