from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import os
import datetime
from tkcalendar import DateEntry


ls=os.listdir("files/" )









def check():
    check()


def ope():


    root = Toplevel(top)
    root.geometry("980x560")
    root.title("File Base Record System")
    wl=Label(root,text="Welcome To File Base Record System",relief=GROOVE,bd=5,pady=10,font=("times new roman",30,"bold"),bg="yellow",
             fg="red" ).pack(fill=X)
    root.configure(bg="#EEFFF9")
    sc=Label(root,text="Enter File Deatails",bd=2,relief=GROOVE,font=("Cambira",15,"bold")).place(x=220,y=100,w=250,h=25)

    root.name=StringVar()
    root.r_no=StringVar()
    root.Email=StringVar()
    root.Mobile=StringVar()
    root.Date=StringVar()
    root.Branch=StringVar()
    root.Address=StringVar()
    root.city=StringVar()
    root.Course=StringVar()
    root.Payment=StringVar()
    




    
    
    
   
    name=Label(root,text="Name",bd=2,relief=GROOVE,font=("cambria",12,"bold")).place(x=30,y=160,w=60,h=23)
    NE=Entry(root,w=30,bd=2,relief=GROOVE,textvariable=root.name).place(x=110,y=160)
    
    Emil=Label(root,text="Email",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=30,y=210,w=60,h=23)
    EE=Entry(root,w=30,bd=2,relief=GROOVE,textvariable=root.Email).place(x=110,y=210)

    RNo=Label(root,text="Roll_No",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=30,y=260,w=64,h=23)
    EE=Entry(root,w=30,bd=2,relief=GROOVE,textvariable=root.r_no).place(x=110,y=260)

    Brnch=Label(root,text="Branch",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=30,y=310,w=66,h=23)
    combo=ttk.Combobox(root,width=20,state="readonly",textvariable=root.Branch)
    combo['values']=("Computer","IT","Mechanical","Electrical","Civil")
    combo.place(x=115,y=310,w=180,h=23)

    Mbl=Label(root,text="Molile",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=30,y=360,w=66,h=23)
    EE=Entry(root,w=30,bd=2,relief=GROOVE,textvariable=root.Mobile).place(x=110,y=360)

    std=Label(root,text="Date",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=310,y=160,w=66,h=23)
    #EE=Entry(root,w=30,bd=2,relief=GROOVE,textvariable=root.Date).
    cal = DateEntry(root, width=12, year=2019, month=6, day=22,textvariable=root.Date,
    background='darkblue', foreground='white', borderwidth=2)
    cal.place(x=390,y=160,w=178)

    std=Label(root,text="State",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=300,y=210,w=76,h=23)
    #EE=Entry(root,w=30,bd=2,relief=GROOVE,textvariable=root.Address).place(x=390,y=210)
    combo=ttk.Combobox(root,width=20,state="readonly",textvariable=root.Address)
    combo['values']=("Delhi","Utter Pradesh","Rajasthan","Goa","Maharashtra","Gujrat")
    combo.place(x=390,y=210,w=180,h=23)

    city=Label(root,text="City",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=310,y=260,w=66,h=23)
   # EE=Entry(root,w=30,bd=2,relief=GROOVE,textvariable=root.city).place(x=390,y=260)
    combo1=ttk.Combobox(root,width=20,state="readonly",textvariable=root.city)
    combo1['values']=("Aurangabad","Pune","Nashik","Bhusawal","Nagpur","Jalgoan")
    combo1.place(x=390,y=260,w=180,h=23)

    course=Label(root,text="Course",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=310,y=310,w=66,h=23) 
    combo=ttk.Combobox(root,width=20,state="readonly",textvariable=root.Course)
    combo['values']=("Java","C","C++","Vb.net","Android","Python")
    combo.place(x=394,y=310,w=180,h=23)

    dgree=Label(root,text="Payment",bd=2,relief=GROOVE,font=("cambira",12,"bold")).place(x=300,y=360,w=76,h=23)
    combo=ttk.Combobox(root,width=30,state="readonly",textvariable=root.Payment)
    combo['values']=("Paytm","G-Pay","Phone-pay","ATM")
    combo.place(x=394,y=360,w=180,h=23)
    
    btnframe = Frame(root,bd=8,relief=GROOVE)
    btnframe.place(x=50,y=450,w=870,h=90)

    def save_data():
        if root.name.get()=="":
            messagebox.showerror("Error","Name must be Required")
        elif root.Email.get()=="":
            messagebox.showerror("Error","Email must be Required")

        elif root.r_no.get()=="":
            messagebox.showerror("Error","Roll No must be Required")
            
        elif root.Branch.get()=="":
            messagebox.showerror("Error","Branch must be Required")

        elif root.Mobile.get()=="":
            messagebox.showerror("Error","Mobile must be Required")
            
        elif root.Date.get()=="":
            messagebox.showerror("Error"," Date must be Required")
            
        elif root.Address.get()=="":
            messagebox.showerror("Error","Address must be Required")

        elif root.city.get()=="":
            messagebox.showerror("Error","City must be Required")

        elif root.Course.get()=="":
            messagebox.showerror("Error","Course must be Required")

        elif root.Payment.get()=="":
            messagebox.showerror("Error","Payment must be Required")
            
            

              
        else:
           
            f=open("files/"+str(root.name.get())+".txt","w")
            f.write(
                    str(root.r_no.get())+"  \n"+
                    str(root.name.get())+"\n"+
                    str(root.Email.get())+"\n"+
                    str(root.Branch.get())+"\n"+
                    str(root.Mobile.get())+"\n"+
                    str(root.Course.get())+"\n"+
                    str(root.Date.get())+"\n"+
                    str(root.Address.get())+"\n"+
                    str(root.city.get())+"\n"+
                    str(root.Payment.get())
                )

            f.close()
            messagebox.showinfo("Success","Record has benn Saved successsfully..!!!")
            l1 = os.listdir("files/")
            
       


    
    sv=Button(btnframe,text="Save",command=save_data,font=("cambria",15,"bold"),bd=10,width=10).grid(row=0,column=0,padx=15,pady=10)
    
    def delete():
        present="no"
        if root.name.get()=="":
             messagebox.showinfo("Error","name must be rquired")
        else:
            global f
            f=os.listdir("files/")

        if len(f)>0:
            
            for i in f:
                if i.split(".")[0]==root.name.get():
                    present="yes"
        if present=="yes":
           global ask
        ask= messagebox.askyesno("Delete","Do you want to delete ")
        if ask>0:
              os.remove("files/"+root.name.get()+".txt")
              messagebox.showinfo("Delete","File Deleted successfully..!!")
              l1 = os.listdir("files/")
        else:
              messagebox.showerror("Error","file Not Found")
                                     
    dele=Button(btnframe,text="Delete",command=delete,font=("cambria",15,"bold"),bd=10,width=10).grid(row=0,column=1,padx=10,pady=10)

    def clr():
        root.name.set("")
        root.r_no.set("")
        root.Email.set("")
        root.Mobile.set("")
        root.Date.set("")
        root.Branch.set("")
        root.Address.set("")
        root.city.set("")
        root.Course.set("")
        root.Payment.set("")
    
    
    clr=Button(btnframe,text="Clear",command=clr,font=("cambria",15,"bold"),bd=10,width=10).grid(row=0,column=2,padx=10,pady=10)
    def ex():
        optio=messagebox.askyesno("Exit","Really Want To Exit...")
        if optio>0:
        
                top.destroy()
        else:
            return

    def logot():
        opti=messagebox.askyesno("Logout","Really Want To Logout...")
        if opti>0:
        
                root.destroy()
        else:
            return
       
    lg=Button(btnframe,text="Logout",command=logot,font=("cambria",15,"bold"),bd=10,width=10).grid(row=0,column=3,padx=10,pady=10)

   
        
    ex=Button(btnframe,text="Exit",command=ex,font=("cambria",15,"bold"),bd=10,width=10).grid(row=0,column=4,padx=10,pady=10)
         
    filfr=Frame(root,bd=10,relief=GROOVE)
    filfr.place(x=650,y=100,w=300,h=340)
    fti=Label(filfr,text="All Files",font=("times new roman",16,"bold"),bd=5,relief=GROOVE).pack(side=TOP,fill=X)


    def show_files():
        files=listdir("files/")
        if len(files)>0:
                for i in files:
                    root.filt.insert(END,i)

    
    scroll_y=Scrollbar( filfr,orient=VERTICAL)
    root.filt=Listbox(filfr,yscrollcommand=scroll_y.set)
    l1 = os.listdir("files/")
    for a in range (0,len(l1)):
        root.filt.insert(END,l1[a])
        #print(l1[a])

    #root.filt.insert(END,i)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config()
    root.filt.pack(fill=BOTH,expand=1)
    #root.show_files()

   
    '''''  def get_data():
             get.cursor=root.filt.curselection()
             #print(root.filt.get( get.cursor))
             f1=open("files/"+root.filt.get( get.cursor))
             value=[]
             for f in f1: '''
             
         

    
    root.resizable(0, 0)    
    root.mainloop()


top = Tk()  
  
top.geometry("520x370")

top.configure(bg='#FFFEEE')



top.title("User Login")
Tl=Button(top,text="Login",relief=GROOVE,font=("Cambria",30,"bold"),fg="black").place(x=150,y=30,w=180,h=55)

uname = Label(top, text = "Username",font=("cambria",12,"bold"),fg="red").place(x = 60,y = 120)
user=StringVar()
pswd=StringVar()

password=Label(top,text="Password",font=("cambria",12,"bold"),fg="Red" ).place(x=60,y=180)
t1=Entry (top,w=30,bd=2,relief=GROOVE,show="*",textvariable=user)
t1.place(x=152,y=180,h=25,w=180)
t2=Entry(top,w=30,bd=2,relief=GROOVE,textvariable=pswd)
t2.place(x=152,y=120,h=25,w=180)

img = ImageTk.PhotoImage(file="login.jpg")
logo = Label(top, image=img)
logo.place(x=350,y=100,h=150,w=150)
#img = Image.PhotoImage(file="login.jpg")
#img.place(x=100,y=10)

#(img.show()).place(x=130,y=120,h=30,w=60) 
Sbt=Button(top,text="Submit",relief=GROOVE,command=check,font=("cambria",15,"bold"),fg="Green").place(x=170,y=300,w=100)
def exi():
    option=messagebox.askyesno("Exit","Really Want To Exit...")
    if option>0:
        
        top.destroy()
    else:
            return
       
    
TE=Button(top,text="Exit",relief=GROOVE,command=exi,font=("Cambria",15,"bold"),fg="Green").place(x=240,y=240,w=100)
def rest():
    user.set("")
    pswd.set("")
TE=Button(top,text="Reset",relief=GROOVE,command=rest,font=("Cambria",15,"bold"),fg="Green").place(x=110,y=240,w=100)

def check():
    s1 = t1.get()
    s2 = t2.get()

    if  s1=="" and s2=="":
            messagebox.showerror("Error","All Field Required")
    
    elif (s1=="a" and s2=="a"):
        ope()
        
    else:
        messagebox.showerror("Error","Incorrect username or password")



top.resizable(0, 0)
top.mainloop()
