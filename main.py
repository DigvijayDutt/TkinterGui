import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3

def enter_data():
    tc = terms_status.get()
    if tc=="True":
        firstname = fn_entry.get()
        lastname = ln_entry.get()
        if firstname and lastname:
            title = title_select.get()
            age =  age_box.get()
            nationality = nationality_box.get()
            course = numc_box.get()
            sem = sem_box.get()
            reg = reg_status.get()

            conn = sqlite3.connect('data.db')
            table_create = '''CREATE TABLE IF NOT EXISTS Student_data(
            firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, reg TEXT, course INT, semester INT
            )'''
            conn.execute(table_create)
            data_insert = '''INSERT INTO Student_data(firstname, lastname, title, age, nationality, reg, course, semester) VALUES(?,?,?,?,?,?,?,?)'''
            data_insert_tup =(firstname,lastname,title,age,nationality,reg,course,sem)
            cursor = conn.cursor()
            cursor.execute(data_insert,data_insert_tup)
            conn.commit()
            conn.close()
        else:
            tkinter.messagebox.showwarning(title="Error", message="First and Last Names are required.")
    else:
        tkinter.messagebox.showwarning(title="Error",message="You have have not accepted the Terms & Conditions.")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

user_info = tkinter.LabelFrame(frame, text="User information")
user_info.grid(row=0,column=0, padx=20, pady=20)

first_name = tkinter.Label(user_info, text="First Name")
first_name.grid(row=0,column=0)
fn_entry = tkinter.Entry(user_info)
fn_entry.grid(row=1,column=0)

last_name = tkinter.Label(user_info, text="Last Name")
last_name.grid(row=0,column=1)
ln_entry = tkinter.Entry(user_info)
ln_entry.grid(row=1,column=1)

title = tkinter.Label(user_info, text="Title")
title_select = ttk.Combobox(user_info, values=["Mr.", "Ms.", "Dr.", ""])
title.grid(row=0,column=2)
title_select.grid(row=1,column=2)

age_label = tkinter.Label(user_info, text="Age")
age_box = tkinter.Spinbox(user_info, from_=18, to=110)
age_box.grid(row=3,column=0)
age_label.grid(row=2, column=0)

nationality_label = tkinter.Label(user_info, text="Nationality")
nationality_box = ttk.Combobox(user_info, values=["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"])
nationality_label.grid(row=2, column=1)
nationality_box.grid(row=3,column=1)

for i in user_info.winfo_children():
    i.grid_configure(padx=10, pady=5)

course_info = tkinter.LabelFrame(frame, text="Course information")
course_info.grid(row=1,column=0, padx=20, pady=20, sticky="news")

register_lbl = tkinter.Label(course_info, text="Registration Status:")
reg_status = tkinter.StringVar(value="False")
register_box = tkinter.Checkbutton(course_info, text="Currently Registered", variable=reg_status, onvalue="True", offvalue="False")
register_lbl.grid(row=0, column=0)
register_box.grid(row=1,column=0)

numc_lbl = tkinter.Label(course_info, text="#Completed Courses")
numc_box = tkinter.Spinbox(course_info, from_=0, to="infinity")
numc_lbl.grid(row=0, column=1)
numc_box.grid(row=1,column=1)

sem_lbl = tkinter.Label(course_info, text="#semester")
sem_box = tkinter.Spinbox(course_info, from_=0, to=8)
sem_lbl.grid(row=0, column=2)
sem_box.grid(row=1,column=2)

for i in course_info.winfo_children():
    i.grid_configure(padx=10, pady=5)

terms = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms.grid(row=2,column=0, padx=20, pady=20, sticky="news")

terms_status = tkinter.StringVar()
terms_btn = tkinter.Checkbutton(terms, text="I accept the Terms & Conditions",variable=terms_status, onvalue="True", offvalue="False")
terms_btn.grid(row=0,column=0, padx=10, pady=5)

submit = tkinter.Button(frame, text="Enter Data", command= enter_data)
submit.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()