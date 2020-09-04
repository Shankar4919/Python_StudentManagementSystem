import tkinter as tk  # Tkinter module
from PIL import ImageTk  # Using pillow model for images
from tkinter import ttk, messagebox  # model for combobox and messagebox
from back_end.back_end import *  # import back_end model for database connection
from model.student2 import *  # import model for setter and getter method
from model.user_login import *  # setter and getter of Login

font_type = (('times new roman'), 16)  # global variable
try:
    dbconn=Connection()  # global variable of database connection
except:
    print('Database Connection Error')  # throw error if data connection error
else:                                   # runs if database is connected to the system
    class SampleApp(tk.Tk):             # main window
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)   # types of variable
            self.geometry('1350x800+100+0')
            self._frame = None
            self.switch_frame(login_page)       # home frame
            self.resizable(False,False)         # disable window minimize function

        def switch_frame(self, frame_class):  # method for switching frames
            new_frame = frame_class(self)
            if self._frame is not None:
                self._frame.destroy()
            self._frame = new_frame
            self._frame.pack()


    class login_page(tk.Frame):  # login class
        def __init__(self, master):
            tk.Frame.__init__(self, master)
            self.fm_3 = tk.Frame(master)  # frame for background
            self.fm_3.place(x=0, y=0, width=1350, height=800)
            self.btn_img = ImageTk.PhotoImage(file='image2/wall_png.png')  # image for background
            ad_lb1 = tk.Label(self.fm_3, image=self.btn_img)  # inserting image
            ad_lb1.place(x=0, y=0, relheight=1, relheigh=1)  # setting position

        # exit button ===================================================================================
            hom_btn = tk.Button(self.fm_3, text='Exit', fg='white', font=('times new roman', 16),
                                cursor='hand2', bg='red', width=7,command=master.destroy)
            hom_btn.place(x=2, y=0)
        # =============================login frame===================================================================
            self.fm_4 = tk.Frame(self.fm_3)
            self.fm_4.place(x=450, y=170, width=460, height=400)
            leb = tk.Label(self.fm_4, text='Admin Login', fg='orange', font=('Helvetic', 30, 'bold'))
            leb.place(x=60, y=20)
            leb_1 = tk.Label(self.fm_4, text='Develop by Shankar Tamang', fg='orange', font=('times', 16))
            leb_1.place(x=60, y=80)

        # ================================= pop-up message ========================================================
            self.pop_up = tk.Label(self.fm_4, text='', fg='red', font=('times', 14))
            self.pop_up.place(x=120, y=130)  # label for error popup

            self.usr_img = ImageTk.PhotoImage(file='image2/usr_1.png')  # using image in user label
            ad_lb3 = tk.Label(self.fm_4, image=self.usr_img)
            ad_lb3.place(x=70, y=180)
            self.usr_enty = tk.Entry(self.fm_4, font=('times new roman', 20), bg='azure')
            self.usr_enty.place(x=120, y=180)

            self.psw_img = ImageTk.PhotoImage(file='image2/pass_1.png') # using image in password label
            ad_lb4 = tk.Label(self.fm_4, image=self.psw_img)
            ad_lb4.place(x=70, y=250)
            self.psw_enty = tk.Entry(self.fm_4, font=('times new roman', 20), bg='azure', show='*')
            self.psw_enty.place(x=120, y=250)

        # ======button for login ================================================================================
            ad_btn = tk.Button(self.fm_3, text='Login', font=('times', 16), cursor='hand2', bg='orange',
                               command=self.verification, fg='white')
            ad_btn.place(x=580, y=540, width=200, height=50)

        # ====login_verification========================================================================
        def verification(self):
            while True:
                verify = login_detail(self.usr_enty.get(), self.psw_enty.get())
                query = 'select * from admin_login where username = %s and password = %s'
                values = (verify.get_username(), verify.get_password())
                rows = dbconn.user_login(query, values)
                if rows:  # switch frame to manage_student if username in row
                    self.master.switch_frame(manage_student)
                elif verify.get_username() == '' or verify.get_password() == '':
                    self.pop_up['text'] = 'Please fill all the entries!'
                else:
                    self.pop_up['text'] = 'Invalid Entry!'
                break

        # destroying frames after switching to new frame===============================================================
        def destroy(self):
            self.fm_3.destroy()
            self.fm_4.destroy()

    # student_management frame ===========================================================================
    class manage_student(tk.Frame):  # student management class
        def __init__(self, master):
            tk.Frame.__init__(self, master)
            self.admission = tk.Frame(master, bd=0, bg='Royal blue4')
            self.admission.place(x=0, y=0, height=55, width=1350)

        # exit button and title ==========================================================================
            hom_btn = tk.Button(self.admission, text='Exit', fg='white', font=('times new roman', 17),
                                cursor='hand2', bg='red', width=7, command=master.destroy)
            hom_btn.pack(side=tk.LEFT)

            user_lb1 = tk.Label(self.admission, text='Student Management System',
                                font=("times new roman", 28, 'bold'),bd=2,relief=tk.RIDGE,
                                bg='royal blue4', fg='white',height=10)
            user_lb1.pack(side=tk.TOP,fill=tk.X)

        # Desk board frame not to delete ======================================================================
            self.manage_desk=tk.Frame(master,bd=1,relief=tk.RIDGE,bg='steel blue')
            self.manage_desk.place(x=0,y=55,width=100,height=740)

            # ===== creating button in desk board ====================================
        # button for mange_student in desk board ==================================================

            self.stu_desk_frame=tk.Frame(self.manage_desk,bg='royal blue4',width=100,height=100)
            self.stu_desk_frame.place(x=0,y=80)
            self.stu_image = ImageTk.PhotoImage(file='image2/manage student.png')
            self.stu_button = tk.Button(self.stu_desk_frame, image=self.stu_image,width=92,cursor='hand2',
                                        activebackground='royal blue4',command=self.message_info)
            self.stu_button.place(x=0, y=0, relheight=1, relheigh=1)
            stu_lb = tk.Label(self.manage_desk, text='Manage Student', font=('times', 11),
                             bg='steel blue')
            stu_lb.place(x=0, y=70)

        # button for change password in desk board ====================================================
            change_psw = tk.Label(self.manage_desk, text='Change Password', font=('times', 10),
                                bg='steel blue')
            change_psw.place(x=0, y=280)

            self.change_desk_frame = tk.Frame(self.manage_desk, bg='royal blue4', width=100, height=100)
            self.change_desk_frame.place(x=0, y=300)
            self.change_pass = ImageTk.PhotoImage(file='image2/change_password.png')
            change_btn = tk.Button(self.change_desk_frame, image=self.change_pass, width=92, cursor='hand2',
                                   activebackground='royal blue4', command=lambda:master.switch_frame(change_password))
            change_btn.place(x=0, y=0, relheight=1, relheigh=1)

        # button for logout in desk board ===============================================================
            log_out = tk.Label(self.manage_desk, text='Logout', font=('times', 12),
                                bg='steel blue')
            log_out.place(x=0, y=480)

            self.logout_desk_frame = tk.Frame(self.manage_desk, bg='royal blue4', width=100, height=100)
            self.logout_desk_frame.place(x=0, y=500)
            self.logout_image = ImageTk.PhotoImage(file='image2/logout.png')
            logout_btn = tk.Button(self.logout_desk_frame, image=self.logout_image, width=92, cursor='hand2',
                                   activebackground='royal blue4',command=lambda:master.switch_frame(login_page))
            logout_btn.place(x=0, y=0, relheight=1, relheigh=1)


        # management frame
            self.manage_frame = tk.Frame(master, bd=4, relief=tk.RIDGE, bg='light steel blue')
            self.manage_frame.place(x=110, y=80, width=640, height=685)
            # management title

            title = tk.Label(self.manage_frame, text='Manage Student', font=('times', 24, 'bold'),
                             bg='light steel blue')
            title.place(x=200, y=10)

            canvas = tk.Canvas(self.manage_frame)
            canvas.place(x=0, y=60, height=4, width=632)

            # manage labels and entries
            roll = tk.Label(self.manage_frame, text='Roll No.', font=font_type, bg='light steel blue')
            roll.place(x=10, y=100)
            self.roll_ent = tk.Entry(self.manage_frame, font=('times',14))
            self.roll_ent.place(x=100, y=100)

            name = tk.Label(self.manage_frame, text='Name', font=font_type, bg='light steel blue')
            name.place(x=350, y=100)
            self.name_ent = tk.Entry(self.manage_frame,font=('times',14))
            self.name_ent.place(x=430, y=100)

            gender = tk.Label(self.manage_frame, text='Gender', font=font_type, bg='light steel blue')
            gender.place(x=10, y=180)
            self.gender_combo = tk.ttk.Combobox(self.manage_frame, font=('times',12), state='readonly')
            self.gender_combo['values'] = ('Male', 'Female', 'Other')
            self.gender_combo.place(x=100, y=180)

            dob = tk.Label(self.manage_frame, text='D.O.B', font=font_type, bg='light steel blue')
            dob.place(x=350, y=180)
            self.dob_ent = tk.Entry(self.manage_frame, font=('times',14))
            self.dob_ent.place(x=430, y=180)

            title_dob = tk.Label(self.manage_frame, text='(YYYY/M/D)', font=('times', 12),bg='light steel blue')
            title_dob.place(x=430, y=210)

            stu_class = tk.Label(self.manage_frame, text='Class', font=font_type, bg='light steel blue')
            stu_class.place(x=10, y=260)
            self.class_ent = tk.Entry(self.manage_frame, font=('times',14))
            self.class_ent.place(x=100, y=260)

            email = tk.Label(self.manage_frame, text='Email', font=font_type, bg='light steel blue')
            email.place(x=350, y=260)
            self.email_ent = tk.Entry(self.manage_frame, font=('times',14))
            self.email_ent.place(x=430, y=260)

            contact = tk.Label(self.manage_frame, text='Contact', font=font_type, bg='light steel blue')
            contact.place(x=10, y=340)
            self.contact_ent = tk.Entry(self.manage_frame, font=('times',14))
            self.contact_ent.place(x=100, y=340)

            country = tk.Label(self.manage_frame, text='Country', font=font_type, bg='light steel blue')
            country.place(x=350, y=340)
            self.country_ent = tk.Entry(self.manage_frame, font=('times', 14))
            self.country_ent.place(x=430, y=340)

            city = tk.Label(self.manage_frame, text='City', font=font_type, bg='light steel blue')
            city.place(x=10, y=420)
            self.city_ent = tk.Entry(self.manage_frame, font=('times', 14))
            self.city_ent.place(x=100, y=420)

            address = tk.Label(self.manage_frame, text='Address', font=font_type, bg='light steel blue')
            address.place(x=350, y=420)
            self.address_ent = tk.Text(self.manage_frame, font=('times', 12), width=22, height=3)
            self.address_ent.place(x=430, y=420)

        # button frame ===========================================================================================

            self.button_frame = tk.Frame(self.manage_frame, bd=1, relief=tk.RIDGE,bg='steel blue')
            self.button_frame.place(x=10, y=580, width=610, height=80)

            add = tk.Button(self.button_frame, text='Add', width=8, font=('times', 21, 'bold'), cursor='hand2',
                            activebackground='light steel blue', bg='royal blue4',fg='white',command=self.add_student)
            add.pack(side=tk.LEFT, padx=4)
            delete = tk.Button(self.button_frame, text='Delete', width=8, font=('times', 21, 'bold'), cursor='hand2',
                               activebackground='light steel blue', bg='royal blue4',fg='white',command=self.delete)
            delete.pack(side=tk.LEFT, padx=4)
            Update = tk.Button(self.button_frame, text='Update', width=8, font=('times', 20, 'bold'), cursor='hand2',
                               activebackground='light steel blue', bg='royal blue4',fg='white',command=self.update)
            Update.pack(side=tk.LEFT, padx=4)
            Clear = tk.Button(self.button_frame, text='Clear', width=8, font=('times', 20, 'bold'), cursor='hand2',
                              activebackground='light steel blue',bg='royal blue4',fg='white',command=self.clear)
            Clear.pack(side=tk.LEFT, padx=4)

        # info_frame ================================================================================================
            self.info_frame = tk.Frame(master, bd=4, relief=tk.RIDGE, bg='light steel blue')
            self.info_frame.place(x=760, y=80, width=570, height=685)

        # ================ search details ==================================================================

            search = tk.Label(self.info_frame, text='Search By', font=('times', 20, 'bold'), bg='light steel blue')
            search.grid(row=0, column=0, pady=2, padx=20, sticky='w')

            self.search_combo = tk.ttk.Combobox(self.info_frame, width=10, font=('times', 12), state='readonly')
            self.search_combo['values'] = ('Roll No.', 'Name', 'Email')
            self.search_combo.grid(row=0, column=1, padx=2, pady=10)

            self.search_ent = tk.Entry(self.info_frame, font=('times', 18),width=20)
            self.search_ent.grid(row=0, column=2, pady=2, padx=20, sticky='w')

            search_btn = tk.Button(self.info_frame, text='Search', width=20, font=('times', 15, 'bold'), cursor='hand2',
                                   activebackground='light steel blue',bg='royal blue4',fg='white',
                                   command=self.search_data)
            search_btn.place(x=20,y=60)

            show_btn = tk.Button(self.info_frame, text='Show All', width=20, font=('times', 15, 'bold'), cursor='hand2',
                                 activebackground='light steel blue',bg='royal blue4',fg='white',
                                 command=self.fetch_data)
            show_btn.place(x=295,y=60)

        # ============================ sort detail ==================================================================
            sort_lb = tk.Label(self.info_frame, text='Sort Roll No.', font=('times', 20, 'bold'),
                               bg='light steel blue')
            sort_lb.place(x=20,y=600)

            self.sort_combo = tk.ttk.Combobox(self.info_frame, width=12, font=('times', 16), state='readonly')
            self.sort_combo['values'] = ('Asc','Desc')
            self.sort_combo.place(x=200,y=605)

            sort_btn = tk.Button(self.info_frame, text='Sort',width=13, font=('times', 16, 'bold'), cursor='hand2',
                                 activebackground='light steel blue',bg='royal blue4',fg='white',
                                 command=self.sort_data)
            sort_btn.place(x=380, y=600)

        # ================ table_frame with treeview ==================================================================

            self.table1_Frame = tk.Frame(self.info_frame, bd=4, relief=tk.RIDGE)
            self.table1_Frame.place(x=10, y=120, width=540, height=430)

            scroll_x = tk.Scrollbar(self.table1_Frame, orient=tk.HORIZONTAL)
            scroll_y = tk.Scrollbar(self.table1_Frame, orient=tk.VERTICAL)
            self.Student_table = tk.ttk.Treeview(self.table1_Frame, columns=(
            'roll', 'name', 'gender', 'dob','class', 'email','contact','country','city','address'),
                                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
            scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
            scroll_x.config(command=self.Student_table.xview)
            scroll_y.config(command=self.Student_table.yview)
            self.Student_table.heading('roll', text='Roll No.')
            self.Student_table.heading('name', text='Name')
            self.Student_table.heading('gender', text='Gender')
            self.Student_table.heading('dob', text='D.O.B')
            self.Student_table.heading('class', text='Class')
            self.Student_table.heading('email', text='Email')
            self.Student_table.heading('contact', text='Contact')
            self.Student_table.heading('country',text='Country')
            self.Student_table.heading('city',text='City')
            self.Student_table.heading('address', text='Address')

            self.Student_table['show'] = 'headings'
            self.Student_table.column('roll', width=80)
            self.Student_table.column('name', width=80)
            self.Student_table.column('gender', width=80)
            self.Student_table.column('dob', width=80)
            self.Student_table.column('class',width=80)
            self.Student_table.column('email', width=80)
            self.Student_table.column('contact', width=80)
            self.Student_table.column('country', width=80)
            self.Student_table.column('city', width=80)
            self.Student_table.column('address', width=80)
            self.Student_table.pack(fill=tk.BOTH, expand=1)

            # using bind bind function to call Button Event
            self.Student_table.bind('<ButtonRelease-1>', self.get_data)

            self.fetch_data()  # fetch all datas from database in Treeview

        # methods for uploading datas and photo in database ===========================================================

        def add_student(self):
            try:
                stu = student2(self.roll_ent.get(), self.name_ent.get(), self.gender_combo.get(), self.dob_ent.get(),
                               self.class_ent.get(), self.email_ent.get(), self.contact_ent.get(),
                               self.country_ent.get(), self.city_ent.get(), self.address_ent.get('1.0', tk.END))

                if stu.get_roll() == '' or stu.get_name() == '' or stu.get_gender() == '' or stu.get_dob() == '' or \
                        stu.get_stu_class() == '' or stu.get_email() == '' or stu.get_contact() == '' \
                        or stu.get_country() == '' or \
                        stu.get_city() == '' or stu.get_address() == '':
                    messagebox.showerror('error', 'Please Fill all the entries and contact no. must be int')
                else:
                    query = 'insert into student_management values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                    values = (stu.get_roll(), stu.get_name(), stu.get_gender(), stu.get_dob(), stu.get_stu_class(),
                              stu.get_email(), stu.get_contact(), stu.get_country(), stu.get_city(),
                              stu.get_address())
                    dbconn.insert(query, values)
                    self.fetch_data()  # fetch new added data in treeview
                    self.clear()  # clears entries after adding
                    messagebox.showinfo('Info', 'Data Inserted Successfully!')
            except:
                messagebox.showerror("Error","Must be unique integer roll no, contact and email!")



        # ======== fetching data from mysql =========================================================

        def fetch_data(self):
            stu = student2(self.roll_ent.get(), self.name_ent.get(), self.gender_combo.get(), self.dob_ent.get(),
                           self.class_ent.get(), self.email_ent.get(), self.contact_ent.get(),
                           self.country_ent.get(),
                           self.city_ent.get(), self.address_ent.get('1.0', tk.END))
            query = 'select * from student_management'
            rows = dbconn.select(query)
            if len(rows) != 0:  # if length of row is not equal to zero than there will be some data
                self.Student_table.delete(
                    *self.Student_table.get_children())  # deleting children element from Student_table
                for row in rows:  # iteration for loop, with this loop we will store the datas from fetch data
                    self.Student_table.insert('', tk.END, values=row)

        # =========== function for clearing entered entry =======================================================

        def clear(self):
            self.roll_ent.delete('0', tk.END)
            self.name_ent.delete('0', tk.END)
            self.gender_combo.set('')
            self.dob_ent.delete('0', tk.END)
            self.class_ent.delete('0',tk.END)
            self.email_ent.delete('0', tk.END)
            self.contact_ent.delete('0', tk.END)
            self.country_ent.delete('0', tk.END)
            self.city_ent.delete('0', tk.END)
            self.address_ent.delete('1.0', tk.END)

        # ============ function to update data ===================================================================
        def update(self):
            stu = student2(self.roll_ent.get(), self.name_ent.get(), self.gender_combo.get(), self.dob_ent.get(),
                           self.class_ent.get(), self.email_ent.get(), self.contact_ent.get(),
                           self.country_ent.get(), self.city_ent.get(), self.address_ent.get('1.0', tk.END))
            if stu.get_roll() == '' or stu.get_name() == '' or stu.get_gender() == '' or stu.get_dob() == '' or \
                    stu.get_stu_class() == '' or stu.get_email() == '' or stu.get_contact() == '' \
                    or stu.get_country() == '' or stu.get_city() == '' or stu.get_address() == '':
                messagebox.showerror('error', 'Please Fill all the entries')
            else:
                query = 'update student_management set name=%s,gender=%s,dob=%s,class=%s,email=%s,contact=%s,' \
                        'country=%s,city=%s,address=%s where roll=%s'
                values = (stu.get_name(), stu.get_gender(), stu.get_dob(), stu.get_stu_class(),
                          stu.get_email(), stu.get_contact(), stu.get_country(), stu.get_city(),
                          stu.get_address(), stu.get_roll())
                dbconn.update(query, values)
                self.clear()  # clear the entries after deleting
                self.fetch_data()  # show new data after updating in treeview
                messagebox.showinfo('Info', 'Data Updated Successfully!')

        # ============ function to delete data ===================================================================
        def delete(self):
            stu = student2(self.roll_ent.get(), self.name_ent.get(), self.gender_combo.get(), self.dob_ent.get(),
                           self.class_ent.get(), self.email_ent.get(), self.contact_ent.get(),
                           self.country_ent.get(), self.city_ent.get(), self.address_ent.get('1.0', tk.END))
            if stu.get_roll() == '' or stu.get_name() == '' or stu.get_gender() == '' or stu.get_dob() == '' or \
                    stu.get_stu_class() == '' or stu.get_email() == '' or stu.get_contact() == '' \
                    or stu.get_country() == '' or stu.get_city() == '' or stu.get_address() == '':
                messagebox.showerror('error', 'Please Fill all the entries')
            else:
                query = 'delete from student_management where roll=%s'
                values = (stu.get_roll(),)
                dbconn.delete(query, values)
                self.clear()  # clear the entries after deleting
                self.fetch_data()  # show new data after deleting in Treeview
                messagebox.showinfo('Info', 'Data Deleted Successfully!')

        # ===== creating function to fetch data from Treeview to entry field ===================================
        def get_data(self, ev):
            data_row = self.Student_table.focus()  # using focus function in Student_table to attract values of cursor
            content = self.Student_table.item(data_row)  # using data_row value to content
            row = content['values']  # with the help of content fetching all values in row

            stu = student2(self.roll_ent.delete('0',tk.END), self.name_ent.delete('0',tk.END),
                           self.gender_combo.delete('0',tk.END), self.dob_ent.delete('0',tk.END),
                           self.class_ent.delete('0',tk.END), self.email_ent.delete('0',tk.END),
                           self.contact_ent.delete('0',tk.END),self.country_ent.delete('0',tk.END),
                           self.city_ent.delete('0',tk.END), self.address_ent.delete('1.0', tk.END))
            self.roll_ent.insert(tk.END, row[0])
            self.name_ent.insert(tk.END, row[1])
            self.gender_combo.set(row[2])
            self.dob_ent.insert(tk.END, row[3])
            self.class_ent.insert(tk.END,row[4])
            self.email_ent.insert(tk.END, row[5])
            self.contact_ent.insert(tk.END, row[6])
            self.country_ent.insert(tk.END, row[7])
            self.city_ent.insert(tk.END, row[8])
            self.address_ent.insert(tk.END, row[9])

    # Algorithm for Linear search ==================================================================
        # 1. start
        # 2. create function called linear_search with three arguments fetch_value, value and key
        # 3. initialize a empty list with variable name rows
        # 4. loop through fetch_value
        # 5. check whether the iterate value in a given index number is integer or not
        # 6. if condition meets, then check whether the iterate value in a given index is equal to search value or not
        # 7. if condition meets, append the iterate value in empty list
        # 8. if any of these condition is not meet, convert iterated value in given index to capital letter
        # 9. check whether the step 8 is equal to search value which is converted to capital letter
        # 10. if step 9 meets the condition, append the iterated value to empty list
        # 11. return rows
        # 12. stop

        @classmethod
        def linear_search(self,fetch_value, value, key):
            rows = []  # made empty list of rows
            for row in fetch_value:  # it will iterete the fetched values for database
                if type(row[key]) == int:  # check whether the value is integer or not
                    if row[key] == value:  # if value is integer then check whether the value exist or not
                        rows.append(row)  # if value exists then append to empty list
                else:
                    if row[key].upper() == value.upper(): # if value is string than check the value exist or not
                        rows.append(row)  # if value exists then append to empty list
            return rows  # return the list of matching values

        # fetching data according to linear search ==================================================================
        def search_data(self):
            search_by=self.search_combo.get()
            search_value=self.search_ent.get()
            try:
                search_value=int(search_value)
            except ValueError:
                pass

            if search_by == '' or search_value == '':
                messagebox.showerror('Error','Please select all required fields!')
            elif search_by == 'Roll No.' and type(search_value) is str:
                messagebox.showerror('Error','Roll no. should be integer')
            elif search_by == 'Name' and type(search_value) is int:
                messagebox.showerror('Error','Name must be string')
            elif search_by == 'Email' and type(search_value) is int:
                messagebox.showerror('Error','Contact must be integer')
            else:
                query = 'select * from student_management'
                fetch_value=dbconn.select(query)

                if search_by == 'Roll No.':
                    rows=self.linear_search(fetch_value, search_value, 0)
                elif search_by == 'Name':
                    rows = self.linear_search(fetch_value,search_value, 1)
                elif search_by == 'Email':
                    rows=self.linear_search(fetch_value, search_value, 5)
                else:
                    rows=[]
                if len(rows) != 0:  # if length of row is not equal to zero than there will be some data
                    self.Student_table.delete(
                        *self.Student_table.get_children())  # deleting children element from Student_table
                    for row in rows:  # iteration for loop, with this loop we will store the datas from fetch data
                        self.Student_table.insert('', tk.END, values=row)

        # Algorithm for merge sort ====================================================================

        # 1. start
        # 2. create a function call mergeSort with two argument records and ascending
        # 3. set argument ascending equal to boolean value
        # 4. initialize a empty list represent by result
        # 5. check whether the length of records is equal to one
        # 6. if condition meets, return records
        # 7. if conditon is does not meet, divide the lenght of records in absolute two half
        # 8. store the value in variable mid
        # 9. call merge sort with argument records[:mid] and store in varible lefthalf
        # 10. call merge sort with argument records[mid:] and store in varible righthalf
        # 11. create a two variable x and y having 0 value with both
        # 12. use while loop to check the whether x and y is greater than lenght of lefthalf and righthalf respectively
        # 13. if value of lefthalf is greater than righthalf, append the righthalf value to empty list and
        #     increase the value of y with 1
        # 14. if condition is does not meet, append the value of lefthalf to empty list and increase the value of x
        #     with 1
        # 15. now, set result equal to the sum of result and lefthalf[x:]
        # 16. now, set result equal to the sum of result and righthalf[y:]
        # 17. Now, check whether ascending is equal to True or false
        # 18. if condition meets, return result
        # 19. if ascending is equal to False, reverse the result and return result
        # 20. stop


        @classmethod
        def mergeSort(self, records, ascending = True):  # merge sort =======
            result=[]
            if len(records) == 1:
                return records

            mid = len(records)//2
            lefthalf=self.mergeSort(records[:mid])
            righthalf=self.mergeSort(records[mid:])
            x,y=0,0
            while x<len(lefthalf) and y<len(righthalf):
                if lefthalf[x] > righthalf[y]: # < for descending
                    result.append(righthalf[y])
                    y=y+1
                else:
                    result.append(lefthalf[x])
                    x=x+1
            result=result+lefthalf[x:]
            result=result+righthalf[y:]
            if ascending==True: # ascending
                return result
            else:
                result.reverse() # descending
                return result

    # fetching data according to merge sort ==================================================================
        def sort_data(self):
            sort_by = self.sort_combo.get()
            query = 'select * from student_management'
            fetch_value = dbconn.select(query)
            if sort_by=='':
                messagebox.showerror('Error','Sort entry filed is empty!')
            else:
                if sort_by == 'Asc':
                    rows = self.mergeSort(fetch_value, True)
                elif sort_by == 'Desc':
                    rows = self.mergeSort(fetch_value, False)
                else:
                    rows = []
                if len(rows) != 0:  # if length of row is not equal to zero than there will be some data
                    self.Student_table.delete(
                        *self.Student_table.get_children())  # deleting children element from Student_table
                    for row in rows:  # iteration for loop, with this loop we will store the datas from fetch data
                        self.Student_table.insert('', tk.END, values=row)

        # destroying frames =======================================================================================
        def destroy(self):
            self.admission.destroy()
            self.manage_desk.destroy()
            self.manage_frame.destroy()
            self.stu_desk_frame.destroy()
            self.change_desk_frame.destroy()
            self.logout_desk_frame.destroy()
            self.info_frame.destroy()
            self.table1_Frame.destroy()
            self.button_frame.destroy()

        def message_info(self):
            messagebox.showinfo('Info','We are in student management page!')

    # change password class =====================================================================================
    class change_password(tk.Frame):
        def __init__(self,master):
            tk.Frame.__init__(self, master)
            self.fm_3 = tk.Frame(master)  # frame for background
            self.fm_3.place(x=0, y=0, width=1350, height=800)
            self.btn_img = ImageTk.PhotoImage(file='image2/wall_png.png')
            ad_lb1 = tk.Label(self.fm_3, image=self.btn_img)
            ad_lb1.place(x=0, y=0, relheight=1, relheigh=1)

            # exit button ===================================================================================
            hom_ext = tk.Button(self.fm_3, text='Exit', fg='black', font=('times new roman', 18),
                                cursor='hand2', bg='light steel blue', width=10, command=master.destroy,
                                activebackground='red')
            hom_ext.place(x=2, y=1)

            hom_manage_stu = tk.Button(self.fm_3, text='Manage Student', bg='light steel blue', fg='black',
                                       font=('times new roman', 18),command=lambda:master.switch_frame(manage_student),
                                       cursor='hand2', width=14, activebackground='red')
            hom_manage_stu.place(x=150, y=1)

            hom_log = tk.Button(self.fm_3, fg='black', font=('times new roman', 18), text='Logout',cursor='hand2',
                                command=lambda:master.switch_frame(login_page),bg='light steel blue', width=12,
                                activebackground='red')
            hom_log.place(x=350, y=1)

            # =============================login frame===================================================================
            self.fm_4 = tk.Frame(self.fm_3)
            self.fm_4.place(x=440, y=120, width=500, height=510)
            leb = tk.Label(self.fm_4, text='Change Password', fg='orange', font=('Helvetic', 30, 'bold'))
            leb.place(x=60, y=20)
            leb_1 = tk.Label(self.fm_4, text='Develop by Shankar Tamang', fg='orange', font=('times', 16))
            leb_1.place(x=60, y=80)

            usrname = tk.Label(self.fm_4, text="Username", fg='black', font=('Helvetic', 15, 'bold'))
            usrname.place(x=60, y=150)
            self.user_ent1 = tk.Entry(self.fm_4, font=('Helvetic', 16), width=25)
            self.user_ent1.place(x=65, y=190)
            psswod = tk.Label(self.fm_4, text="Current Password", fg='black', font=('Helvetic', 15, 'bold'))
            psswod.place(x=60, y=250)
            self.pass_ent1 = tk.Entry(self.fm_4, font=('Helvetic', 16), width=25, show='*')
            self.pass_ent1.place(x=65, y=290)
            new_psswod = tk.Label(self.fm_4, text="New Password", fg='black', font=('Helvetic', 15, 'bold'))
            new_psswod.place(x=60, y=350)
            self.new_pass_ent2 = tk.Entry(self.fm_4, font=('Helvetic', 16), width=25, show='*')
            self.new_pass_ent2.place(x=65, y=390)

            ad_btn = tk.Button(self.fm_3, text='Done', font=('times', 16), cursor='hand2', bg='orange', fg='white',
                               command=self.insert_change)
            ad_btn.place(x=580, y=600, width=200, height=50)

        def change_verify(self):
            log = login_detail(self.user_ent1.get(), self.new_pass_ent2.get())
            query = 'update admin_login set password=%s where username=%s'
            values = (log.get_password(), log.get_username())
            dbconn.update(query, values)
            messagebox.showinfo('Info', 'Password changed sucessully!')

        def insert_change(self):
            verify = login_detail(self.user_ent1.get(), self.pass_ent1.get())
            if verify.get_username() == '' or verify.get_password() == '' or self.new_pass_ent2.get() == '':
                messagebox.showerror('Error', 'Please fill all the entries!')
            else:
                query = 'select * from admin_login where username = %s and password = %s'
                values = (verify.get_username(), verify.get_password())
                rows = dbconn.user_login(query, values)
                if rows:
                    self.change_verify()
                else:
                    messagebox.showerror('Error', "Your current username and password does not matched.")
            self.change_clear()

        def change_clear(self):
            self.user_ent1.delete('0',tk.END)
            self.pass_ent1.delete('0',tk.END)
            self.new_pass_ent2.delete('0',tk.END)



        def destroy(self):
            self.fm_3.destroy()


    app = SampleApp()
    app.mainloop()
