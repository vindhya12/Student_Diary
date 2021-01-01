from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

t=Tk()
t.geometry("425x280")
f55=None




def info():
        n=ttk.Notebook()
        n.place(x=0,y=0,width=425,height=280)
        def demo(a):
                if(n.index("current")==5):
                        home()
        n.bind("<<NotebookTabChanged>>",demo)
        f1=Frame(bg="cyan")
        n.add(f1,text="Insert")

        u1=Label(f1,text="Ent Roll",bg="cyan")
        u1.place(x=100,y=50)
        e1=Entry(f1,textvariable=f)
        e1.place(x=170,y=50)

        u2=Label(f1,text="Ent Name",bg="cyan")
        u2.place(x=100,y=80)
        e2=Entry(f1,textvariable=g)
        e2.place(x=170,y=80)

        u3=Label(f1,text="Maths Mark",bg="cyan")
        u3.place(x=100,y=110)
        e3=Entry(f1,textvariable=h)
        e3.place(x=170,y=110)

        u4=Label(f1,text="Phy Mark",bg="cyan")
        u4.place(x=100,y=140)
        e4=Entry(f1,textvariable=i)
        e4.place(x=170,y=140)

        u5=Label(f1,text=" Chem Mark",bg="cyan")
        u5.place(x=100,y=170)
        e5=Entry(f1,textvariable=j)
        e5.place(x=170,y=170)

        b1=Button(f1,text="Insert",command=insert)
        b1.place(x=200,y=210)
        b2=Button(f1,text="logIn",command=loginpg)
        b2.place(x=3,y=4)

        f2=Frame(bg="cyan")
        k=StringVar()
        n.add(f2,text="Search")


        u1=Label(f2,text="Ent Roll",bg="cyan")
        u1.place(x=100,y=50)
        e1=Entry(f2,textvariable=k)
        e1.place(x=170,y=50)

        def search():
                db=sqlite3.connect('vindu4.db')
                cr=db.cursor()
                r=cr.execute("select * from login where ROLL='"+k.get()+"'")
                for r1 in r:
                        u2=Label(f2,text="Ent Name",bg="cyan")
                        u2.place(x=100,y=80)
                        un=Entry(f2)
                        un.place(x=170,y=80)
                        un.insert(0,r1[1])

                        u3=Label(f2,text="Maths Mark",bg="cyan")
                        u3.place(x=100,y=110)
                        uo=Entry(f2)
                        uo.place(x=170,y=110)
                        uo.insert(0,r1[2])

                        u4=Label(f2,text="Phy Mark",bg="cyan")
                        u4.place(x=100,y=140)
                        up=Entry(f2)
                        up.place(x=170,y=140)
                        up.insert(0,r1[3])

                        u5=Label(f2,text=" Chem Mark",bg="cyan")
                        u5.place(x=100,y=170)
                        uq=Entry(f2)
                        uq.place(x=170,y=170)
                        uq.insert(0,r1[4])

                        break
                else:
                        messagebox.showinfo("Invalid","Invalid Roll No")
                        k.set("")
                        
                db.commit()
                db.close()
        
        b1=Button(f2,text="Search",command=search)
        b1.place(x=310,y=50)
        

        all(n)

        f4=Frame(bg="cyan")
        l=StringVar()
        n.add(f4,text="Update")

        u1=Label(f4,text="Ent Roll",bg="cyan")
        u1.place(x=100,y=50)
        e1=Entry(f4,textvariable=l)
        e1.place(x=170,y=50)


        def updt1():
                db=sqlite3.connect('vindu4.db')
                cr=db.cursor()
                r=cr.execute("select * from login where ROLL='"+l.get()+"'")
                for r1 in r:
                        m=StringVar()
                        n=StringVar()
                        o=StringVar()
                        p=StringVar()
                        u2=Label(f4,text="Ent Name",bg="cyan")
                        u2.place(x=100,y=80)
                        un=Entry(f4,textvariable=m)
                        un.place(x=170,y=80)
                        un.insert(0,r1[1])

                        u3=Label(f4,text="Maths Mark",bg="cyan")
                        u3.place(x=100,y=110)
                        uo=Entry(f4,textvariable=n)
                        uo.place(x=170,y=110)
                        uo.insert(0,r1[2])

                        u4=Label(f4,text="Phy Mark",bg="cyan")
                        u4.place(x=100,y=140)
                        up=Entry(f4,textvariable=o)
                        up.place(x=170,y=140)
                        up.insert(0,r1[3])

                        u5=Label(f4,text=" Chem Mark",bg="cyan")
                        u5.place(x=100,y=170)
                        uq=Entry(f4,textvariable=p)
                        uq.place(x=170,y=170)
                        uq.insert(0,r1[4])

                        def updt2():
                                db=sqlite3.connect('vindu4.db')
                                cr=db.cursor()
                                cr.execute("update login set NAME='"+m.get()+"',MATHS='"+n.get()+"',PHY='"+o.get()+"',CHEM='"+p.get()+"' where ROLL='"+l.get()+"'")
                                db.commit()
                                db.close()
                                all1(f55)
                                messagebox.showinfo("Update","Your data has been sucessfully Updated")
                                l.set("")
                                m.set("")
                                n.set("")
                                o.set("")
                                p.set("")                               


                        b2=Button(f4,text="Update",command=updt2)
                        b2.place(x=200,y=210)
                        break
                else:
                        messagebox.showinfo("Invalid","Invalid Roll No")
                        l.set("")
                        

                        
                db.commit()
                db.close()
                
                
        b1=Button(f4,text="Update",command=updt1)
        b1.place(x=310,y=50)
        


        f5=Frame(bg="cyan")
        q=StringVar()
        r=StringVar()
        n.add(f5,text="Delete")

        u1=Label(f5,text="Ent Roll",bg="cyan")
        u1.place(x=100,y=50)
        e1=Entry(f5,textvariable=q)
        e1.place(x=170,y=50)

        
        u2=Label(f5,text="Ent Name",bg="cyan")
        u2.place(x=100,y=80)
        e2=Entry(f5,textvariable=r)
        e2.place(x=170,y=80)

        def dele1():
                db=sqlite3.connect('vindu4.db')
                cr=db.cursor()
                cr.execute("delete from login where NAME='"+r.get()+"' AND ROLL='"+q.get()+"'")                
                db.commit()
                db.close()
                all1(f55)
                messagebox.showinfo("Delete","Your data has been sucessfully deleted")
                r.set("")
                q.set("")


        b1=Button(f5,text="Delete",command=dele1)
        b1.place(x=200,y=110)




        f6=Frame(bg="cyan")
        n.add(f6,text="Logout")


def all1(f3):
        for w in f3.winfo_children():
                    w.destroy()
        db=sqlite3.connect('vindu4.db')
        cr=db.cursor()
        r=cr.execute("select * from login")
        Label(f3,text="Roll",bg="cyan").place(x=50,y=15)
        Label(f3,text="Name",bg="cyan").place(x=100,y=15)
        Label(f3,text="Maths",bg="cyan").place(x=150,y=15)
        Label(f3,text="Phy",bg="cyan").place(x=200,y=15)
        Label(f3,text="Chem",bg="cyan").place(x=250,y=15)
        x=50
        y=30
        for r1 in r:
                Label(f3,text=r1[0],bg="cyan").place(x=x,y=y)
                x=x+50
                Label(f3,text=r1[1],bg="cyan").place(x=x,y=y)
                x=x+50
                Label(f3,text=r1[2],bg="cyan").place(x=x,y=y)
                x=x+50
                Label(f3,text=r1[3],bg="cyan").place(x=x,y=y)
                x=x+50
                Label(f3,text=r1[4],bg="cyan").place(x=x,y=y)
                x=50
                y=y+15
        db.commit()
        db.close()

def all(n=ttk.Notebook):
        f3=Frame(bg="cyan")
        n.add(f3,text="Show All")
        global f55
        f55=f3
        all1(f3)



f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
j=StringVar()
def insert():
        db=sqlite3.connect('vindu4.db')
        cr=db.cursor()
        cr.execute("insert into login values('"+f.get()+"','"+g.get()+"','"+h.get()+"','"+i.get()+"','"+j.get()+"')")
        messagebox.showinfo("Insert","Sucessfully Inserted")
        f.set("")
        g.set("")
        h.set("")
        i.set("")
        j.set("")

        db.commit()
        db.close()

        all1(f55)




d=StringVar()
e=StringVar()

def login():
        db=sqlite3.connect('vindu3.db')
        cr=db.cursor()
        r=cr.execute("select * from login where NAME='"+d.get()+"' AND PASS='"+e.get()+"'")
        for r1 in r:
                #u3=Label(f1,text="Welcome",bg="red")
                #u3.place(x=220,y=140)
                messagebox.showinfo("LogIn","Welcome")
                info()
                break
        else:
                #u3=Label(f1,text="Invalid Name or Pass",bg="red")
                #u3.place(x=220,y=140)
                messagebox.showinfo("Fail","Invalid Name or Pass")
        d.set("")
        e.set("")
        db.commit()
        db.close()



a=StringVar()
b=StringVar()
c=StringVar()

def show():
        db=sqlite3.connect('vindu3.db')
        cr=db.cursor()
        cr.execute("insert into login values('"+a.get()+"','"+b.get()+"','"+c.get()+"')")
        messagebox.showinfo("Register","You have been sucessfully registered")
        a.set("")
        b.set("")
        c.set("")
        db.commit()
        db.close()
def home():
        f8=Frame(bg="cyan")
        f8.place(x=0,y=0,width=425,height=280)

        u1=Label(f8,text=" Home Page ",font=("",25),bg="cyan")
        u1.place(x=130,y=20)
        b1=Button(f8,text="Rgister",font=("",15),command=regispg,width=12,height=2,bg="cyan")
        b1.place(x=60,y=120)
        b2=Button(f8,text="logIn",font=("",15),command=loginpg,width=12,height=2,bg="cyan")
        b2.place(x=250,y=120)

def regispg():
        f9=Frame(bg="cyan")
        f9.place(x=0,y=0,width=425,height=280)

        u1=Label(f9,text="Enter Name",bg="cyan")
        u1.place(x=100,y=50)
        e1=Entry(f9,textvariable=a)
        e1.place(x=170,y=50)
        u2=Label(f9,text="Enter Pass",bg="cyan")
        u2.place(x=100,y=80)
        e2=Entry(f9,show="*",textvariable=b)
        e2.place(x=170,y=80)
        u3=Label(f9,text="Enter En.No",bg="cyan")
        u3.place(x=100,y=110)
        e3=Entry(f9,textvariable=c)
        e3.place(x=170,y=110)
        b1=Button(f9,text="Rgister",command=show)
        b1.place(x=200,y=150)        
        b3=Button(f9,text="Home",command=home)
        b3.place(x=3,y=4)
        b4=Button(f9,text="Login",command=loginpg)
        b4.place(x=380,y=4)
def loginpg():
        f10=Frame(bg="cyan")
        f10.place(x=0,y=0,width=425,height=280)

        u1=Label(f10,text="Enter Name",bg="cyan")
        u1.place(x=100,y=50)
        e1=Entry(f10,textvariable=d)
        e1.place(x=170,y=50)
        u2=Label(f10,text="Enter Pass",bg="cyan")
        u2.place(x=100,y=80)
        e2=Entry(f10,show="*",textvariable=e)
        e2.place(x=170,y=80)
        b1=Button(f10,text="logIn",command=login)
        b1.place(x=200,y=120)
        b3=Button(f10,text="Register",command=regispg)
        b3.place(x=360,y=4)
        b2=Button(f10,text="Home",command=home)
        b2.place(x=3,y=4)


home()
t.mainloop()
