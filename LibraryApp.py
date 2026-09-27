import sqlite3
import tkinter as tk
import atexit
from datetime import datetime, timedelta

mydb = sqlite3.connect("LibraryDatabase.db")
myc = mydb.cursor()

myc.execute("""CREATE TABLE IF NOT EXISTS Books
            (Name TEXT, 
             Publisher TEXT, 
             Number INT,
             Id INT,
             Type TEXT)""")

myc.execute("""CREATE TABLE IF NOT EXISTS Member
             (Firstname TEXT,
             Lastname TEXT,
             Id INT,
             Gender TEXT,
             Age INT,
             Phone TEXT,
             SubExpiry TEXT)""")

myc.execute("""CREATE TABLE IF NOT EXISTS Info
             (PersonId INT,
             BookId INT,
             ReturnTime TEXT)""")

myc.execute("""CREATE TABLE IF NOT EXISTS MemberStats
            (PersonId INT, 
             Age INT,
             DeadLine TEXT,
             EntryTimes INT)""")

myc.execute("""CREATE TABLE IF NOT EXISTS BookStats
            (BookType TEXT, 
             DeadLine TEXT,
             TimesBorrowed INT)""")

root = tk.Tk()
root.title("Library")

width = 600
height = 350

sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()

x = (sc_width - width) // 2
y = (sc_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(True, True)
root.minsize(600,350)
root.maxsize(850,400)
root.config(bg = '#b8b4b0')

f1 = tk.Frame(root,bg='#b8b4b0')
f2 = tk.Frame(root,bg='#b8b4b0')
f3 = tk.Frame(root,bg='#b8b4b0')
f4 = tk.Frame(root,bg='#b8b4b0')
f5 = tk.Frame(root,bg='#b8b4b0')
f6 = tk.Frame(root,bg='#b8b4b0')
fBack = tk.Frame(root,bg='#b8b4b0')
fBack1 = tk.Frame(root,bg='#b8b4b0')
fBack2 = tk.Frame(root,bg='#b8b4b0')
fBack3 = tk.Frame(root,bg='#b8b4b0')
fBack4 = tk.Frame(root,bg='#b8b4b0')
fExtend = tk.Frame(root,bg='#b8b4b0')
opt = tk.Frame(root,bg='#b8b4b0')
fborrow = tk.Frame(root,bg='#b8b4b0')
freturn = tk.Frame(root,bg='#b8b4b0')
ffind = tk.Frame(root,bg='#b8b4b0')
fexit = tk.Frame(root,bg='#b8b4b0')
finfo = tk.Frame(root,bg='#b8b4b0')

def clearWidgets(frame):
    for a in frame.winfo_children():
        a.destroy()
        
def del_book():
    myc.execute("""DELETE FROM Books
                WHERE Name = ''
                OR Publisher = ''
                OR Number = ''
                OR Id = '' 
                OR Type = '' 
                OR Name IS NULL 
                OR Publisher IS NULL
                OR Number IS NULL 
                OR Id IS NULL 
                OR Type IS NULL""")
    mydb.commit()

def del_member():
    myc.execute("""DELETE FROM Member
                WHERE Firstname = '' 
                OR Lastname = ''
                OR Id = '' OR Gender = '' 
                OR Age = '' OR Phone = ''
                OR Firstname IS NULL 
                OR Lastname IS NULL
                OR Id IS NULL 
                OR Gender IS NULL 
                OR Age IS NULL 
                OR Phone IS NULL
                OR SubExpiry = ''
                OR SubExpiry IS NULL""")
    mydb.commit()

def del_info():
    myc.execute("""DELETE FROM Info
                WHERE PersonId IS NULL 
                OR BookId IS NULL 
                OR ReturnTime IS NULL
                OR PersonId = ''
                OR BookId = ''
                OR ReturnTime = ''""")
    mydb.commit()

def frame_6():
    clearWidgets(f1)
    f6.tkraise()

    l1 = tk.Label(f6,text='Please sign in to your account',font=('Franklin Gothic Medium',24),bg='#b8b4b0')
    l2 = tk.Label(f6,text='Id:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    l3 = tk.Label(f6,text='',font=('Franklin Gothic Medium',18),bg='#b8b4b0')

    e1 = tk.Entry(f6,font=('Franklin Gothic Medium',18),bg='#35809c')

    def sign_in():
        memid = e1.get()

        myc.execute("""SELECT Id FROM Member""")
        r = myc.fetchall()
        x = 0
        try:
            for i in r:
                if i == (int(memid),):
                    x += 1
            if x == 1:
                def opt_():
                    clearWidgets(f6)
                    opt.tkraise()
                    myc.execute("""SELECT Firstname FROM Member
                                WHERE Id = ?""",(memid,))
                    r = myc.fetchall()
                    for i in r:
                        namee = f"{i}"
                        opp = namee.removeprefix("('")
                        name = opp.removesuffix("',)").title()
                    l1 = tk.Label(opt,text=f'Welcome {name}',font=('Franklin Gothic Medium',24),bg='#b8b4b0')
                    
                    def borrow():
                        clearWidgets(opt)
                        fborrow.tkraise()

                        l1 = tk.Label(fborrow,text='Book Id:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
                        l2 = tk.Label(fborrow,text='Person Id:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
                        
                        l3 = tk.Label(fborrow,text=f'{memid}',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
                        l4 = tk.Label(fborrow,text='',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
                        l5 = tk.Label(fborrow,text='Return Time:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')

                        e1 = tk.Entry(fborrow,font=('Franklin Gothic Medium',18),bg='#35809c')

                        returnTime = tk.StringVar()
                        re1 = tk.Radiobutton(fborrow, text='2 Weeks',font=('Franklin Gothic Medium',18),bg='#b8b4b0',variable=returnTime,value='2 Weeks')
                        re2 = tk.Radiobutton(fborrow, text='1 Month',font=('Franklin Gothic Medium',18),bg='#b8b4b0',variable=returnTime,value='1 Month')
                        def sub_3():
                            selected_return = returnTime.get()
                            bookid = e1.get()
                            myc.execute("""SELECT Id FROM Books""")
                            r = myc.fetchall()
                            x = 0
                            try:
                                def frame_back3():
                                    clearWidgets(fborrow)
                                    fBack3.tkraise()
                        
                                    l1 = tk.Label(fBack3,text='Choose One Of The Options Below:',font=('Franklin Gothic Medium',26),bg='#b8b4b0')
                                    b1 = tk.Button(fBack3,text='Borrow another book',font=('Franklin Gothic Medium',26),bg='#35809c',command=borrow)
                
                                    b2 = tk.Button(fBack3,text='Back',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_1)
                                    b3 = tk.Button(fBack3,text='Main menu',font=('Franklin Gothic Medium',26),bg='#35809c',command=opt_)
                                    b4 = tk.Button(fBack3,text='Submit new book',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_2)
                                    
                                    l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                                    b1.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                
                                    b2.grid(row=3,column=0,padx=5,pady=5,sticky="NEWS")
                                    b3.grid(row=3,column=1,padx=5,pady=5,sticky="NEWS")
                                    b4.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

                                    for i in range(4):
                                        for j in range(2):
                                            fBack3.grid_rowconfigure(i,weight=1)
                                            fBack3.grid_columnconfigure(j,weight=1)
                                
                                for i in r:
                                    if i == (int(bookid),):
                                        x += 1
                                if x == 1:
                                    myc.execute("""SELECT * FROM Books 
                                                WHERE Id = ?""", (bookid,))
                                    data = myc.fetchone()
                                    
                                    z = 0
                                    myc.execute("""SELECT * FROM Info
                                                WHERE PersonId = ?
                                                AND BookId = ?""", (memid,bookid))
                                    w = myc.fetchone()
                                    if w:
                                        z += 1
                                    if selected_return == "":
                                        l4.config(text='Please choose the return time and try again.')
                                    elif z == 1:
                                        l4.config(text='You have already borrowed this book.')
                                        root.after(3000,frame_back3)
                                    elif data[2] >= 1:
                                        num = data[2] - 1
                                        myc.execute("""UPDATE Books 
                                                    SET number = ? 
                                                    WHERE Id = ?""",
                                                    (num, bookid))
                                        myc.execute("""INSERT INTO Info
                                                (PersonId,BookId) 
                                                VALUES (?, ?)""",(memid, bookid))
                                        time = datetime.now()
                                        if selected_return == '2 Weeks':
                                            two_weeks = (time + timedelta(weeks=2)).date()
                                            myc.execute("""UPDATE Info SET ReturnTime = ?
                                                        WHERE PersonId = ?
                                                        AND BookId = ?""",
                                                        (two_weeks, memid, bookid))
                                        elif selected_return == '1 Month':
                                            one_month = (time + timedelta(days=30)).date()
                                            myc.execute("""UPDATE Info SET ReturnTime = ?
                                                        WHERE PersonId = ?
                                                        AND BookId = ?""",
                                                        (one_month, memid, bookid))
                                        myc.execute("""SELECT * FROM MemberStats
                                                WHERE PersonId = ?""", (memid,))
                                        a = myc.fetchone()
                                        num1 = a[3] + 1
                                        myc.execute("""UPDATE MemberStats 
                                                    SET EntryTimes = ? 
                                                    WHERE PersonId = ?""",
                                                    (num1, memid))
                                        myc.execute("""SELECT Type FROM Books
                                                    WHERE Id = ?""", (bookid,))
                                        c = myc.fetchone()
                                        f = f"{c}"
                                        d = f.removeprefix("('")
                                        e = d.removesuffix("',)")
                                        myc.execute("""SELECT * FROM BookStats
                                                WHERE BookType = ?""", (e,))
                                        b = myc.fetchone()
                                        num2 = b[2] + 1
                                        myc.execute("""UPDATE BookStats 
                                                    SET TimesBorrowed = ? 
                                                    WHERE BookType = ?""",
                                                    (num2, e))
                                        mydb.commit()

                                        l4.config(text=f'The book no.{bookid} has been borrowed by {name}.')
                                        del_info()
                                        root.after(3000,frame_back3)
                                    elif data[2] == 0:
                                        myc.execute("""SELECT ReturnTime FROM Info
                                                    WHERE BookId = ?""", (bookid,))
                                        r = myc.fetchone()
                                        for m in r:
                                            re = f"{m}"
                                            datee = re.removeprefix("('")
                                            date = datee.removesuffix("',)")
                                        l4.config(text=f"The Book no.{bookid} will be available on {date}.")
                                        root.after(3000,frame_back3)
                                elif x == 0:
                                    l4.config(text=f"The Book no.{bookid} doesn't exist,please submit the book!")
                                    root.after(3000,frame_back3)
                            except ValueError:
                                l4.config(text='Please fill all the blanks correctly and try again.')
                        
                        b1 = tk.Button(fborrow,text='Submit',font=('Franklin Gothic Medium',18),bg='#35809c',command=sub_3)
                        b2 = tk.Button(fborrow,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=opt_)

                        l2.grid(row=0,column=0,padx=5,pady=5,sticky="NEWS")
                        l3.grid(row=0,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")
                        
                        l1.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
                        e1.grid(row=1,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")
                        
                        l5.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
                        re1.grid(row=2,column=1,padx=5,pady=5,sticky="NEWS")
                        re2.grid(row=2,column=2,padx=5,pady=5,sticky="NEWS")

                        b1.grid(row=3,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                        b2.grid(row=3,column=2,padx=5,pady=5,sticky="NEWS")
                        l4.grid(row=4,column=0,columnspan=3,padx=5,pady=5,sticky="NEWS")

                        for k in range(5):
                            for a in range(3):
                                fborrow.grid_rowconfigure(k,weight=1)
                                fborrow.grid_columnconfigure(a,weight=1)

                    def _return():
                        clearWidgets(opt)
                        freturn.tkraise()

                        l1 = tk.Label(freturn,text='Book Id:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
                        l2 = tk.Label(freturn,text='Person Id:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
                        
                        l3 = tk.Label(freturn,text=f'{memid}',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
                        l4 = tk.Label(freturn,text='',font=('Franklin Gothic Medium',18),bg='#b8b4b0')

                        e1 = tk.Entry(freturn,font=('Franklin Gothic Medium',18),bg='#35809c')

                        def sub_4():
                            bookid = e1.get()
                            myc.execute("""SELECT * FROM Info
                                        WHERE PersonId = ?
                                        AND BookId = ?""", (memid,bookid))
                            r = myc.fetchone()
                            x = 0
                            try:
                                def frame_back4():
                                    clearWidgets(freturn)
                                    fBack4.tkraise()
                        
                                    l1 = tk.Label(fBack4,text='Choose One Of The Options Below:',font=('Franklin Gothic Medium',26),bg='#b8b4b0')
                                    b1 = tk.Button(fBack4,text='Return another book',font=('Franklin Gothic Medium',26),bg='#35809c',command=_return)
                
                                    b2 = tk.Button(fBack4,text='Back',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_1)
                                    b3 = tk.Button(fBack4,text='Main menu',font=('Franklin Gothic Medium',26),bg='#35809c',command=opt_)

                                    l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                                    b1.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                
                                    b2.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
                                    b3.grid(row=2,column=1,padx=5,pady=5,sticky="NEWS")

                                    for i in range(3):
                                        for j in range(2):
                                            fBack4.grid_rowconfigure(i,weight=1)
                                            fBack4.grid_columnconfigure(j,weight=1)
                                
                                if r:
                                    x += 1
                                if x == 1:
                                    myc.execute("""SELECT * FROM Books 
                                                WHERE Id = ?""", (bookid,))
                                    data = myc.fetchone()
                                    num = data[2] + 1
                                    myc.execute("""UPDATE Books 
                                                SET Number = ? 
                                                WHERE Id = ?""",
                                                (num, bookid))
                                    myc.execute("""DELETE FROM Info
                                                WHERE PersonId = ?
                                                AND BookId = ?"""
                                                ,(memid, bookid))
                                    mydb.commit()
                                    l4.config(text=f'The book no.{bookid} has been returned by {name}.')
                                    root.after(3000,frame_back4)
    
                                elif x == 0:
                                    l4.config(text=f"The person no.{memid} hasn't borrowed this book!")
                            except ValueError:
                                l4.config(text='Please fill all the blanks correctly and try again.')

                        b1 = tk.Button(freturn,text='Submit',font=('Franklin Gothic Medium',18),bg='#35809c',command=sub_4)
                        b2 = tk.Button(freturn,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=opt_)

                        l2.grid(row=0,column=0,padx=5,pady=5,sticky="NEWS")
                        l3.grid(row=0,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")
                        
                        l1.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
                        e1.grid(row=1,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")

                        b1.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                        b2.grid(row=2,column=2,padx=5,pady=5,sticky="NEWS")
                        l4.grid(row=3,column=0,columnspan=3,padx=5,pady=5,sticky="NEWS")

                        for k in range(4):
                            for a in range(3):
                                freturn.grid_rowconfigure(k,weight=1)
                                freturn.grid_columnconfigure(a,weight=1)

                    b1 = tk.Button(opt,text='Borrow',font=('Franklin Gothic Medium',18),bg='#35809c',command=borrow)
                    b2 = tk.Button(opt,text='Return',font=('Franklin Gothic Medium',18),bg='#35809c',command=_return)
                    
                    b3 = tk.Button(opt,text='Previous',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_6)
                    b4 = tk.Button(opt,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_1)

                    l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                    b1.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
                    b2.grid(row=1,column=1,padx=5,pady=5,sticky="NEWS")

                    b3.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                    b4.grid(row=3,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

                    for m in range(4):
                        for j in range(2):
                            opt.grid_rowconfigure(m,weight=1)
                            opt.grid_columnconfigure(j,weight=1)
                opt_()
            elif x == 0:
                l3.config(text="The Id doesn't exist,please sign up!")
        except ValueError:
            del_member()
            l3.config(text='Please fill all the blanks correctly and try again.')
    
    def find():
        clearWidgets(f6)
        ffind.tkraise()
        
        l1 = tk.Label(ffind,text='Find Id by Lastname',font=('Franklin Gothic Medium',26),bg='#b8b4b0')
        l2 = tk.Label(ffind,text='Last Name:',font=('Franklin Gothic Medium',22),bg='#b8b4b0')
        l3 = tk.Label(ffind,text='',font=('Franklin Gothic Medium',24),bg='#b8b4b0')
        
        e1 = tk.Entry(ffind,font=('Franklin Gothic Medium',18),bg='#35809c')

        def _find():
            lname = e1.get()
            myc.execute("""SELECT Id FROM Member
                        WHERE LastName = ?"""
                        ,(lname,))
            r = myc.fetchone()
            if lname == '':
                l3.config(text="Please fill the blank correctly and try again.")
            else:
                x = 0
                if r:
                    x += 1
                if x == 1:
                    a = f"{r}"
                    b = a.removeprefix("(")
                    Id = b.removesuffix(",)")
                    l3.config(text=f'Your Id is {Id}')
                elif x == 0:
                    l3.config(text=f"The last name '{lname}' doesn't exist!")

        b1 = tk.Button(ffind,text='Find',font=('Franklin Gothic Medium',18),bg='#35809c',command=_find)
        b2 = tk.Button(ffind,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_6)

        l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
        l2.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
        e1.grid(row=1,column=1,padx=5,pady=5,sticky="NEWS")

        b1.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
        b2.grid(row=2,column=1,padx=5,pady=5,sticky="NEWS")
        l3.grid(row=3,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

        for i in range(4):
            for j in range(2):
                ffind.grid_rowconfigure(i,weight=1)
                ffind.grid_columnconfigure(j,weight=1)
    
    b2 = tk.Button(f6,text='Sign In',font=('Franklin Gothic Medium',18),bg='#35809c',command=sign_in)
    b1 = tk.Button(f6,text='Sign Up',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_5)
    b3 = tk.Button(f6,text='Find Id',font=('Franklin Gothic Medium',18),bg='#35809c',command=find)
    b4 = tk.Button(f6,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_1)

    l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
    l2.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
    e1.grid(row=1,column=1,padx=5,pady=5,sticky="NEWS")

    b1.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
    b2.grid(row=2,column=1,padx=5,pady=5,sticky="NEWS")
    b3.grid(row=3,column=0,padx=5,pady=5,sticky="NEWS")

    b4.grid(row=3,column=1,padx=5,pady=5,sticky="NEWS")
    l3.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

    for i in range(5):
        for j in range(2):
            f6.grid_rowconfigure(i,weight=1)
            f6.grid_columnconfigure(j,weight=1)
            
def extension():
    clearWidgets(f4)
    fExtend.tkraise()

    l1 = tk.Label(fExtend,text='Id:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    l2 = tk.Label(fExtend,text='Subscription Extension:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    l3 = tk.Label(fExtend,text='',font=('Franklin Gothic Medium',18),bg='#b8b4b0')

    e1 = tk.Entry(fExtend,font=('Franklin Gothic Medium',18),bg='#35809c')

    subscription = tk.StringVar()
    sub1 = tk.Radiobutton(fExtend,text='3 Months',font=('Franklin Gothic Medium',18),bg='#b8b4b0',variable=subscription,value='3 Months')
    sub2 = tk.Radiobutton(fExtend,text='6 Months',font=('Franklin Gothic Medium',18),bg='#b8b4b0',variable=subscription,value='6 Months')

    def sub_2():
        memid = e1.get()
        selected_sub = subscription.get()

        myc.execute("""SELECT Id FROM Member""")
        r = myc.fetchall()
        x = 0
        try:
            def frame_back2():
                clearWidgets(fExtend)
                fBack2.tkraise()
                        
                l1 = tk.Label(fBack2,text='Choose One Of The Options Below:',font=('Franklin Gothic Medium',26),bg='#b8b4b0')
                b1 = tk.Button(fBack2,text='Submit another extension',font=('Franklin Gothic Medium',26),bg='#35809c',command=extension)
                
                b2 = tk.Button(fBack2,text='Back',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_1)
                b3 = tk.Button(fBack2,text='Previous',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_4)
                b4 = tk.Button(fBack2,text='Sign Up',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_5)

                l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                b1.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
                b4.grid(row=1,column=1,padx=5,pady=5,sticky="NEWS")
                
                b2.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
                b3.grid(row=2,column=1,padx=5,pady=5,sticky="NEWS")

                for i in range(3):
                    for j in range(2):
                        fBack2.grid_rowconfigure(i,weight=1)
                        fBack2.grid_columnconfigure(j,weight=1)
            for i in r:
                if i == (int(memid),):
                    x += 1
            if x == 1:
                if selected_sub == '':
                    l3.config(text='Please choose one of the extensions.')
                else:
                    myc.execute("""SELECT SubExpiry FROM Member 
                                WHERE Id = ?""",(memid,))
                    time = myc.fetchone()
                    for i in time:
                        if selected_sub == '3 Months':                   
                            three_months = datetime.strptime(i,"%Y-%m-%d %H:%M:%S.%f") + timedelta(weeks=13)
                            myc.execute("""UPDATE Member SET SubExpiry = ?
                                        WHERE Id = ?""",
                                        (three_months, memid))
                        elif selected_sub == '6 Months':
                            six_months = datetime.strptime(i,"%Y-%m-%d %H:%M:%S.%f") + timedelta(weeks=26)
                            myc.execute("""UPDATE Member SET SubExpiry = ?
                                        WHERE Id = ?""",
                                        (six_months, memid))
                    mydb.commit()
                    l3.config(text='The subscription has been successfully extended.')
                    root.after(3000,frame_back2)
                        
            elif x == 0:
                l3.config(text="The Id doesn't exist, please sign up!")
                root.after(3000,frame_back2)
        except ValueError:
            del_member()
            l3.config(text='Please fill all the blanks correctly and try again.')

    b1 = tk.Button(fExtend,text='Submit',font=('Franklin Gothic Medium',18),bg='#35809c',command=sub_2)
    b2 = tk.Button(fExtend,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_4)

    l1.grid(row=0,column=0,padx=5,pady=5,sticky="NEWS")
    e1.grid(row=0,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")
    l2.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")

    sub1.grid(row=1,column=1,padx=5,pady=5,sticky="NEWS")
    sub2.grid(row=1,column=2,padx=5,pady=5,sticky="NEWS")
    b1.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

    b2.grid(row=2,column=2,padx=5,pady=5,sticky="NEWS")
    l3.grid(row=3,column=0,columnspan=3,padx=5,pady=5,sticky="NEWS")
    for i in range(4):
        for j in range(3):
            fExtend.grid_rowconfigure(i,weight=1)
            fExtend.grid_columnconfigure(j,weight=1)
            
def frame_5():
    clearWidgets(f4)
    f5.tkraise()

    l1 = tk.Label(f5,text='First Name:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    l2 = tk.Label(f5,text='Last Name:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    l3 = tk.Label(f5,text='Id:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    
    l4 = tk.Label(f5,text='Age:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    l5 = tk.Label(f5,text='Gender:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    
    l6 = tk.Label(f5,text='Phone Number:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    l7 = tk.Label(f5,text='Subscription Type:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    l8 = tk.Label(f5,text='',font=('Franklin Gothic Medium',18),bg='#b8b4b0')

    e1 = tk.Entry(f5,font=('Franklin Gothic Medium',18),bg='#35809c')
    e2 = tk.Entry(f5,font=('Franklin Gothic Medium',18),bg='#35809c')
    e3 = tk.Entry(f5,font=('Franklin Gothic Medium',18),bg='#35809c')
    
    e4 = tk.Entry(f5,font=('Franklin Gothic Medium',18),bg='#35809c')
    e5 = tk.Entry(f5,font=('Franklin Gothic Medium',18),bg='#35809c')

    def sub_1():
        fname = e1.get().lower()
        lname = e2.get().lower()
        memid = e3.get()
        selected_gender = gender.get()
        selected_sub = subscription.get()
        age = e4.get()
        phone = e5.get()
        myc.execute("""SELECT Id FROM Member""")
        r = myc.fetchall()
        myc.execute("""SELECT Lastname FROM Member""")
        m = myc.fetchall()
        x = 0
        z = 0
        try:
            def frame_back1():
                clearWidgets(f5)
                fBack1.tkraise()
                        
                l1 = tk.Label(fBack1,text='Choose One Of The Options Below:',font=('Franklin Gothic Medium',26),bg='#b8b4b0')
                b1 = tk.Button(fBack1,text='Submit another member',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_4)
                b2 = tk.Button(fBack1,text='Back',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_1)

                l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                b1.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                b2.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

                for i in range(3):
                    for j in range(1):
                        fBack1.grid_rowconfigure(i,weight=1)
                        fBack1.grid_columnconfigure(j,weight=1)
            for i in r:
                if i == (int(memid),):
                    x += 1
            for j in m:
                if j ==(lname,):
                    z += 1
            if x == 0 and z == 0:
                q = 0
                if fname == '' or lname == '' or memid == '' or selected_gender == '' or selected_sub == '' or age == '' or phone == '':
                    q = 1
                if q == 1:
                    l8.config(text='Please fill all the blanks correctly and try again.')
                elif q == 0:
                    time = datetime.now()
                    one_month = (time + timedelta(days=30)).date()
                    myc.execute("""INSERT INTO MemberStats
                                (PersonId, Age, DeadLine, EntryTimes)
                                VALUES (?, ?, ?, 0)""",
                                (memid, age, one_month))
                    myc.execute("""INSERT INTO Member 
                                (Firstname, Lastname, Id,
                                Gender, Age, Phone)
                                VALUES (?, ?, ?, ?, ?, ?)""", 
                                (fname, lname, memid, selected_gender, age, phone))
                    if selected_sub == '3 Months':
                        three_months = time + timedelta(weeks=13)
                        myc.execute("""UPDATE Member SET SubExpiry = ?
                                    WHERE Id = ?""",
                                    (three_months, memid))
                    elif selected_sub == '6 Months':
                        six_months = time + timedelta(weeks=26)
                        myc.execute("""UPDATE Member SET SubExpiry = ?
                                    WHERE Id = ?""",
                                    (six_months, memid))
                    mydb.commit()
                    l8.config(text='The informations has been successfully submitted.')
                    root.after(3000,frame_back1)
                        
            elif x >= 1 and z == 0:
                l8.config(text='The Id already exists, try another one!')
            elif z >= 1 and x == 0:
                l8.config(text='The Lastname already exists, try another one!')
            elif z >=1 and x >= 1:
                l8.config(text='The Lastname and the Id already exist, try another ones!')
        except ValueError:
            del_member()
            l8.config(text='Please fill all the blanks correctly and try again.')

    b1 = tk.Button(f5,text='Submit',font=('Franklin Gothic Medium',18),bg='#35809c',command=sub_1)
    b2 = tk.Button(f5,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_4)
    
    l1.grid(row=0,column=0,padx=5,pady=5,sticky="NEWS")
    e1.grid(row=0,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")
    l2.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")

    e2.grid(row=1,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")
    l3.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
    e3.grid(row=2,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")

    l4.grid(row=3,column=0,padx=5,pady=5,sticky="NEWS")
    e4.grid(row=3,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")
    l5.grid(row=4,column=0,padx=5,pady=5,sticky="NEWS")
   
    gender = tk.StringVar()
    male = tk.Radiobutton(f5, text='Male',font=('Franklin Gothic Medium',18),bg='#b8b4b0',variable=gender,value='Male')
    female = tk.Radiobutton(f5, text='Female',font=('Franklin Gothic Medium',18),bg='#b8b4b0',variable=gender,value='Female')
    
    subscription = tk.StringVar()
    sub1 = tk.Radiobutton(f5, text='3 Months',font=('Franklin Gothic Medium',18),bg='#b8b4b0',variable=subscription,value='3 Months')
    sub2 = tk.Radiobutton(f5, text='6 Months',font=('Franklin Gothic Medium',18),bg='#b8b4b0',variable=subscription,value='6 Months')
    
    male.grid(row=4,column=1,padx=5,pady=5,sticky="NEWS")
    female.grid(row=4,column=2,padx=5,pady=5,sticky="NEWS")
    
    l6.grid(row=5,column=0,padx=5,pady=5,sticky="NEWS")
    e5.grid(row=5,column=1,columnspan=2,padx=5,pady=5,sticky="NEWS")
    
    l7.grid(row=6,column=0,padx=5,pady=5,sticky="NEWS")
    sub1.grid(row=6,column=1,padx=5,pady=5,sticky="NEWS")
    sub2.grid(row=6,column=2,padx=5,pady=5,sticky="NEWS")

    b1.grid(row=7,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
    b2.grid(row=7,column=2,columnspan=2,padx=5,pady=5,sticky="NEWS")
    
    l8.grid(row=8,column=0,columnspan=3,padx=5,pady=5,sticky="NEWS")

    for i in range(9):
        for j in range(3):
            f5.grid_rowconfigure(i,weight=1)
            f5.grid_columnconfigure(j,weight=1)

def frame_4():
    del_member()
    clearWidgets(f2)
    clearWidgets(f5)
    f4.tkraise()
        
    l1 = tk.Label(f4,text='Choose One Of The Options Below:',font=('Franklin Gothic Medium',26),bg='#b8b4b0')
    b1 = tk.Button(f4,text='Sign up',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_5)    
    
    b2 = tk.Button(f4,text='Subscription Extension',font=('Franklin Gothic Medium',18),bg='#35809c',command=extension)
    b3 = tk.Button(f4,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_1)

    l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
    b1.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
    
    b2.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
    b3.grid(row=3,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

    for i in range(4):
        for j in range(1):
            f4.grid_rowconfigure(i,weight=1)
            f4.grid_columnconfigure(j,weight=1)

def frame_2():
    del_book()
    clearWidgets(f1)
    clearWidgets(f3)
    f2.tkraise()
        
    l1 = tk.Label(f2,text='Book Name:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    e1 = tk.Entry(f2,font=('Franklin Gothic Medium',18),bg='#35809c')

    l2 = tk.Label(f2,text='Publisher:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    e2 = tk.Entry(f2,font=('Franklin Gothic Medium',18),bg='#35809c')
    
    l3 = tk.Label(f2,text="",font=('Franklin Gothic Medium',18),bg='#b8b4b0')

    def book_check():
        name = e1.get().lower()
        pub = e2.get().lower()
        myc.execute("""SELECT * FROM Books 
                    WHERE Name = ? 
                    AND Publisher = ?""", (name, pub))
        data = myc.fetchone()
        if data:
            num = data[2] + 1
            myc.execute("""UPDATE Books 
                        SET Number = ? 
                        WHERE Name = ? 
                        AND Publisher = ?""",
                        (num, name, pub))
            mydb.commit()
            l3.config(text=f"The number has been updated to {num} for {name} written by {pub}.")
        else:
            try:
                if name == "" or pub == "":
                    raise RuntimeError
                else:
                    myc.execute("""INSERT INTO Books 
                                (Name, Publisher)
                                VALUES (?, ?)""", (name, pub))
                    mydb.commit()
                    clearWidgets(f2)
                    f3.tkraise()
            except RuntimeError:
                l3.config(text='Please fill all the blanks correctly and try again.')
            l11 = tk.Label(f3,text='Number Of The Book:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
            e11 = tk.Entry(f3,font=('Franklin Gothic Medium',18),bg='#35809c')
            
            l21 = tk.Label(f3,text='Book ID:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
            e21 = tk.Entry(f3,font=('Franklin Gothic Medium',18),bg='#35809c')

            l31 = tk.Label(f3,text='Book Subject:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
            e31 = tk.Entry(f3,font=('Franklin Gothic Medium',18),bg='#35809c')
            l41 = tk.Label(f3,text="",font=('Franklin Gothic Medium',18),bg='#b8b4b0')
            def book_update():
                num1 = e11.get()
                bookid = e21.get()
                sub = e31.get().lower()

                myc.execute("""SELECT Id FROM Books""")
                r = myc.fetchall()
                x = 0
                try:
                    def frame_back():
                        clearWidgets(f3)
                        clearWidgets(f2)
                        fBack.tkraise()
                            
                    l1 = tk.Label(fBack,text='Choose One Of The Options Below:',font=('Franklin Gothic Medium',26),bg='#b8b4b0')
                    b1 = tk.Button(fBack,text='Submit another book',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_2)
                    b2 = tk.Button(fBack,text='Back',font=('Franklin Gothic Medium',26),bg='#35809c',command=frame_1)

                    l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                    b1.grid(row=1,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
                    b2.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

                    for i in range(3):
                        for j in range(1):
                            fBack.grid_rowconfigure(i,weight=1)
                            fBack.grid_columnconfigure(j,weight=1)

                    for i in r:
                        if i == (int(bookid),):
                            x += 1
                    if x == 0 and int(num1) >= 1:
                        time = datetime.now()
                        one_month = (time + timedelta(days=30)).date()
                        myc.execute("""SELECT * FROM BookStats
                                    WHERE BookType = ?""",
                                    (sub,))
                        a = myc.fetchall()
                        if len(a) == 0:
                            myc.execute("""INSERT INTO BookStats
                                    (BookType, DeadLine, TimesBorrowed)
                                    VALUES (?, ?, 0)""",
                                    (sub, one_month))
                        myc.execute("""UPDATE Books 
                                    SET Number = ?, 
                                    Id = ?, Type = ?
                                    WHERE Name = ? 
                                    AND Publisher = ?""", 
                                    (num1, bookid, sub, name, pub))
                        mydb.commit()
                        l41.config(text='The informations has been successfully submitted.')
                        root.after(3000,frame_back)
                    elif int(num1) <= 0:
                        l41.config(text='Number of the book must be at least 1 !')
                    elif x >= 1:
                        l41.config(text='The Id already exists, try another one!')
                except ValueError:
                    l41.config(text='Please fill all the blanks correctly and try again.')                  

            b11 = tk.Button(f3,text='Submit',font=('Franklin Gothic Medium',18),bg='#35809c',command=book_update)
            b21 = tk.Button(f3,text='Previous',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_2)
            b31 = tk.Button(f3,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_1)

            l11.grid(row=0,column=0,padx=5,pady=5,sticky="NEWS")
            e11.grid(row=0,column=1,padx=5,pady=5,sticky="NEWS")

            l21.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
            e21.grid(row=1,column=1,padx=5,pady=5,sticky="NEWS")

            l31.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
            e31.grid(row=2,column=1,padx=5,pady=5,sticky="NEWS")

            b11.grid(row=3,column=0,padx=5,pady=5,sticky="NEWS")
            b21.grid(row=3,column=1,padx=5,pady=5,sticky="NEWS")
                
            b31.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
            l41.grid(row=5,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

            for i in range(5):
                for j in range(2):
                    f3.grid_rowconfigure(i,weight=1)
                    f3.grid_columnconfigure(j,weight=1)

    b1 = tk.Button(f2,text='Submit',font=('Franklin Gothic Medium',18),bg='#35809c',command=book_check)
    b2 = tk.Button(f2,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_1)    

    l1.grid(row=0,column=0,padx=5,pady=5,sticky="NEWS")
    e1.grid(row=0,column=1,padx=5,pady=5,sticky="NEWS")

    l2.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
    e2.grid(row=1,column=1,padx=5,pady=5,sticky="NEWS")

    b1.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
    b2.grid(row=2,column=1,padx=5,pady=5,sticky="NEWS")

    l3.grid(row=3,column=0,rowspan=4,columnspan=3,padx=5,pady=5,sticky="NEWS")

    for i in range(4):
        for j in range(2):
            f2.grid_rowconfigure(i,weight=1)
            f2.grid_columnconfigure(j,weight=1)
            
def frame_exit():
    clearWidgets(f1)
    fexit.tkraise()

    l1 = tk.Label(fexit,text='Are you sure that you want to exit?',font=('Franklin Gothic Medium',26),bg='#b8b4b0')
    
    def exit_tk():
        del_book()
        del_info()
        del_member()
        root.destroy()




    b1 = tk.Button(fexit,text='Yes',font=('Franklin Gothic Medium',22),bg='#35809c',command=exit_tk)
    b2 = tk.Button(fexit,text='No',font=('Franklin Gothic Medium',22),bg='#35809c',command=frame_1)    

    l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
    b1.grid(row=2,column=0,padx=5,pady=5,sticky="NEWS")
    b2.grid(row=2,column=1,padx=5,pady=5,sticky="NEWS")

    for i in range(3):
        for j in range(2):
            fexit.grid_rowconfigure(i,weight=1)
            fexit.grid_columnconfigure(j,weight=1)

def frame_info():
    time = datetime.now().strftime('%Y-%m')
    clearWidgets(f1)
    finfo.tkraise()

    l1 = tk.Label(finfo,text=f'Statistics for {time}',font=('Franklin Gothic Medium',24),bg='#b8b4b0')
    l2 = tk.Label(finfo,text='',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
    def book_stat():
        myc.execute("""SELECT BookType
                    FROM BookStats 
                    WHERE TimesBorrowed >= 3""")
        r = myc.fetchmany(3)
        if r == []:
            l2.config(text='None of the current book types are popular.')
        else:
            statlist = []
            for i in r:
                a = f'{i}'
                b = a.removeprefix("('")
                c = b.removesuffix("',)")
                statlist.append(c)
            a1 = f'{statlist}'
            b1 = a1.removeprefix("[")
            c1 = b1.removesuffix("]")
            l2.config(text=f'The most popular book(s) are {c1}')
    def member_stat():
        myc.execute("""SELECT PersonId
                    FROM MemberStats 
                    WHERE EntryTimes < 2""")
        r = myc.fetchmany(3)
        if r == []:
            l2.config(text='Everyone is coming to the library at least twice.')
        else:
            statlist = []
            for i in r:
                a = f'{i}'
                b = a.removeprefix("(")
                c = b.removesuffix(",)")
                statlist.append(c)
            a1 = f'{statlist}'
            b1 = a1.removeprefix("[")
            c1 = b1.removesuffix("]")
            l2.config(text=f'The Id(s) that entered the library less than twice are {c1}')
    b1 = tk.Button(finfo,text='Books stat',font=('Franklin Gothic Medium',18),bg='#35809c',command=book_stat)
    b2 = tk.Button(finfo,text='Members stat',font=('Franklin Gothic Medium',18),bg='#35809c',command=member_stat)
    b3 = tk.Button(finfo,text='Back',font=('Franklin Gothic Medium',18),bg='#35809c',command=frame_1)

    l1.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
    b1.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
    
    b2.grid(row=1,column=1,padx=5,pady=5,sticky="NEWS")
    b3.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")
    l2.grid(row=3,column=0,columnspan=2,padx=5,pady=5,sticky="NEWS")

    for i in range(4):
        for j in range(2):
            finfo.grid_rowconfigure(i,weight=1)
            finfo.grid_columnconfigure(j,weight=1)
            
def frame_1():
    del_book()
    clearWidgets(f2)
    clearWidgets(f3)
    clearWidgets(f4)
    clearWidgets(f5)
    clearWidgets(f6)
    
    clearWidgets(fBack)
    clearWidgets(fBack1)
    clearWidgets(fBack2)
    clearWidgets(fBack3)
    clearWidgets(fBack4)
    
    clearWidgets(fexit)
    clearWidgets(fExtend)
    clearWidgets(finfo)
    f1.tkraise()
        
    def up_time():
        l1 = tk.Label(f1,text='Welcome to my Library :)',font=('Forte',24),bg='#b8b4b0')
        l2 = tk.Label(f1,text='Choose one of the options below:',font=('Franklin Gothic Medium',18),bg='#b8b4b0')
        time_label = tk.Label(f1,text="",font=('Forte',18),bg='#b8b4b0')
        l1.grid(row=0,column=0,padx=5,pady=5,sticky="NEWS")
        time_label.grid(row=0,column=1,rowspan=2,padx=5,pady=5,sticky="NEWS")
        l2.grid(row=1,column=0,padx=5,pady=5,sticky="NEWS")
        time = datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')
        time_label.config(text=time)
        f1.after(1000, up_time)
    
    
    up_time()
        
    b1 = tk.Button(f1,text='Books',font=('Franklin Gothic Medium',16),bg='#35809c',command=frame_2)
    b2 = tk.Button(f1,text='Membership',font=('Franklin Gothic Medium',16),bg='#35809c',command=frame_4)
    b3 = tk.Button(f1,text='Accounts',font=('Franklin Gothic Medium',16),bg='#35809c', command=frame_6)

    b4 = tk.Button(f1,text='Statistics',font=('Franklin Gothic Medium',16),bg='#35809c',command=frame_info)
    b5 = tk.Button(f1,text='Exit',font=('Franklin Gothic MediumV',16),bg='#35809c',command=frame_exit)
        
    
        
    b1.grid(row=4,column=1,rowspan=2,padx=5,pady=5,sticky="NEWS")
    b2.grid(row=2,column=0,rowspan=2,padx=5,pady=5,sticky="NEWS")
    b3.grid(row=2,column=1,rowspan=2,padx=5,pady=5,sticky="NEWS")
        
    b4.grid(row=4,column=0,rowspan=2,padx=5,pady=5,sticky="NEWS")
    b5.grid(row=6,column=0,columnspan=2,rowspan=2,padx=5,pady=5,sticky="NEWS")

        
    for i in range(8):
        for j in range(2):
            f1.grid_rowconfigure(i,weight=1)
            f1.grid_columnconfigure(j,weight=1)

frame_1()

f1.grid(row=0,column=0,sticky="NEWS")
f2.grid(row=0,column=0,sticky="NEWS")
f3.grid(row=0,column=0,sticky="NEWS")
f4.grid(row=0,column=0,sticky="NEWS")
f5.grid(row=0,column=0,sticky="NEWS")
f6.grid(row=0,column=0,sticky="NEWS")

fBack.grid(row=0,column=0,sticky="NEWS")
fBack1.grid(row=0,column=0,sticky="NEWS")
fBack2.grid(row=0,column=0,sticky="NEWS")
fBack3.grid(row=0,column=0,sticky="NEWS")
fBack4.grid(row=0,column=0,sticky="NEWS")

opt.grid(row=0,column=0,sticky="NEWS")
fExtend.grid(row=0,column=0,sticky="NEWS")
fborrow.grid(row=0,column=0,sticky="NEWS")
freturn.grid(row=0,column=0,sticky="NEWS")

ffind.grid(row=0,column=0,sticky="NEWS")
fexit.grid(row=0,column=0,sticky="NEWS")
finfo.grid(row=0,column=0,sticky="NEWS")

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

atexit.register(del_book)
atexit.register(del_member)
atexit.register(del_info)

def del_sub():
    time = datetime.now()
    myc.execute("""DELETE FROM Member
                WHERE SubExpiry <= ?""",
                (time,))
    mydb.commit()

def res_stats():
    time = datetime.now()
    one_month = (time + timedelta(days=30)).date()
    myc.execute("""UPDATE MemberStats
                SET EntryTimes = 0
                WHERE DeadLine <= ?""",
                (time,))
    myc.execute("""UPDATE MemberStats
                SET DeadLine = ?
                WHERE DeadLine <= ?""",
                (one_month, time))
    
    myc.execute("""UPDATE BookStats
                SET TimesBorrowed = 0
                WHERE DeadLine <= ?""",
                (time,))
    myc.execute("""UPDATE BookStats
                SET DeadLine = ?
                WHERE DeadLine <= ?""",
                (one_month, time))
    mydb.commit()

root.after(1000,del_sub)
root.after(1000,res_stats)

root.mainloop()