from tkinter import *
from tkinter import messagebox
root=Tk()

root.eval('tk::PlaceWindow . center')
l1=Label(text="A")
l1.grid(row=0,column=0)
e1=Entry()
e1.grid(row=0,column=1)
e1.focus()

l2=Label(text="B")
l2.grid(row=1,column=0)
e2=Entry()
e2.grid(row=1,column=1)

l3=Label(text="C")
l3.grid(row=2,column=0)
e3=Entry()
e3.grid(row=2,column=1)

def mysum():
 e3.delete(0,END)
 a=int(e1.get())
 b=int(e2.get())
 c=a+b
 e3.insert(0,c)

def mysub():
 e3.delete(0,END)
 a=int(e1.get())
 b=int(e2.get())
 c=a-b
 e3.insert(0,c)

def mymul():
 e3.delete(0,END)
 a=int(e1.get())
 b=int(e2.get())
 c=a*b
 e3.insert(0,c)

def mydiv():
 try:
   e3.delete(0,END)
   a=int(e1.get())
   b=int(e2.get())
   c=a/b
   e3.insert(0,c)
 except:
  messagebox.showinfo("Error","Not Possible To Divide A number with zero")
  e2.delete(0,END)
  e2.focus()

def myfdiv():
 try:
   e3.delete(0,END)
   a=int(e1.get())
   b=int(e2.get())
   c=a//b
   e3.insert(0,c)
 except:
  messagebox.showinfo("Error","Not Possible To Divide A number with zero")
  e2.delete(0,END)
  e2.focus()

def mymod():
 e3.delete(0,END)
 a=int(e1.get())
 b=int(e2.get())
 c=a%b
 e3.insert(0,c)

def myexp():
 e3.delete(0,END)
 a=int(e1.get())
 b=int(e2.get())
 c=a**b
 e3.insert(0,c)

def cf():
 e1.delete(0,'end')
 e2.delete(0,'end')
 e3.delete(0,'end')
 e1.focus()
b1=Button(text="+",width=10, command=mysum)
b1.grid(row=3,column=0)

b2=Button(text="-",width=10, command=mysub)
b2.grid(row=3,column=1)

b3=Button(text="*",width=10, command=mymul)
b3.grid(row=3,column=2)



b4=Button(text="/",width=10, command=mydiv)
b4.grid(row=4,column=0)

b5=Button(text="//",width=10, command=myfdiv)
b5.grid(row=4,column=1)

b6=Button(text="%",width=10, command=mymod)
b6.grid(row=4,column=2)


b7=Button(text="**",width=10, command=myexp)
b7.grid(row=5,column=0)

b8=Button(text="<-",width=10, command=cf)
b8.grid(row=5,column=1)

b9=Button(text="X",width=10, command=quit)
b9.grid(row=5,column=2)

mainloop()




