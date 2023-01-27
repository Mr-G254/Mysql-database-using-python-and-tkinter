from tkinter import*
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import webbrowser
import pyperclip as pc
import mysql.connector

Win=Tk()
Win.title("Desktop-Database")
Win.geometry("500x450+100+100")
Win.resizable(False,False)
7
img0=ImageTk.PhotoImage(Image.open("icons/data.png"))
Win.iconphoto(False,img0)

def pos(event,x):
    if x==username and passname.get()=="":
        passname.configure(show="")
        passname.insert(0,"Password")
        see.configure(image=img5)
    elif x==passname and username.get()=="":
        username.insert(0,"Username")

    if x.get()=="Username": 
        x.delete(0,END)
        try:
            error1.destroy()
            errorsep1.destroy()
        except:
            pass

    elif x.get()=="Password":
        x.delete(0,END)
        try:
            error2.destroy()
            errorsep2.destroy()
        except:
            pass
        
        x.configure(show="*")

def check(event):
    if username.get()=="Username" or username.get()=="" or passname.get()=="Password" or passname.get()=="":
        loginbtn.configure(state="disable")
    else:
        loginbtn.configure(state="normal")

def show(x,y):
    if x.get()=="Password":
        pass
    else:
        global value
        if value=="hidden":
            value="visible"
            y.configure(image=img4)
            x.config(show="")
        elif value=="visible":
            value="hidden"
            y.configure(image=img5)
            x.config(show="*")

def login():
    value="hidden"

    global name
    name=username.get()

    global passwd
    passwd=passname.get()

    global hst
    hst="'"+name+"'@'localhost'"

    try:
        dst()
    except:
        pass

    if username.get()=="Username" or username.get()=="" or passname.get()=="Password" or passname.get()=="":
        if username.get()=="Username" or username.get()=="":
            global error1
            error1=Label(startupframe,text="Please fill in the Username field                                          ",bg="#900C3F",bd=0,font=("Times 10"),image=img6,compound=RIGHT)
            error1.place(x=80,y=245)

            global errorsep1
            errorsep1=ttk.Separator(startupframe,orient="horizontal")
            errorsep1.place(x=80,y=263,width=170)

        if passname.get()=="Password" or passname.get()=="":
            global error2
            error2=Label(startupframe,text="Please fill in the Password field                                          ",bg="#900C3F",bd=0,font=("Times 10"),image=img6,compound=RIGHT)
            error2.place(x=80,y=335)

            global errorsep2
            errorsep2=ttk.Separator(startupframe,orient="horizontal")
            errorsep2.place(x=80,y=353,width=170)

    else:
    
        try:
            Win.update()
            loginbtn.configure(state="disable")

            global mydb
            mydb = mysql.connector.connect(
            host="localhost",
            user=username.get(),
            password=passname.get()
            )

            global db
            db=mydb.cursor()

            dbpy()

            startupframe.destroy()

            global Win_Frame
            Win_Frame=Frame(Win,height=500,width=700,bg="#900C3F")
            Win_Frame.place(x=0,y=0)

            global mainframe
            mainframe=Frame(Win_Frame,height=500,width=665,bg="#900C3F")
            mainframe.place(x=35,y=0)
            mainframe.bind("<Button-1>",touch)

            Win.geometry("700x500+100+100")

########################################             MENU                 #############################################################################################
            global sideframe
            sideframe=Frame(Win_Frame,height=500,width=35,bg="#900C3F")
            sideframe.place(x=0,y=0)

            global menubtn
            menubtn=Button(sideframe,bg="#900C3F",activebackground="#900C3F",image=img7,bd=0,command=expand)
            menubtn.place(x=0,y=0,width=35,height=35)

            userlabel=Label(sideframe,bg="#7E0534",image=img9)
            userlabel.place(x=51,y=30)

            global user
            user=Label(sideframe,bg="#900C3F",text=name,font=("Times 20"),fg="white")
            user.place(x=5,y=165,width=230)

            global homebtn
            homebtn=Button(sideframe,bg="#3077AF",activebackground="#3077AF",bd=0,text="Home",padx=20,font=("Times 13"),anchor=W,image=img10,compound="left",command=home)
            homebtn.place(x=35,y=255,width=180,height=25)
        
            global addevbtn
            addevbtn=Button(sideframe,bg="#900C3F",activebackground="#900C3F",bd=0,text="Add a device",padx=20,font=("Times 13"),anchor=W,image=img21,compound="left",command=adddevice)
            addevbtn.place(x=35,y=290,width=180,height=25)

            global settingsbtn
            settingsbtn=Button(sideframe,bg="#900C3F",activebackground="#900C3F",bd=0,text="Settings",padx=20,font=("Times 13"),anchor=W,image=img11,compound="left",command=settings)
            settingsbtn.place(x=35,y=325,width=180,height=25)

            exitbtn=Button(sideframe,bg="#900C3F",activebackground="#900C3F",bd=0,text="Exit",padx=20,font=("Times 13"),anchor=W,image=img12,compound="left",command=lambda :ext(Win))
            exitbtn.place(x=35,y=360,width=180,height=25)

########################################################################################################################################################################

########################################                HOME                 ###########################################################################################

            devicepic=Label(mainframe,bg="#900C3F",image=img32,compound="right")
            devicepic.place(x=40,y=-30)

            devicelabel=Label(mainframe,bg="#900C3F",font=("Times 16"),text="Devices")
            devicelabel.place(x=140,y=200)

            devicesep=ttk.Separator(mainframe,orient="horizontal")
            devicesep.place(x=40,y=230,width=260)

            # refresh=Button(mainframe,bg="#7E0534",image=img34,bd=0,command=lambda:showdatabases(2))
            # refresh.place(x=305,y=203,width=30,height=30)

            global dbwin
            dbwin=Frame(mainframe,width=330,height=250,bg="#900C3F")
            dbwin.place(x=40,y=245)
            dbwin.bind("<Button-1>",touch)

            showdatabases(1)

        except:
            inv=Label(startupframe,bg="#900C3F",text="Invalid Username or Password",font=("Times 13"))
            inv.place(x=40,y=410,width=400)

            loginbtn.configure(state="normal")

def expand():
    global dimension
    if dimension=="small":
        dimension="big"
        sideframe.configure(width=235,bg="#7E0534")
        menubtn.configure(bg="#7E0534",activebackground="#7E0534",image=img8)
        user.configure(bg="#7E0534")

    elif dimension=="big":
        dimension="small"
        sideframe.configure(width=35,bg="#900C3F")
        menubtn.configure(bg="#900C3F",activebackground="#900C3F",image=img7)
        user.configure(bg="#900C3F")

def dst():
    error1.destroy()
    error2.destroy()
    errorsep1.destroy()
    errorsep2.destroy()

def ext(x):
    # if x=="Win":
    #     db.close()

    x.destroy()


def git():
    try:
        webbrowser.open("https://github.com/Mr-G254")
    except Exception as e:
        messagebox.showerror("Error",e)

def mail():
    global maillabel
    try:
        ext(maillabel)
    except:
        pass
    
    pc.copy("Gikuhiezekiel@gmail.com")

    maillabel=Label(settingsframe,bg="#900C3F",text="The email has been copied to clipboard",font=("Times 13"))
    maillabel.place(x=0,y=470,width=276)

def touch(event):
    global dimension
    if dimension=="big":
        dimension="small"
        sideframe.configure(width=35,bg="#900C3F")
        menubtn.configure(image=img7,bg="#900C3F")
        user.configure(bg="#900C3F")
    
    try:
        ext(maillabel)
    except:
        pass

def chgcolor(x):
    x.configure(bg="#3077AF",activebackground="#3077AF")

    if x != homebtn:
        homebtn.configure(bg="#900C3F",activebackground="#900C3F")
    
    if x != settingsbtn:
        settingsbtn.configure(bg="#900C3F",activebackground="#900C3F")

    if x != addevbtn:
        addevbtn.configure(bg="#900C3F",activebackground="#900C3F")

def home():
    chgcolor(homebtn)
    touch(Event)

    try:
        ext(settingsframe)
    except:
        pass

    try:
        ext(deviceframe)
    except:
        pass

    try:
        ext(plus)
    except:
        pass

    try:
        ext(minus)
    except:
        pass

def showdatabases(x):
    if x==1:
        pass
    else:
        dbpy()

    global p
    p=0

    global dbframe
    try:
        ext(dbframe)
    except:
        pass

    global ht
    ht=int(len(database))*40

    dbframe=Frame(dbwin,width=330,height=ht,bg="#900C3F")
    dbframe.place(x=0,y=0)

    if ht > 250:
        dbframe.bind('<MouseWheel>',lambda event:scroll(event,dbframe,250,ht))
    Y=0

    if len(database) > 0:
        for i in database:
            m=str(i).split("_")
            no=len(m)
            if no > 2:
                txt0=m[0]
                for r in range(no):
                    if r==0:
                        continue
                    elif r==no-1:
                        break

                    txt0=txt0+"_"+m[r]
            else:
                txt0=m[0]

            # nm="Button"+str(i)
            nm=Button(dbframe,text=str(txt0).capitalize(),bg="#7E0534",font=("Times 13"),anchor=W,padx=20,bd=0,image=img33,compound="left",command= lambda i=i:opendb(i))
            nm.place(x=0,y=Y,width=260,height=30)

            Y=Y+40
        
    else:
        dbframe.configure(height=100)
        nodev=Label(dbframe,text="No devices were found",bg="#900C3F",fg="white",font=("Times 14"),wraplength=300)
        nodev.place(x=0,y=50,width=260)

def dbpy():
    db.execute("SHOW DATABASES")

    global database
    database=[]
    for i in db:
        if i==('sys',) or i==('information_schema',) or i==('mysql',) or i==('performance_schema',):
            continue
        x=str(i).split("'")
        y=str(x).split("_")
        if len(y) > 1:
            database.append(x[1])

def opendb(x):
    global dbwindow
    try:
        ext(dbwindow)
    except:
        pass

    t=str(x).split("_")
    ni=len(t)
    if ni > 2:
        winname=t[0]
        for r in range(ni):
            if r==0:
                continue
            elif r==ni-1:
                break

            winname=winname+"_"+t[r]
    else:
        winname=t[0]

    dbwindow=Toplevel(bg="#900C3F")
    dbwindow.title(winname.capitalize())
    dbwindow.geometry("1350x600+0+100")
    dbwindow.resizable(False,False)
    dbwindow.iconphoto(False,img0)
    
    Win.iconify()

    global sdframe
    sdframe=Frame(dbwindow,width=250,height=600,bg="#7E0534")
    sdframe.place(x=0,y=0)

    global tbframe1
    tbframe1=Frame(dbwindow,width=1190,height=600,bg="#900C3F")
    tbframe1.place(x=250,y=0)

    tbl=Label(sdframe,text="Tables",font=("Times 14"),bg="#7E0534",fg="white")
    tbl.place(x=0,y=10,width=250)

    global tb1win
    tb1win=Frame(sdframe,width=250,height=400,bg="#7E0534")
    tb1win.place(x=0,y=40)

    show_tables(x,t[len(t)-1])

    tbsep=ttk.Separator(sdframe,orient="horizontal")
    tbsep.place(x=20,y=35,width=210)

    add_table=Button(sdframe,text="Add table",activebackground="#900C3F",bg="#900C3F",font=("Times 13"),bd=0,anchor=W,padx=20,image=img36,compound="left",command=lambda:create_table(winname,x,t[len(t)-1]))
    add_table.place(x=35,y=485,width=180,height=25)

    delete_database=Button(sdframe,text="Delete db/device",activebackground="#900C3F",bg="#900C3F",font=("Times 13"),bd=0,anchor=W,padx=20,image=img37,compound="left",command=lambda:dell_db(winname,x))
    delete_database.place(x=35,y=515,width=180,height=25)

    cls=Button(sdframe,text="Close",bg="#900C3F",activebackground="#900C3F",font=("Times 13"),bd=0,anchor=W,padx=20,image=img16,compound="left",command=close_db)
    cls.place(x=35,y=545,width=180,height=25)

def show_tables(x,y):
    global tb1frame
    try:
        ext(tb1frame)
    except:
        pass
    
    if x!=1:
        db.execute("Use "+ str(x))
    db.execute("Show tables")

    tables=[]
    for i in db:
        tables.append(i)


    ht2=len(tables)*40
    tb1frame=Frame(tb1win,width=250,height=ht2,bg="#7E0534")
    tb1frame.place(x=0,y=0)

    global v
    v=0

    if ht2 > 400:
        tb1frame.bind_all('<MouseWheel>',lambda event:scroll(event,tb1frame,400,ht2))

    tb=-40
    for i in tables:
        tb=tb+40

        tbtxt=str(i).split("'")
        n=tbtxt[1]
        no=Button(tb1frame,text=str(n).capitalize(),bg="#900C3F",activebackground="#900C3F",font=("Times 13"),anchor=W,padx=10,bd=0,image=img38,compound="left",command= lambda n=n,tb=tb:open_table(n,tb,y))
        no.place(x=10,y=tb,width=230,height=30)

    global shw
    shw=Frame(tb1frame,bg="#3077AF",width=5,height=30)
        
def close_db():
    dbwindow.destroy()
    Win.deiconify()

def create_table(x,y,z):
    Win.update()
    # Win.deiconify()
    Win.title("Add a table --"+x.capitalize())
    # adddevice()
    mod()
    # devlbl.configure(text="New table",image=img36)
    # devnm.place_forget()
    # devsep1.place_forget()
    # devname.place_forget()
    # devty.place_forget()
    # devsep2.place_forget()
    # devtype.place_forget()
    # dropdown.place_forget()
    # menubtn.place_forget()

    sct(z,2)

    # global imglb
    # imglb=Label(deviceframe,image=img39,bg="#900C3F")
    # imglb.place(x=0,y=50,width=400,height=170)

    # global cnl
    # cnl=Button(deviceframe,bg="#7E0534",activebackground="#7E0534",bd=0,text="Cancel",font=("Times 13"),command=cancel)
    # cnl.place(x=440,y=466,width=200,height=30)

    crt.configure(command=lambda :create_database("table",y))
    # Win_Frame.grab_set()

def mod():
    adddevice()

    devlbl.configure(text="New table",image=img36)
    devnm.place_forget()
    devsep1.place_forget()
    devname.place_forget()
    devty.place_forget()
    devsep2.place_forget()
    devtype.place_forget()
    dropdown.place_forget()
    menubtn.place_forget()

    global imglb
    imglb=Label(deviceframe,image=img39,bg="#900C3F")
    imglb.place(x=0,y=50,width=400,height=170)

    global cnl
    cnl=Button(deviceframe,bg="#7E0534",activebackground="#7E0534",bd=0,text="Cancel",font=("Times 13"),command=cancel)
    cnl.place(x=440,y=466,width=200,height=30)

    Win.deiconify()
    Win_Frame.grab_set()

def cancel():
    Win_Frame.grab_release()
    home()
    Win.update()
    Win.iconify()
    Win.title("Desktop-Database")
    dbwindow.deiconify()
    menubtn.place(x=0,y=0,width=35,height=35)
    try:
        crt.configure(command=lambda :create_database("database","none"))
    except:
        pass

def dell_db(x,y):
    ask=messagebox.askyesno("Delete database","Are you sure you want to delete "+str(x).capitalize())
    if ask:
        db.execute("Drop database "+y)
    
        ext(dbwindow)
        Win.deiconify()
        showdatabases(2)
    
def open_table(x,v,z):
    shw.place(x=240,y=v)

    global tbframe
    try:
        ext(tbframe)
    except:
        pass

    tbframe=Frame(dbwindow,width=1190,height=600,bg="#900C3F")
    tbframe.place(x=250,y=0)

    global table_options
    table_options=Frame(tbframe,width=190,height=95,bg="#7E0534")
    # table_options.place(x=900,y=45)

    values_btn=Button(table_options,bg="#900C3F",bd=0,font=("Times 13"),activebackground="#900C3F",text="Add values",anchor=W,padx=20,image=img41,compound="left")
    values_btn.place(x=5,y=5,width=180,height=25)

    column_btn=Button(table_options,bg="#900C3F",bd=0,font=("Times 13"),activebackground="#900C3F",text="Add columns",anchor=W,padx=20,image=img42,compound="left",command= lambda:show_col(x,z,v))
    column_btn.place(x=5,y=35,width=180,height=25)

    del_btn=Button(table_options,bg="#900C3F",bd=0,font=("Times 13"),activebackground="#900C3F",text="Delete table",anchor=W,padx=20,image=img37,compound="left",command=lambda :del_table(x))
    del_btn.place(x=5,y=65,width=180,height=25)

    global columns
    columns=[]
    # print(x)
    db.execute("describe "+str(x))

    for p in db :
        m=str(p).split("'")
        columns.append(m[1])
           
    wid=(len(columns)*140)+(len(columns)*3)+2
    wy=50
    wx=50

    sepa=ttk.Separator(tbframe,orient="horizontal")
    sepa.place(x=wx,y=wy,width=wid)
    wy=wy+2

    for i in columns:
        wsep=ttk.Separator(tbframe,orient="vertical")
        wsep.place(x=wx,y=wy,height=30)

        wx=wx+3

        wlb=Label(tbframe,text=i,padx=10,font=("Times 13"),anchor=W,bg="#7E0534")
        wlb.place(x=wx,y=wy,height=30,width=140)

        wx=wx+140
    
    wsep=ttk.Separator(tbframe,orient="vertical")
    wsep.place(x=wx,y=wy,height=30)

    wy=wy+30
    wx=50

    sepa=ttk.Separator(tbframe,orient="horizontal")
    sepa.place(x=wx,y=wy,width=wid)

    wy=wy+2

    db.execute("select * FROM "+str(x))
    for i in db:
        for j in i:
            wsep=ttk.Separator(tbframe,orient="vertical")
            wsep.place(x=wx,y=wy,height=30)

            wx=wx+3

            wlb=Label(tbframe,text=j,padx=10,font=("Times 13"),anchor=W,bg="#900C3F")
            wlb.place(x=wx,y=wy,height=30,width=140)

            wx=wx+140
        wsep=ttk.Separator(tbframe,orient="vertical")
        wsep.place(x=wx,y=wy,height=30)

        wy=wy+30
        wx=50

        sepa=ttk.Separator(tbframe,orient="horizontal")
        sepa.place(x=wx,y=wy,width=wid)

        wy=wy+2

    size=wid+30

    global row_frame
    row_frame=Frame(tbframe,bg="#7E0534",width=size,height=32)
    # row_frame.place(x=wx,y=wy)
    values_btn.configure(command=lambda wy=wy:show_row(wy))

    global shw2
    shw2=Frame(table_options,bg="#3077AF",width=5,height=25)
    show_row(wy)

    wx=0
    wy=0

    global entry
    entry=[]
    for i in columns:
        wsep=ttk.Separator(row_frame,orient="vertical")
        wsep.place(x=wx,y=wy,height=30)

        wx=wx+3

        wen=Entry(row_frame,font=("Times 13"),bg="#7E0534",bd=0,fg="white",justify=CENTER)
        wen.place(x=wx,y=wy,height=30,width=140)
        entry.append(wen)

        wx=wx+140
    
    wsep=ttk.Separator(row_frame,orient="vertical")
    wsep.place(x=wx,y=wy,height=30)

    wy=wy+30
    wx=0

    sepa=ttk.Separator(row_frame,orient="horizontal")
    sepa.place(x=wx,y=wy,width=wid)

    wx=wx+wid
    wy=wy-30

    add_button=Button(row_frame,bg="#900C3F",activebackground="#900C3F",image=img29,bd=0,command=lambda:add_values(x,v))
    add_button.place(x=wx,y=wy,width=30,height=32)

    imglb2=Label(tbframe,image=img40,bg="#900C3F",bd=0)
    imglb2.place(x=1020,y=5,width=40,height=40)

    drp=Button(tbframe,bg="#900C3F",bd=0,activebackground="#900C3F",image=img34,command=table_opt)
    drp.place(x=1060,y=5,width=20,height=40)

def add_values(x,v):
    val=[]

    for i in entry:
        if i.get()=="":
            messagebox.showerror("Error","Ensure that you have filled all the fields")
            break
        val.append(i.get())

    if len(val)==len(columns):
        add="insert into "+str(x)+" ("
        for i in range(len(columns)):
            if i != 0:
                add=add+","
            add=add+columns[i]
        
        add=add+") values ("

        for i in range(len(columns)):
            if i != 0:
                add=add+","
            add=add+("%s")

        add=add+")"

        add_val="("
        for i in range(len(val)):
            if i==0:
                add_val=add_val+val[i]
            else:
                add_val=add_val+",'"+val[i]+"'"
        
        add_val=add_val+")"

        try:
            db.execute(add,val)
            mydb.commit()
            open_table(x,v)
        except mysql.connector.Error as e:
            messagebox.showerror("Error",e)

def table_opt():
    if table_options.winfo_ismapped()==False:
        table_options.place(x=900,y=45)
    elif table_options.winfo_ismapped()==True:
        table_options.place_forget()

def del_table(x):
    ask=messagebox.askyesno("Delete a table","Are you sure you want to delete "+str(x))
    if ask:
        db.execute("Drop table "+str(x))

        show_tables(1)
        tbframe.destroy()

def show_row(X):
    if table_options.winfo_ismapped()==True:
        table_options.place_forget()

    shw2.place(x=0,y=5)
    if row_frame.winfo_ismapped()==False:
        row_frame.place(x=50,y=X)

def show_col(x,z,v):
    if table_options.winfo_ismapped()==True:
        table_options.place_forget()    
        
    shw2.place(x=0,y=35)
    if row_frame.winfo_ismapped()==True:
        row_frame.place_forget()

    Win.update()
    Win.title("Add a column --"+x.capitalize())
    mod()

    sct(z,2)
    tablenmb.insert(0,x.capitalize())
    tablenmb.configure(state=DISABLED)
    plus.place_forget()
    crt.configure(text=" Add",image=img42,compound="left",command=lambda:alt_col(v,z))

def alt_col(x,y):
    for i in range(len(fieldlst)):
        if i==0:
            continue

        if fieldlst[i].get() =="" or dataty[i].get() =="":
            err="Ensure all the fields in Field "+str(i)+" are not blank"

            messagebox.showerror("Error",err)
            break
        else:
            add_col="Alter TABLE "+tablenmb.get()+" ADD "
            add_col=add_col+fieldlst[i].get()+" "+dataty[i].get()
            
            try:
                print(add_col)
                db.execute(add_col)

                crt.configure(text="",image=img31)
                open_table(tablenmb.get(),x,y)
                Win.after(500,cancel)
            except mysql.connector.Error as e:
                messagebox.showerror("Error",e)

###########################################################################################################################

########################################             ADD DEVICE              ##############################################

def adddevice():
    chgcolor(addevbtn)
    touch(Event)

    global fieldlst
    fieldlst=[]

    global dataty
    dataty=[]

    try:
        ext(settingsframe)
    except:
        pass

    global deviceframe
    try:
        ext(deviceframe)
    except:
        pass

    global plus
    try:
        ext(plus)
    except:
        pass

    global minus
    try:
        ext(minus)
    except:
        pass

    deviceframe=Frame(mainframe,height=500,width=665,bg="#900C3F") 
    deviceframe.place(x=0,y=0)
    deviceframe.bind("<Button-1>",touch)

    sep1=ttk.Separator(deviceframe,orient="vertical")
    sep1.place(x=405,y=30,height=440)

    global devlbl
    devlbl=Label(deviceframe,text="New device",bg="#900C3F",font=("Times 15"),padx=15,image=img21,compound="left")
    devlbl.place(x=0,y=0,width=400,height=50)

    global devnm
    devnm=Label(deviceframe,text="Name",bg="#7E0534",font=("Times 13"))
    devnm.place(x=0,y=70,width=100,height=30)

    global devsep1
    devsep1=ttk.Separator(deviceframe,orient="vertical")
    devsep1.place(x=90,y=70,height=30)

    global devname
    devname=Entry(deviceframe,bg="#7E0534",font=("Times 13"),bd=0,fg="white")
    devname.place(x=100,y=70,width=250,height=30)
    devname.bind("<KeyRelease>",edit)

    global devty
    devty=Label(deviceframe,text="Type",bg="#7E0534",font=("Times 13"))
    devty.place(x=0,y=110,width=100,height=30)

    global devsep2
    devsep2=ttk.Separator(deviceframe,orient="vertical")
    devsep2.place(x=90,y=110,height=30)

    global devtype
    devtype=Entry(deviceframe,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",state="disable",disabledbackground="#7E0534")
    devtype.place(x=100,y=110,width=220,height=30)

    global dropdown
    dropdown=Button(deviceframe,bg="#7E0534",image=img22,bd=0,activebackground="#7E0534",command=lambda :drop(dropdownframe))
    dropdown.place(x=320,y=110,width=30,height=30)

    fieldlst.append(devname)
    dataty.append(devtype)

    global dropdownframe
    dropdownframe=Frame(deviceframe,height=75,width=230,bg="#7E0534",relief="flat",bd=0)

    global phone
    phone=Button(dropdownframe,text="   Smartphone",bg="#7E0534",bd=0,activebackground="#7E0534",font=("Times 13"),image=img23,compound="left",command= lambda :sct(phone,1))
    phone.place(x=0,y=0,height=25,width=230)
    phone.bind('<Enter>',lambda Event:hover(Event,phone))
    phone.bind('<Leave>',lambda Event:hoverout(Event,phone))

    global tablet
    tablet=Button(dropdownframe,text="   Tablet         ",bg="#7E0534",bd=0,activebackground="#7E0534",font=("Times 13"),image=img24,compound="left",command= lambda :sct(tablet,1))
    tablet.place(x=0,y=25,height=25,width=230)
    tablet.bind('<Enter>',lambda Event:hover(Event,tablet))
    tablet.bind('<Leave>',lambda Event:hoverout(Event,tablet))

    global laptop
    laptop=Button(dropdownframe,text="   Laptop        ",bg="#7E0534",bd=0,activebackground="#7E0534",font=("Times 13"),image=img25,compound="left",command= lambda :sct(laptop,1))
    laptop.place(x=0,y=50,height=25,width=230)
    laptop.bind('<Enter>',lambda Event:hover(Event,laptop))
    laptop.bind('<Leave>',lambda Event:hoverout(Event,laptop))

    global fielddesc
    fielddesc=Label(deviceframe,bg="#900C3F",font=("Times 15"),fg="white",text="Field name                       |  Data type")
    fielddesc.place(x=95,y=220)

    global deviceframe1b
    deviceframe1b=Frame(deviceframe,height=250,width=405,bg="#900C3F")
    deviceframe1b.place(x=0,y=250)

    global deviceframe2
    deviceframe2=Frame(deviceframe1b,height=370,width=405,bg="#900C3F")
    deviceframe2.place(x=0,y=0)
    deviceframe2.bind("<Button-1>",touch)

    fieldnm1=Label(deviceframe2,text="Field 1",bg="#7E0534",font=("Times 13"))
    fieldnm1.place(x=0,y=0,width=100,height=30)

    fieldsep1a=ttk.Separator(deviceframe2,orient="vertical")
    fieldsep1a.place(x=90,y=0,height=30)

    global fieldname1a
    fieldname1a=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",disabledbackground="#7E0534")
    fieldname1a.place(x=100,y=0,width=200,height=30)

    fieldsep1b=ttk.Separator(deviceframe2,orient="vertical")
    fieldsep1b.place(x=300,y=0,height=30)

    global fieldname1b
    fieldname1b=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",state="disable",disabledbackground="#7E0534")
    fieldname1b.place(x=303,y=0,width=60,height=30)

    dropdown1=Button(deviceframe2,bg="#7E0534",image=img22,bd=0,activebackground="#7E0534",command= lambda : drop2(0,fieldname1b))
    dropdown1.place(x=363,y=0,width=30,height=30)

    fieldlst.append(fieldname1a)
    dataty.append(fieldname1b)

    global fieldnm2
    fieldnm2=Label(deviceframe2,text="Field 2",bg="#7E0534",font=("Times 13"))

    global fieldsep2a
    fieldsep2a=ttk.Separator(deviceframe2,orient="vertical")

    global fieldname2a
    fieldname2a=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",disabledbackground="#7E0534")

    global fieldsep2b
    fieldsep2b=ttk.Separator(deviceframe2,orient="vertical")

    global fieldname2b
    fieldname2b=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",state="disable",disabledbackground="#7E0534")

    global dropdown2
    dropdown2=Button(deviceframe2,bg="#7E0534",image=img22,bd=0,activebackground="#7E0534",command= lambda : drop2(50,fieldname2b))

    global fieldnm3
    fieldnm3=Label(deviceframe2,text="Field 3",bg="#7E0534",font=("Times 13"))

    global fieldsep3a
    fieldsep3a=ttk.Separator(deviceframe2,orient="vertical")

    global fieldname3a
    fieldname3a=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",disabledbackground="#7E0534")

    global fieldsep3b
    fieldsep3b=ttk.Separator(deviceframe2,orient="vertical")

    global fieldname3b
    fieldname3b=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",state="disable",disabledbackground="#7E0534")

    global dropdown3
    dropdown3=Button(deviceframe2,bg="#7E0534",image=img22,bd=0,activebackground="#7E0534",command= lambda : drop2(100,fieldname3b))

    global fieldnm4
    fieldnm4=Label(deviceframe2,text="Field 4",bg="#7E0534",font=("Times 13"))

    global fieldsep4a
    fieldsep4a=ttk.Separator(deviceframe2,orient="vertical")

    global fieldname4a
    fieldname4a=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",disabledbackground="#7E0534")

    global fieldsep4b
    fieldsep4b=ttk.Separator(deviceframe2,orient="vertical")

    global fieldname4b
    fieldname4b=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",state="disable",disabledbackground="#7E0534")

    global dropdown4
    dropdown4=Button(deviceframe2,bg="#7E0534",image=img22,bd=0,activebackground="#7E0534",command= lambda : drop2(150,fieldname4b))

    global fieldnm5
    fieldnm5=Label(deviceframe2,text="Field 5",bg="#7E0534",font=("Times 13"))

    global fieldsep5a
    fieldsep5a=ttk.Separator(deviceframe2,orient="vertical")

    global fieldname5a
    fieldname5a=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",disabledbackground="#7E0534")

    global fieldsep5b
    fieldsep5b=ttk.Separator(deviceframe2,orient="vertical")

    global fieldname5b
    fieldname5b=Entry(deviceframe2,bg="#7E0534",font=("Times 13"),bd=0,fg="white",disabledforeground="white",state="disable",disabledbackground="#7E0534")

    global dropdown5
    dropdown5=Button(deviceframe2,bg="#7E0534",image=img22,bd=0,activebackground="#7E0534",command= lambda : drop2(200,fieldname5b))

    global dropdownframe2
    dropdownframe2=Frame(deviceframe2,height=125,width=90,bg="#7E0534",relief="flat",bd=0)

    global num
    num=Button(dropdownframe2,text="INT            ",bg="#7E0534",bd=0,activebackground="#7E0534",font=("Times 13"))
    num.place(x=0,y=0,width=90,height=25)
    num.bind('<Enter>',lambda Event : hover(Event,num))
    num.bind('<Leave>',lambda Event : hoverout(Event,num))

    global dec
    dec=Button(dropdownframe2,text="FLOAT      ",bg="#7E0534",bd=0,activebackground="#7E0534",font=("Times 13"))
    dec.place(x=0,y=25,width=90,height=25)
    dec.bind('<Enter>',lambda Event : hover(Event,dec))
    dec.bind('<Leave>',lambda Event : hoverout(Event,dec))

    global txt
    txt=Button(dropdownframe2,text="VARCHAR",bg="#7E0534",bd=0,activebackground="#7E0534",font=("Times 13"))
    txt.place(x=0,y=50,width=90,height=25)
    txt.bind('<Enter>',lambda Event : hover(Event,txt))
    txt.bind('<Leave>',lambda Event : hoverout(Event,txt))

    global dat
    dat=Button(dropdownframe2,text="DATE         ",bg="#7E0534",bd=0,activebackground="#7E0534",font=("Times 13"))
    dat.place(x=0,y=75,width=90,height=25)
    dat.bind('<Enter>',lambda Event : hover(Event,dat))
    dat.bind('<Leave>',lambda Event : hoverout(Event,dat))

    global tim
    tim=Button(dropdownframe2,text="TIME         ",bg="#7E0534",bd=0,activebackground="#7E0534",font=("Times 13"))
    tim.place(x=0,y=100,width=90,height=25)
    tim.bind('<Enter>',lambda Event : hover(Event,tim))
    tim.bind('<Leave>',lambda Event : hoverout(Event,tim))

    # global plus
    plus=Button(Win_Frame,bg="#7E0534",activebackground="#7E0534",bd=0,image=img29,command=addfields)
    plus.place(x=3,y=468,width=29,height=29)

    # global minus
    minus=Button(Win_Frame,bg="#7E0534",activebackground="#7E0534",bd=0,image=img30,command=remfields)

    global scrollbar
    scrollbar=Frame(deviceframe1b,height=200,width=5,bg="#3077AF")

    global x
    x=0

    global nofields
    nofields=1

    global devname2
    devname2=Label(deviceframe,bg="#900C3F",font=("Times 17"),fg="white",wraplength=300)
    devname2.place(x=410,y=30,width=255,height=30)

    global devtype2
    devtype2=Label(deviceframe,bg="#900C3F")
    devtype2.place(x=410,y=60,width=255)

    tablenma=Label(deviceframe,text="Enter the Table name",bg="#7E0534",font=("Times 14"))
    tablenma.place(x=415,y=200,width=243,height=30)

    tablesep=ttk.Separator(deviceframe,orient="horizontal")
    tablesep.place(x=418,y=228,width=237)

    global tablenmb
    tablenmb=Entry(deviceframe,bg="#7E0534",disabledbackground="#7E0534",font=("Times 13"),fg="white",bd=0,justify=CENTER,disabledforeground="white")
    tablenmb.place(x=415,y=230,width=243,height=30)

    nofieldsa=Label(deviceframe,text="Number of fields",bg="#7E0534",font=("Times 13"))
    nofieldsa.place(x=415,y=270,width=200,height=30)

    nofieldsep=ttk.Separator(deviceframe,orient="horizontal")
    nofieldsep.place(x=615,y=270,height=30)

    global nofieldsb
    nofieldsb=Label(deviceframe,text="1",bg="#7E0534",font=("Times 13"),fg="white")
    nofieldsb.place(x=618,y=270,height=30,width=40)

    global crt
    crt=Button(deviceframe,bg="#7E0534",activebackground="#7E0534",bd=0,text="Create",font=("Times 13"),command=lambda :create_database("database","none"))
    crt.place(x=440,y=431,width=200,height=30)

def drop(x):
    global size
    if x.winfo_ismapped()==False:
        x.place(x=93,y=140)
    elif x.winfo_ismapped()==True:
        x.place_forget()
        
def hover(Event,x):
    x.configure(bg="#3077AF",activebackground="#3077AF")

def hoverout(Event,x):
    x.configure(bg="#7E0534",activebackground="#7E0534")


def sct(x,y):
    if x==phone or x=="phone":
        selected="phone"
        try:
            devtype2.configure(image=img26)
        except:
            pass

    elif x==tablet or x=="tablet":
        selected="tablet"
        try:
            devtype2.configure(image=img27)
        except:
            pass

    elif x==laptop or x=="laptop":
        selected="laptop"
        try:
            devtype2.configure(image=img28)
        except:
            pass

    if y==1:
        phone.unbind('<Enter>')
        phone.unbind('<Leave>')

        tablet.unbind('<Enter>')
        tablet.unbind('<Leave>')

        laptop.unbind('<Enter>')
        laptop.unbind('<Leave>')

        devtype.configure(state="normal")
        devtype.delete(0,END)
        devtype.insert(3,selected.capitalize())
        devtype.configure(state="disable")

        x.configure(bg="#3077AF",activebackground="#3077AF")
        if x != phone:
            phone.configure(bg="#7E0534",bd=0,activebackground="#7E0534")
        
        if x != tablet:
            tablet.configure(bg="#7E0534",bd=0,activebackground="#7E0534")

        if x != laptop:
            laptop.configure(bg="#7E0534",bd=0,activebackground="#7E0534")

        # dropdownframe.place_forget()
        drop(dropdownframe)

def edit(Event):
    txt=devname.get()
    devname2.configure(text=txt.capitalize())

def drop2(a,b):
    Y=a+30

    if dropdownframe2.winfo_ismapped()==False:
        dropdownframe2.place(x=303,y=Y)
    elif dropdownframe2.winfo_ismapped()==True:
        if dropdownframe2.winfo_rooty()==a+411:
            dropdownframe2.place_forget()
        else:
            dropdownframe2.place(x=303,y=Y)
    
    num.configure(command= lambda :insert(b,"INT"))
    dec.configure(command= lambda :insert(b,"FLOAT"))
    txt.configure(command= lambda :insert(b,"VARCHAR(255)"))
    dat.configure(command= lambda :insert(b,"DATE"))
    tim.configure(command= lambda :insert(b,"TIME"))

def insert(x,y):
    x.configure(state="normal")
    x.delete(0,END)
    x.insert(2,y)
    x.configure(state="disable")
    dropdownframe2.place_forget()

def addfields():
    global nofields
    if nofields==1:
        fieldnm2.place(x=0,y=50,width=100,height=30)
        fieldsep2a.place(x=90,y=50,height=30)
        fieldname2a.place(x=100,y=50,width=200,height=30)
        fieldsep2b.place(x=300,y=50,height=30)
        fieldname2b.place(x=303,y=50,width=60,height=30)
        dropdown2.place(x=363,y=50,width=30,height=30)

        fieldlst.append(fieldname2a)
        dataty.append(fieldname2b)

        plus.place(x=3,y=436,width=29,height=29)
        minus.place(x=3,y=468,width=29,height=29)

    elif nofields==2:
        fieldnm3.place(x=0,y=100,width=100,height=30)
        fieldsep3a.place(x=90,y=100,height=30)
        fieldname3a.place(x=100,y=100,width=200,height=30)
        fieldsep3b.place(x=300,y=100,height=30)
        fieldname3b.place(x=303,y=100,width=60,height=30)
        dropdown3.place(x=363,y=100,width=30,height=30)

        deviceframe2.bind_all('<MouseWheel>',lambda event:scroll(event,deviceframe2,250,370))

        fieldlst.append(fieldname3a)
        dataty.append(fieldname3b)

    elif nofields==3:
        fieldnm4.place(x=0,y=150,width=100,height=30)
        fieldsep4a.place(x=90,y=150,height=30)
        fieldname4a.place(x=100,y=150,width=200,height=30)
        fieldsep4b.place(x=300,y=150,height=30)
        fieldname4b.place(x=303,y=150,width=60,height=30)
        dropdown4.place(x=363,y=150,width=30,height=30)

        fieldlst.append(fieldname4a)
        dataty.append(fieldname4b)

    elif nofields==4:
        fieldnm5.place(x=0,y=200,width=100,height=30)
        fieldsep5a.place(x=90,y=200,height=30)
        fieldname5a.place(x=100,y=200,width=200,height=30)
        fieldsep5b.place(x=300,y=200,height=30)
        fieldname5b.place(x=303,y=200,width=60,height=30)
        dropdown5.place(x=363,y=200,width=30,height=30)

        fieldlst.append(fieldname5a)
        dataty.append(fieldname5b)
    
    if nofields < 5:
        nofields=nofields+1
    else:
        messagebox.showinfo("Adding more fields","To add more fields, first create the database then access it on the homepage")

    nofieldsb.configure(text=nofields)

def remfields():
    global nofields
    if nofields==2:
        fieldnm2.place_forget()
        fieldsep2a.place_forget()
        fieldname2a.place_forget()
        fieldsep2b.place_forget()
        fieldname2b.place_forget()
        dropdown2.place_forget()

        fieldlst.pop(nofields)
        dataty.pop(nofields)

        minus.place_forget()
        plus.place(x=3,y=468,width=29,height=29)

    elif nofields==3:
        fieldnm3.place_forget()
        fieldsep3a.place_forget()
        fieldname3a.place_forget()
        fieldsep3b.place_forget()
        fieldname3b.place_forget()
        dropdown3.place_forget()

        fieldlst.pop(nofields)
        dataty.pop(nofields)

    elif nofields==4:
        fieldnm4.place_forget()
        fieldsep4a.place_forget()
        fieldname4a.place_forget()
        fieldsep4b.place_forget()
        fieldname4b.place_forget()
        dropdown4.place_forget()

        deviceframe2.unbind('<MouseWheel>')

        fieldlst.pop(nofields)
        dataty.pop(nofields)

    elif nofields==5:
        fieldnm5.place_forget()
        fieldsep5a.place_forget()
        fieldname5a.place_forget()
        fieldsep5b.place_forget()
        fieldname5b.place_forget()
        dropdown5.place_forget()

        fieldlst.pop(nofields)
        dataty.pop(nofields)
    
    if nofields > 1:
        nofields=nofields-1
    
    nofieldsb.configure(text=nofields)

def scroll(Event,a,b,c,):
    z=b-c

    global x
    global p
    global v

    if Event.delta > 0:
        times=int((Event.delta/120)*50)
        if a==dbframe:
            ycor=p+times

            if ycor > 0:
                ycor=0

            p=ycor
            a.place(x=0,y=ycor)
        
        try:
            if a==deviceframe2:
                ycor=x+times

                if ycor > 0:
                    ycor=0

                x=ycor
                a.place(x=0,y=ycor)
        except:
            pass
        
        try:
            if a==tb1frame:
                ycor=v+times

                if ycor > 0:
                    ycor=0

                v=ycor
                a.place(x=0,y=ycor)
        except:
            pass
        
              
        
    elif Event.delta < 0:
        times=int(abs((Event.delta/120)*50))
        if a==dbframe:
            ycor=p-times

            if ycor < z:
                ycor=z

            p=ycor
            a.place(x=0,y=ycor)
        
        try:
            if a==tb1frame:  
                ycor=v-times

                if ycor < z:
                    ycor=z

                v=ycor
                a.place(x=0,y=ycor)
        except:
            pass
        
        try:
            if a==deviceframe2:  
                ycor=x-times

                if ycor < z:
                    ycor=z

                x=ycor
                a.place(x=0,y=ycor)
        except:
            pass

        
    # scor=(x/120)*200
    # scrollbar.place(x=595,y=abs(scor))

def create_database(x,y):
    try:
        if tablenmb.get()!="":
            crt_tab="CREATE TABLE "+tablenmb.get()+" ("
            for i in range(len(fieldlst)):
                if x=="table" and i==0:
                    continue

                if fieldlst[i].get() =="" or dataty[i].get() =="":
                    if i==0:
                        err="Ensure the Name and Type are not blank"
                    else:
                        err="Ensure all the fields in Field "+str(i)+" are not blank"

                    messagebox.showerror("Error",err)
                    crt_tab="CREATE TABLE "+tablenmb.get()+" ("
                    break
                else:
                    if i==0:
                        crt_dat=fieldlst[i].get()+"_"+dataty[i].get()
                        crt_dat1="CREATE DATABASE "+crt_dat
                        crt_dat2="USE "+crt_dat

                    else:
                        crt_tab=crt_tab+fieldlst[i].get()+" "+dataty[i].get()
                        if i < len(fieldlst)-1:
                            crt_tab=crt_tab+","
            crt_tab=crt_tab+")"
            if crt_tab != "CREATE TABLE "+tablenmb.get()+" ()":
                print(crt_tab)

                if x=="table":
                    crt_dat2="Use "+str(y)
                else:
                    db.execute(crt_dat1)

                db.execute(crt_dat2)
                db.execute(crt_tab)

                crt.configure(text="",image=img31)
                if x=='table':
                    show_tables(y)
                    Win.after(2000,cancel)
                else:
                    showdatabases(2)
                    Win.after(2000,adddevice)
        else:
            messagebox.showerror("Error","Enter the Table name")
    except mysql.connector.Error as e:
        messagebox.showerror("Error",e)

###########################################################################################################################

########################################              SETTINGS               ##############################################

def settings():
    chgcolor(settingsbtn)
    touch(Event)

    try:
        ext(deviceframe)
    except:
        pass

    try:
        ext(plus)
    except:
        pass

    try:
        ext(minus)
    except:
        pass

    global settingsframe
    try:
        ext(settingsframe)
    except:
        pass

    settingsframe=Frame(mainframe,height=500,width=665,bg="#900C3F")
    settingsframe.place(x=0,y=0)
    settingsframe.bind("<Button-1>",touch)

    sep2=ttk.Separator(settingsframe,orient="vertical")
    sep2.place(x=276,y=30,height=440)

    usericon=Label(settingsframe,bg="#900C3F",image=img14)
    usericon.place(x=0,y=10)

    user=Label(settingsframe,bg="#900C3F",text=name,font=("Times 20"),fg="white")
    user.place(x=0,y=280,width=276)

    dev=Label(settingsframe,bg="#900C3F",text="Developer  ",font=("Times 15"))
    dev.place(x=0,y=370,width=276)

    git2btn=Button(settingsframe,bg="#7E0534",activebackground="#900C3F",bd=0,text="Github",anchor=W,padx=20,font=("Times 13"),image=img13,compound="left",command=git)
    git2btn.place(x=35,y=410,width=180)

    mailbtn=Button(settingsframe,bg="#7E0534",activebackground="#900C3F",bd=0,text="Email",anchor=W,padx=20,font=("Times 13"),image=img15,compound="left",command=mail)
    mailbtn.place(x=35,y=445,width=180)

    changeusrbtn=Button(settingsframe,bg="#7E0534",activebackground="#900C3F",bd=0,text="Change Username or password",anchor=W,padx=20,font=("Times 13"),image=img18,compound="left",command=changepg)
    changeusrbtn.place(x=331,y=190,width=280,height=27)

    addusrbtn=Button(settingsframe,bg="#7E0534",activebackground="#900C3F",bd=0,text="Add a User",anchor=W,padx=20,font=("Times 13"),image=img19,compound="left",command=addpg)
    addusrbtn.place(x=331,y=225,width=280,height=27)

    delusrbtn=Button(settingsframe,bg="#7E0534",activebackground="#900C3F",bd=0,text="Delete a User",anchor=W,padx=20,font=("Times 13"),image=img20,compound="left",command=delpg)
    delusrbtn.place(x=331,y=260,width=280,height=27)

def changepg():
    global usrpg
    usrpg=Frame(settingsframe,height=470,width=385,bg="#900C3F")
    usrpg.place(x=280,y=30)
    usrpg.bind("<Button-1>",touch)

    global txt
    txt="To make changes insert the correct credentials in the fields below and press the change button"

    global changeps
    changeps=Label(usrpg,bg="#900C3F",text=txt,font=("Times 13"),wraplength=400)
    changeps.place(x=0,y=15,width=380,height=55)

    userlabelb=Label(usrpg,bg="#7E0534",image=img2,width=65,height=28)
    userlabelb.place(x=31,y=80)

    col1b=ttk.Separator(usrpg,orient="vertical")
    col1b.place(x=91,y=80,height=32)

    global usernameb
    usernameb=Entry(usrpg,bg="#7E0534",fg="white",bd=0,font=("Times 14"))
    usernameb.place(x=100,y=80,height=32,width=250)

    global passlabelb
    passlabelb=Label(usrpg,bg="#7E0534",image=img3,width=65,height=28)
    passlabelb.place(x=31,y=160)

    global col2b
    col2b=ttk.Separator(usrpg,orient="vertical")
    col2b.place(x=91,y=160,height=32)

    global passnameb
    passnameb=Entry(usrpg,bg="#7E0534",fg="white",bd=0,font=("Times 14"),show="*")
    passnameb.place(x=100,y=160,height=32,width=250)

    global see2
    see2=Button(usrpg,bg="#900C3F",bd=0,image=img5,height=28,command=lambda: show(passnameb,see2))
    see2.place(x=354,y=160)

    global changebtn
    changebtn=Button(usrpg,bg="#7E0534",activebackground="#900C3F",bd=0,text="Change",font=("Times 13"),command=chng)
    changebtn.place(x=91,y=220,width=200)

    canbtn=Button(usrpg,bg="#900C3F",activebackground="#900C3F",bd=0,image=img17,command=cancl)
    canbtn.place(x=354,y=425)

def chng():
    if usernameb.get()==name and passnameb.get()==passwd:
        changeps.configure(text="Insert the new credentials")
        changebtn.place_forget()

        usernameb.delete(0,END)
        passnameb.delete(0,END)

        passlabelb.place(x=31,y=210)
        col2b.place(x=91,y=210,height=32)
        passnameb.place(x=100,y=210,height=32,width=250)
        see2.place(x=354,y=210)

        global svbtna
        svbtna=Button(settingsframe,bg="#7E0534",activebackground="#900C3F",bd=0,text="Save",font=("Times 13"),command= lambda :sv(nm))
        svbtna.place(x=371,y=150,width=200)

        global svbtnb
        svbtnb=Button(settingsframe,bg="#7E0534",activebackground="#900C3F",bd=0,text="Save",font=("Times 13"),command= lambda:sv(psd))
        svbtnb.place(x=371,y=280,width=200)

def cancl():
    touch(Event)

    if changeps.cget("text")=="Insert the new credentials":
        svbtna.destroy()
        svbtnb.destroy()
        passlabelb.place(x=31,y=160)
        col2b.place(x=91,y=160,height=32)
        passnameb.place(x=100,y=160,height=32,width=250)
        see2.place(x=354,y=160)
        changebtn.place(x=91,y=220,width=200)
        changeps.configure(text=txt)
    else:
        usrpg.destroy()

def sv(x):
    touch(Event)
    if x=="username" and usernameb.get()!="":
        try:
            newusernm="rename user "+hst+" to '"+usernameb.get()+"'@'localhost';"
            # db.execute(newusernm)
            svbtna.configure(text="Saved")
            name=usernameb.get()
        except Exception as e:
            messagebox.showerror("Error",e)

    elif x=="password" and passnameb.get()!="":
        try:
            newpasswd="ALTER USER " + hst + " IDENTIFIED BY " +passnameb.get()+ ";flush privileges;"
            # db.execute(newpasswd)
            svbtnb.configure(text="Saved")
            passwd=passnameb.get()
        except Exception as e:
            messagebox.showerror("Error",e)

def addpg():
    touch(Event)

    global addusrpg
    addusrpg=Frame(settingsframe,height=470,width=385,bg="#900C3F")
    addusrpg.place(x=280,y=30)
    addusrpg.bind("<Button-1>",touch)

    change=Label(addusrpg,bg="#900C3F",text="Insert a Username and Password for the new user",font=("Times 13"),wraplength=400)
    change.place(x=0,y=15,width=380,height=55)

    userlabelc=Label(addusrpg,bg="#7E0534",image=img2,width=65,height=28)
    userlabelc.place(x=31,y=80)

    col1c=ttk.Separator(addusrpg,orient="vertical")
    col1c.place(x=91,y=80,height=32)

    global usernamec
    usernamec=Entry(addusrpg,bg="#7E0534",fg="white",bd=0,font=("Times 14"))
    usernamec.place(x=100,y=80,height=32,width=250)

    passlabelc=Label(addusrpg,bg="#7E0534",image=img3,width=65,height=28)
    passlabelc.place(x=31,y=160)

    col2c=ttk.Separator(addusrpg,orient="vertical")
    col2c.place(x=91,y=160,height=32)

    global passnamec
    passnamec=Entry(addusrpg,bg="#7E0534",fg="white",bd=0,font=("Times 14"),show="*")
    passnamec.place(x=100,y=160,height=32,width=250)

    global see3
    see3=Button(addusrpg,bg="#900C3F",bd=0,image=img5,height=28,command=lambda: show(passnamec,see3))
    see3.place(x=354,y=160)

    global addbtn
    addbtn=Button(addusrpg,bg="#7E0534",activebackground="#900C3F",bd=0,text="   Add",font=("Times 13"),image=img19,compound="left",command=addusr)
    addbtn.place(x=91,y=220,width=200)

    xtbtn=Button(addusrpg,bg="#900C3F",activebackground="#900C3F",bd=0,image=img17,command=lambda : ext(addusrpg))
    xtbtn.place(x=354,y=425)

def addusr():
    touch(Event)

    if usernamec.get()!="" and passnamec.get()!="":
        try:
            newusr="CREATE USER '"+usernamec.get()+"'@'localhost' IDENTIFIED BY '"+passnamec.get()+"';"
            # db.execute(newusr)
            addbtn.configure(text="Added")
        except Exception as e:
            messagebox.showerror("Error",e)

def delpg():
    touch(Event)

    global delusrpg
    delusrpg=Frame(settingsframe,height=470,width=385,bg="#900C3F")
    delusrpg.place(x=280,y=30)
    delusrpg.bind("<Button-1>",touch)

    changec=Label(delusrpg,bg="#900C3F",text="Insert the Username",font=("Times 13"),wraplength=400)
    changec.place(x=0,y=15,width=380,height=55)

    userlabeld=Label(delusrpg,bg="#7E0534",image=img2,width=65,height=28)
    userlabeld.place(x=31,y=80)

    col1d=ttk.Separator(delusrpg,orient="vertical")
    col1d.place(x=91,y=80,height=32)

    global usernamed
    usernamed=Entry(delusrpg,bg="#7E0534",fg="white",bd=0,font=("Times 14"))
    usernamed.place(x=100,y=80,height=32,width=250)

    global delbtn
    delbtn=Button(delusrpg,bg="#7E0534",activebackground="#900C3F",bd=0,text="   Delete",font=("Times 13"),image=img20,compound="left",command=delusr)
    delbtn.place(x=91,y=120,width=200)

    xdbtn=Button(delusrpg,bg="#900C3F",activebackground="#900C3F",bd=0,image=img17,command=lambda : ext(delusrpg))
    xdbtn.place(x=354,y=425)

def delusr():
    if usernamed.get()!="" and usernamed.get()!=name:
        try:
            askdel=messagebox.askyesno("Delete a user","Are you sure you want to delete "+str(usernamed.get()).capitalize())
            if askdel:
                delete="drop user '"+usernamed.get()+"'@'localhost';"
                db.execute(delete)
                delbtn.configure(text="Deleted")
        except Exception as e:
            messagebox.showerror("Error",e)

##########################################################################################################################

########################################              STARTUP               ##############################################

startupframe=Frame(Win,height=450,width=500,bg="#900C3F")
startupframe.place(x=0,y=0)

img1=ImageTk.PhotoImage(Image.open("icons/database.png"))
img2=ImageTk.PhotoImage(Image.open("icons/user.png"))
img3=ImageTk.PhotoImage(Image.open("icons/locked.png"))
img4=ImageTk.PhotoImage(Image.open("icons/eye.png"))
img5=ImageTk.PhotoImage(Image.open("icons/eye2.png"))
img6=ImageTk.PhotoImage(Image.open("icons/error.png"))
img7=ImageTk.PhotoImage(Image.open("icons/menu.png"))
img8=ImageTk.PhotoImage(Image.open("icons/reject.png"))
img9=ImageTk.PhotoImage(Image.open("icons/usericon.png"))
img10=ImageTk.PhotoImage(Image.open("icons/home.png"))
img11=ImageTk.PhotoImage(Image.open("icons/setting.png"))
img12=ImageTk.PhotoImage(Image.open("icons/exit.png"))
img13=ImageTk.PhotoImage(Image.open("icons/github.png"))
img14=ImageTk.PhotoImage(Image.open("icons/userbbig.png"))
img15=ImageTk.PhotoImage(Image.open("icons/gmail.png"))
img16=ImageTk.PhotoImage(Image.open("icons/rejectsm.png"))
img17=ImageTk.PhotoImage(Image.open("icons/back.png"))
img18=ImageTk.PhotoImage(Image.open("icons/changes.png"))
img19=ImageTk.PhotoImage(Image.open("icons/add.png"))
img20=ImageTk.PhotoImage(Image.open("icons/remove-user.png"))
img21=ImageTk.PhotoImage(Image.open("icons/addev.png"))
img22=ImageTk.PhotoImage(Image.open("icons/arrowdown.png"))
img23=ImageTk.PhotoImage(Image.open("icons/smartphone.png"))
img24=ImageTk.PhotoImage(Image.open("icons/tablet.png"))
img25=ImageTk.PhotoImage(Image.open("icons/laptop.png"))
img26=ImageTk.PhotoImage(Image.open("icons/smartphonebig.png"))
img27=ImageTk.PhotoImage(Image.open("icons/tabletbig.png"))
img28=ImageTk.PhotoImage(Image.open("icons/laptopbig.png"))
img29=ImageTk.PhotoImage(Image.open("icons/plus.png"))
img30=ImageTk.PhotoImage(Image.open("icons/minus-sign.png"))
img31=ImageTk.PhotoImage(Image.open("icons/check-mark.png"))
img32=ImageTk.PhotoImage(Image.open("icons/devices.png"))
img33=ImageTk.PhotoImage(Image.open("icons/dbsmall.png"))
img34=ImageTk.PhotoImage(Image.open("icons/down-arrow.png"))
img35=ImageTk.PhotoImage(Image.open("icons/table.png"))
img36=ImageTk.PhotoImage(Image.open("icons/plusbg.png"))
img37=ImageTk.PhotoImage(Image.open("icons/bin.png"))
img38=ImageTk.PhotoImage(Image.open("icons/table2.png"))
img39=ImageTk.PhotoImage(Image.open("icons/tablebg.png"))
img40=ImageTk.PhotoImage(Image.open("icons/table.png"))
img41=ImageTk.PhotoImage(Image.open("icons/row.png"))
img42=ImageTk.PhotoImage(Image.open("icons/column.png"))

titlelabel=Label(startupframe,bg="#900C3F",image=img1,)
titlelabel.place(x=186,y=25)

userlabel=Label(startupframe,bg="#7E0534",image=img2,width=65,height=28)
userlabel.place(x=80,y=210)

col1=ttk.Separator(startupframe,orient="vertical")
col1.place(x=140,y=210,height=32)

username=Entry(startupframe,bg="#7E0534",fg="white",bd=0,font=("Times 14"))
username.place(x=149,y=210,height=32,width=250)
username.insert(0,"Username")
username.bind("<Button-1>",lambda event: pos(event,username))

passlabel=Label(startupframe,bg="#7E0534",image=img3,width=65,height=28)
passlabel.place(x=80,y=300)

col2=ttk.Separator(startupframe,orient="vertical")
col2.place(x=140,y=300,height=32)

passname=Entry(startupframe,bg="#7E0534",fg="white",bd=0,font=("Times 14"),show="")
passname.place(x=149,y=300,height=32,width=250)
passname.insert(0,"Password")
passname.bind("<Button-1>",lambda event: pos(event,passname))

see=Button(startupframe,bg="#900C3F",bd=0,image=img5,height=28,command=lambda :show(passname,see))
see.place(x=405,y=300)
value="hidden"
dimension="small"
size="small"
selected="none"

nm="username"
psd="password"

loginbtn=Button(startupframe,bd=0,text="Log in",font=("Times 13"),bg="#3077AF",command=login)
loginbtn.place(x=138,y=370,width=200,height=30)

##########################################################################################################################

mainloop()