import sqlite3 as sql
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import ImageTk, Image

# insert entries
def insert():
    insert_window = Tk()
    insert_window.title("Insert")
    insert_window.geometry('300x300')

    first_name_lbl = Label(insert_window, text=" first name ")
    first_name_lbl.grid(column=0, row=0)
    first_name_txt = Entry(insert_window, width=10)
    first_name_txt.grid(column=1, row=0)
    last_name_lbl = Label(insert_window, text=" last name ")
    last_name_lbl.grid(column=0, row=1)
    last_name_txt = Entry(insert_window, width=10)
    last_name_txt.grid(column=1, row=1)
    gender_lbl = Label(insert_window, text=" gender ")
    gender_lbl.grid(column=0, row=2)
    gender_txt = Entry(insert_window, width=10)
    gender_txt.grid(column=1, row=2)
    maths_lbl = Label(insert_window, text=" maths ")
    maths_lbl.grid(column=0, row=3)
    maths_txt = Entry(insert_window, width=10)
    maths_txt.grid(column=1, row=3)
    dsa_lbl = Label(insert_window, text=" dsa ")
    dsa_lbl.grid(column=0, row=4)
    dsa_txt = Entry(insert_window, width=10)
    dsa_txt.grid(column=1, row=4)
    db_lbl = Label(insert_window, text=" dbms ")
    db_lbl.grid(column=0, row=5)
    db_txt = Entry(insert_window, width=10)
    db_txt.grid(column=1, row=5)
    ld_lbl = Label(insert_window, text=" LD ")
    ld_lbl.grid(column=0, row=6)
    ld_txt = Entry(insert_window, width=10)
    ld_txt.grid(column=1, row=6)
    pce_lbl = Label(insert_window, text=" PCE ")
    pce_lbl.grid(column=0, row=7)
    pce_txt = Entry(insert_window, width=10)
    pce_txt.grid(column=1, row=7)

    def submit():
        sql_command = """
                        CREATE TABLE if not exists student(
                        student_id INTEGER PRIMARY KEY,
                        fname VARCHAR(30),
                        lname VARCHAR(30),
                        gender CHAR(1),
                        maths CHAR(2),
                        dsa CHAR(2),
                        dbms CHAR(2),
                        ld CHAR(2),
                        pce CHAR(2) 
                        );
                      """
        # create table if not exists
        cursor.execute(sql_command)

        first_name = first_name_txt.get()
        last_name = last_name_txt.get()
        gender = gender_txt.get()
        maths = maths_txt.get()
        dsa = dsa_txt.get()
        db = db_txt.get()
        ld = ld_txt.get()
        pce = pce_txt.get()

        fn_temp_list = []
        ln_temp_list = []
        gn_temp_list = []
        m_temp_list = []
        ds_temp_list = []
        db_temp_list = []
        l_temp_list = []
        p_temp_list = []

        dict_list_data = {"fname": fn_temp_list,
                          "lname": ln_temp_list,
                          "gender": gn_temp_list,
                          "maths": m_temp_list,
                          "dsa": ds_temp_list,
                          "dbms": db_temp_list,
                          "ld": l_temp_list,
                          "pce": p_temp_list
                          }

        fn_temp_list.append(str(first_name))
        ln_temp_list.append(str(last_name))
        gn_temp_list.append(str(gender))
        m_temp_list.append(str(maths))
        ds_temp_list.append(str(dsa))
        db_temp_list.append(str(db))
        l_temp_list.append(str(ld))
        p_temp_list.append(str(pce))

        dict_list_data["fname"] = fn_temp_list
        dict_list_data["lname"] = ln_temp_list
        dict_list_data["gender"] = gn_temp_list
        dict_list_data["maths"] = m_temp_list
        dict_list_data["dsa"] = ds_temp_list
        dict_list_data["dbms"] = db_temp_list
        dict_list_data["ld"] = l_temp_list
        dict_list_data["pce"] = p_temp_list

        length = int(len(dict_list_data["fname"]))
        for e in range(length):
            format_str = """
                              INSERT INTO student (student_id, 
                              fname, 
                              lname, 
                              gender, 
                              maths, 
                              dsa, 
                              dbms, 
                              ld, 
                              pce) 
                              VALUES (NULL, 
                              "{fname}", 
                              "{lname}", 
                              "{gender}",
                              "{maths}", 
                              "{dsa}", 
                              "{dbms}", 
                              "{ld}", 
                              "{pce}" 
                              );
                              """
            sql_command = format_str.format(fname=dict_list_data["fname"][e],
                                            lname=dict_list_data["lname"][e],
                                            gender=dict_list_data["gender"][e],
                                            maths=dict_list_data["maths"][e],
                                            dsa=dict_list_data["dsa"][e],
                                            dbms=dict_list_data["dbms"][e],
                                            ld=dict_list_data["ld"][e],
                                            pce=dict_list_data["pce"][e]
                                            )

            cursor.execute(sql_command)
        connection.commit()
        # INSERT ONE MORE BUTTON to SUBMIT

    submit_button = Button(insert_window, text="Submit", command=submit)
    submit_button.grid(column=1, row=8)
    back_button = Button(insert_window, text="Back", command=insert_window.destroy)
    back_button.grid(column=1, row=10)
    insert_window.mainloop()

# display all entries
def display_all():
    out_window = Tk()
    out_window.title("Displaying result")
    out_window.geometry('450x300')
    out_text = scrolledtext.ScrolledText(out_window, width=50, height=30)
    out_text.grid(column=0, row=0)
    cursor.execute("""SELECT  * 
                        FROM student ;""")

    for r in cursor:
        roll = str(r[0])
        name = str(r[1] + " " + r[2])
        gender = str(r[3])
        roll_format = "\nStudent roll number : {} ".format(roll)
        name_format = "\n               Name : {} ".format(name)
        gender_format = "\n            Gender: {} ".format(gender)
        out_text.insert(END, roll_format)
        out_text.insert(END, name_format)
        out_text.insert(END, gender_format)
    back_button = Button(out_window, text="Back", command=out_window.destroy)
    back_button.grid(column=1, row=0)
    out_window.mainloop()

# print marks of a student
def query_marks():
    out_window = Tk()
    out_window.title("Displaying result")
    out_window.geometry('200x100')
    roll_lbl = Label(out_window, text=" roll no ")
    roll_lbl.grid(column=0, row=0)
    roll_txt = Entry(out_window, width=10)
    roll_txt.grid(column=1, row=0)

    def get_result():
        temp_roll = roll_txt.get()
        query_result_window = Tk()
        query_result_window.title("displaying result")
        query_result_window.geometry('300x180')
        out_text = Text(query_result_window, width=50, height=50)
        out_text.grid(column=0, row=0)
        format_str = """SELECT student_id, 
                            fname, 
                            lname, 
                            maths, 
                            dsa, 
                            dbms, 
                            ld, 
                            pce
                            FROM student 
                            WHERE 
                            "{}"={} 
                            ;
                            """
        sql_command = format_str.format(temp_roll, "student_id")
        cursor.execute(sql_command)
        data = cursor.fetchall()
        if len(data) == 0:
            messagebox.showinfo("Alert !", "No such entry")
        else:
         cursor.execute(sql_command)
         for r in cursor:
            roll = str(r[0])
            fname = str(r[1])
            lname = str(r[2])
            maths = str(r[3])
            dsa = str(r[4])
            db = str(r[5])
            ld = str(r[6])
            pce = str(r[7])
            roll_format = "\nStudent roll number : {} ".format(roll)
            fname_format = "\n        first Name : {} ".format(fname)
            lname_format = "\n         last Name : {} ".format(lname)
            maths_format = "\n            Maths: {} ".format(maths)
            dsa_format = "\n            DSA: {} ".format(dsa)
            db_format = "\n            DBMS: {} ".format(db)
            ld_format = "\n            LD: {} ".format(ld)
            pce_format = "\n            PCE: {} ".format(pce)
            out_text.insert(END, roll_format)
            out_text.insert(END, fname_format)
            out_text.insert(END, lname_format)
            out_text.insert(END, maths_format)
            out_text.insert(END, dsa_format)
            out_text.insert(END, db_format)
            out_text.insert(END, ld_format)
            out_text.insert(END, pce_format)
        #out_window.mainloop()
    get_button = Button(out_window, text="Get Result", command=get_result)
    get_button.grid(column=1, row=1)
    back_button = Button(out_window, text="Back", command=out_window.destroy)
    back_button.grid(column=1, row=2)
    out_window.mainloop()

# delete one entry
def delete_entry():
    del_window = Tk()
    del_window.title("Displaying result")
    del_window.geometry('200x100')
    roll_lbl = Label(del_window, text=" roll no ")
    roll_lbl.grid(column=0, row=0)
    roll_txt = Entry(del_window, width=10)
    roll_txt.grid(column=1, row=0)

    def delete_click():
        result = messagebox.askquestion("Exit", "Are You Sure?", icon='warning')
        if result == "yes":
            temp_roll = roll_txt.get()
            format_str = """SELECT  * 
                                FROM student WHERE "{}"={};"""  # <-EDIT
            sql_command = format_str.format(temp_roll, "student_id")
            cursor.execute(sql_command)
            data = cursor.fetchall()
            if len(data) == 0:
                messagebox.showerror("Error", "No such entry ")
            else:
                format_str = """DELETE 
                                FROM student 
                                WHERE 
                                "{}"={}
                                ;
                                """
                sql_command = format_str.format(temp_roll, "student_id")
                cursor.execute(sql_command)
                connection.commit()
                format_str = "Entry succesfully DELETED for roll number : {}".format(temp_roll)
                messagebox.showinfo("Notification", format_str)

    del_button = Button(del_window, text="Delete entry", command=delete_click)
    del_button.grid(column=1, row=1)
    back_button = Button(del_window, text="Back", command=del_window.destroy)
    back_button.grid(column=1, row=2)
    del_window.mainloop()

# delete all entries of student table
def delete_all():
    result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
    if result=="yes":
        cursor.execute("""DROP TABLE student;""")
        connection.commit()
        messagebox.showinfo("Notification", "DELETED all entries")

def exit_window():
    result = messagebox.askquestion("Exit", "Are You Sure?", icon='warning')
    if result == "yes":
        window.destroy()

print("[+]Establishing connection to StudentDB")
connection = sql.connect("StudentDB.db")
cursor = connection.cursor()

try:
    window = Tk()
    window.title("STUDENT RESULT SECTION")
    window.geometry('400x350')
    #path to image
    path = "/home/master/Result-logo.jpeg"
    img = ImageTk.PhotoImage(Image.open(path))

    photo = Label(window, image=img)
    photo.grid(column=3, row=6)

    insert_button = Button(window, text="Insert", command=insert)
    insert_button.grid(column=2, row=0)
    display_all_button = Button(window, text="Display All", command=display_all)
    display_all_button.grid(column=2, row=1)
    query_button = Button(window, text="query marks", command=query_marks)
    query_button.grid(column=2, row=2)
    delete_button = Button(window, text="delete entry", command=delete_entry)
    delete_button.grid(column=2, row=3)
    delete_all_button = Button(window, text="delete All", command=delete_all)
    delete_all_button.grid(column=2, row=4)
    exit_button = Button(window, text="Exit", command=exit_window)
    exit_button.grid(column=2, row=5)
    window.mainloop()

except KeyboardInterrupt:
    print("\n[-]Keyboard Interrupt ")
    print("[-]Closing connection to StudentDB")
    connection.close()
    print("Program successfully terminated")

except sql.OperationalError:
    messagebox.showerror("No such table : student")

else:
    print("\n[-]Closing connection to StudentDB")
    connection.close()
    print("Program successfully terminated")

finally:
    connection.close()
