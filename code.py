import random
import tkinter
import csv
import random
import mysql.connector
def submit():
    s=""
    x=E.get()
    y=F.get()
    mycon=mysql.connector.connect(host="localhost",password="tiya@03",user="root",database="forms")
    mycur=mycon.cursor()
    mycur.execute("select concat(First_Name,'_',Last_Name) AS USER,Password from form")
    data=mycur.fetchall()
    for i in data:
        if(i[0]==x):
            if(i[1]==y):
                Al1=tkinter.Label(text="login Successful",font=("Times New Roman",10,"bold"),fg="White",bg="Green").place(x=0,y=180)
                window=tkinter.Tk()
                window.title("GAME")
                window.geometry('3000x3000')
                window.configure(bg="Pink")
                def greet():
                    S="""HELLO WELCOME TO PLAY TO WIN\nHERE WE ARE GOING TO PLAY 3 MINI GAMES
                    ONE DICE COULD FETCH YOU MAXIMUM 6 AND A SURPRISE FROM OUR GOODIE STORE
                    THEN A RIDDLE AND A MENTAL ABILITY QUESTION WILL GIVE YOU 30 AND 10 POINTS RESPECTIVELY\nWITH THOSE YOU WOULD BE ELIGIBLE TO WIN A BOOK FROM OUR BOOKSTORE
                    SOUNDS EXCITING ?"""
                    l1=tkinter.Label(window,text=S,font=("Broadway",15),fg="Black",bg="Pink").place(x=180,y=30)
                l1=tkinter.Label(window,text="WELCOME TO PLAY TO WIN",font=("Algerian",21),fg="Blue",bg="Pink").pack()
                b5=tkinter.Button(window,text="START >>>",command=greet,bg="Green").place(x=0,y=0)
                def roll_a_die():
                    x=str(random.randint(1,6))
                    l1=tkinter.Label(window,text="Your Score is : "+x,bg="Pink").place(x=0,y=210)
                    f=open(r"https://github.com/Tiagupt03/PlayToWin/blob/main/dice.txt","r")
                    r=csv.reader(f)
                    for e in r:
                        if(e[0]==x):
                            Q=tkinter.Label(window,text="YOU HAVE GOT A  "+e[1],bg="Pink").place(x=0,y=240)  
                    P=tkinter.Label(window,text="THANK YOU FOR VISITING US",bg="Pink").place(x=0,y=270)
                def play_a_riddle():
                    f=open(r"https://github.com/Tiagupt03/PlayToWin/blob/main/riddles.txt","r")
                    l=f.readlines()
                    k=random.randrange(1,37,2)
                    P=tkinter.Label(window,text="Q : "+l[k-1],bg="Pink").place(x=300,y=210)
                    Q=tkinter.Entry(window,width=30,bg="Light green")
                    Q.place(x=300,y=240)
                    def solve():
                        R=tkinter.Label(window,text="THE REAL ANSWER IS: "+l[k],bg="Pink").place(x=300,y=300)
                        if(Q.get() in l[k]):
                            R=tkinter.Label(window,text="Score is 30",bg="Pink").place(x=300,y=330)
                        else:
                            D=tkinter.Label(window,text="Better Luck Next Time",bg="Pink").place(x=300,y=330)
                    T=tkinter.Button(window,text="SUBMIT",command=solve,bg="Light blue").place(x=300,y=270)
                def birthday():
                    V=tkinter.Label(window,text="PLEASE ENTER THE DESIRED DATE (DD-MM-YYYY) ?",bg="Pink").place(x=810,y=210)
                    S=tkinter.Entry(window,width=15,bg="Light green")
                    S.place(x=810,y=240)
                    P=tkinter.Label(window,text="GUESS THE DAY ?",bg="Pink").place(x=810,y=270)
                    Q=tkinter.Entry(window,width=15,bg="Light green")
                    Q.place(x=810,y=300)
                    def solve():
                        n=S.get()
                        v=int(n[6:])
                        f=n[3:5]
                        d={"01":0,"02":3,"03":3,"04":6,"05":1,"06":4,"07":6,"08":2,"09":5,"10":0,"11":3,"12":5}
                        l={0:"sunday",1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saurday"}
                        if(1900<=v<2000):
                            r=int(n[8:])
                        else:
                            r=int(n[7:])+100
                        g=d[f]
                        b=int(n[:2])
                        a=int(r/4)
                        p=a+g+r+b
                        e=p%7
                        k=l[e].upper()
                        R=tkinter.Label(window,text="THE REAL ANSWER IS: "+k,bg="Pink").place(x=810,y=330)
                        if(Q.get()==k):
                            R=tkinter.Label(window,text="Score is 10",bg="Pink").place(x=810,y=360)
                        else:
                            D=tkinter.Label(window,text="Better Luck Next Time",bg="Pink").place(x=810,y=390)       
                    T=tkinter.Button(window,text="SUBMIT",command=solve,bg="Light blue").place(x=930,y=300)
                def score():
                    y=e.get()
                    t=int(y[0])
                    i=y[1]
                    g=t*10
                    con=mysql.connector.connect(user="root",password="tiya@03",host="localhost",database="project")
                    cur=con.cursor()
                    if(g<30):
                        h=tkinter.Label(window,text="WE ARE EXTREMELY SORRY BUT YOU DON'T HAVE ENOUGH POINTS",bg="Pink").place(x=0,y=390)
                    elif(g==30):
                        m=30
                    elif(g==40):
                        if(i=="1" or i=="2"):
                            m=50
                            o=tkinter.Label(window,text="JACKPOT50",bg="Pink").place(x=0,y=420)
                        else:
                            m=40
                    cur.execute("select * from books where PRICE={}".format(m))
                    data=cur.fetchall()
                    for d in data:
                        U=tkinter.Label(window,text="YOU HAVE WON : "+str(d),bg="Pink").place(x=0,y=480)
                def exit_t():
                    window.destroy()
                b1=tkinter.Button(window,text="CALENDER ",command=birthday,bg="Yellow").place(x=810,y=180)    
                b2=tkinter.Button(window,text="PLAY RIDDLES",command=play_a_riddle,bg="Yellow").place(x=300,y=180)
                b3=tkinter.Button(window,text="ROLL THE DIE",command=roll_a_die,bg="Yellow").place(x=0,y=180)
                h=tkinter.Label(window,text="ENTER YOUR TOTAL SCORE",bg="Pink").place(x=0,y=360)
                e=tkinter.Entry(window,width=15,bg="Light green")
                e.place(x=180,y=360)
                b=tkinter.Button(window,text="SUBMIT",command=score,bg="Yellow").place(x=300,y=360)
                W=tkinter.Label(window,text="EXIT",font=("Elephant",21),fg="Green",bg="Pink").place(x=0,y=570) 
                B=tkinter.Button(window,text="X",command=exit_t,bg="Red",fg="Black").place(x=120,y=582)
                window.mainloop()        
                login.destroy()
            else:
                Al1=tkinter.Label(text="login Unsuccessful",font=("Times New Roman",10,"bold"),fg="White",bg="Green").place(x=0,y=180)
        else:
            H=tkinter.Label(login,text="NOT A REGISTERED USER",bg="green",fg="red")
def register():
    def display():
        con=mysql.connector.connect(host="localhost",password="tiya@03",user="root",database="forms")
        cur=con.cursor()
        x=d.get()
        y=e.get()
        z=f.get()
        r=l.get()
        t=k.get()
        if(r!=t):
            u=tkinter.Label(register,text="password doesn't match",bg="green",fg="red").place(x=0,y=420)
        else:
            cur.execute("insert into form value('{}','{}',{},'{}')".format(x,y,z,r))
            con.commit()
            o=tkinter.Label(register,text="USER REGISTERED SUCCESSFULLY",fg="red",bg="green").place(x=0,y=420)
    register=tkinter.Tk()
    register.configure(bg="green")
    register.geometry("900x600")
    register.title("REGISTERATION FORM")
    heading =tkinter.Label(register,text="REGISTERATION FORM",fg="black",bg="yellow",width="500",height="3",font="10").pack()
    a=tkinter.Label(register,text="FIRST NAME",fg="yellow",bg="green",font="5").place(x=0,y=90)
    b=tkinter.Label(register,text="LAST NAME",fg="yellow",bg="green",font="5").place(x=390,y=90)
    c=tkinter.Label(register,text="AGE",fg="yellow",bg="green",font="5").place(x=30,y=180)
    m=tkinter.Label(register,text="PASSWORD",fg="yellow",bg="green",font="5").place(x=0,y=270)
    n=tkinter.Label(register,text="CONFIRM PASSWORD",fg="yellow",bg="green",font="5").place(x=390,y=270)
    d=tkinter.Entry(register,width="15") 
    d.place(x=120,y=90)
    e=tkinter.Entry(register,width="15")
    e.place(x=510,y=90)
    f=tkinter.Entry(register,width="15")
    f.place(x=120,y=180)
    l=tkinter.Entry(register,width="15")
    l.place(x=120,y=270)
    k=tkinter.Entry(register,width="15")
    k.place(x=600,y=270)
    s=tkinter.Button(register,text="SUBMIT",command=display).place(x=300,y=360)  
    register.mainloop()
login=tkinter.Tk()
login.title("LOGIN")
login.geometry('300x300')
login.configure(bg="Green")
Al1=tkinter.Label(text="USERNAME",font=("Ariel",10,"bold"),fg="White",bg="Green").place(x=0,y=0)
E=tkinter.Entry(width=30,bg="Light green")
E.place(x=180,y=0)
Bl1=tkinter.Label(text="PASSWORD",font=("Ariel",10,"bold"),fg="White",bg="Green").place(x=0,y=60)
F=tkinter.Entry(width=30,bg="Light green",show="*")
F.place(x=180,y=60)
b4=tkinter.Button(text="SUBMIT",command=submit,bg="Light blue").place(x=120,y=120)
Cl1=tkinter.Button(text="NEW USER ?",command=register,font=("Ariel",15,),fg="Red",bg="Green").place(x=90,y=150)
login.mainloop()
