#INTRODUCTION
"""1. tkinter
   2. wxPython ---used to make gui for old system and windows
   3.jpython  ---use to make gui and then convert it to java
   4.kiwy   
   5.pyQt($200)   ---paid,crack on github but have less functinalities
GEOMETRY USEED TO STICK ARE:
  1.pack
  a.side: TOP,BOTTOM,LEFT,RIGHT
  b.fill:X,Y

  2.grid
  a.row
  b.column


  3.place
    x,y"""

#NEW SCREEN 1
"""from tkinter import *
scr=Tk()
l=Label(scr,text='hello welcom' ,bg='blue',fg='yellow',font=('times',20,"bold"),cursor='man',relief='raised',width=200)
l.pack()
l.config(cursor="plus",width=40)
l.config(text="hello python")
scr.mainloop() """ 

#NEW SCREEN 2
from tkinter import *
"""rt=Tk()
s=StringVar()     #nayi string input ke liye bar bar kr skte h s.set()
l=Label(rt,textvariable=s ,bg='blue',fg='yellow',font=('times',20,"bold"),cursor='man',relief='raised',width=40)
l.pack()
s.set("my name is python i run on anaconda")
s.set("7355150578")
rt.mainloop()"""



#NEW SCREEN 3           check its error
"""scr=Tk()
v=StringVar()
l=Label(scr,textvariable=v,font=("times",20,"italic"),bg='red',fg='black')
l.pack()
v.set("JIJGYGYGUHBHIUGIYGIUHHIHGJ")
scr.mainloop()"""

#NEW SCREEN 4
"""scr=Tk()
l=Label(scr,bitmap='hourglass',bg='blue')
l.pack(side=TOP,fill=X)
l.pack(side=LEFT,fill=Y)
l.pack(fill=BOTH,expand=True)"""


#NEW SCREEN 5
"""img=Photoimage(file="23.jpg")
l=Label(src,image=img)
l.pack()"""


#BUTTON COOKING


#NEW SCREEN 6
"""scr=Tk()
l=Label(scr,font=("times",20,"bold"))
l.pack()
def fun():
    l.config(text="button clicked")
b=Button(scr,activebackground="yellow",activeforeground="white",bd=10,bg='blue',fg='yellow',relief='sunken',state='active',underline='0',text='submit',command=fun)
b.pack()"""


# Chechbutton and button sath me>>
#NEW SCREEN 7
"""scr=Tk()
v=IntVar()       #v=StringVar()     strings ke liye hota h aur!!!!!
l=Label(scr,font=("times",20,"bold"))
l.pack()
def fun():
    if v.get()==10:
        l.config(text='checkbutton checked')
        b.config(state='normal')
    if v.get()==100:
        l.config(text='checkbutton unchecked')
        b.config(state='disable')


c=Checkbutton(scr,text='I AGREE',onvalue=10,offvalue=100,variable=v,command=fun)
c.pack()
b=Button(scr,text='NEXT>',state='disable')
b.pack()
"""

#DOUBLE VAR
#NEW SCREEN 8
"""scr=Tk()
v=DoubleVar()
l=Label(scr,font=("times",20,"bold"))
l.pack()
def fun():
    if v.get()==1.0:
        l.config(text="radiobutton 1 checked")
    if v.get()==2.0:
        l.config(text="radiobutton 2 checked")
    if v.get()==3.0:
        l.config(text="radiobutton 3 checked")
r=Radiobutton(scr,text="radio-1",value=1.0,command=fun)
r.pack()
r1=Radiobutton(scr,text="radio-2",value=2.0,command=fun)
r1.pack()
r2=Radiobutton(scr,text="radio-3",value=3.0,command=fun)
r2.pack()
r.config(variable=v)
r1.config(variable=v)
r2.config(variable=v)"""


#ENTRY
#NEW SCREEN 9

"""scr=Tk()
e=Entry(scr,bg='yellow',font=('times',20,'bold'))
e.pack()
e.get()    #to get what is input working in python prompt
e.delete(0)
e.delete(0,END)
e.insert(0,'hello')
e.insert(END,'python')    #END likhne pe last me ayega
e.config(show='*')            #type kroge kuch dikhega nhi
e.config(show='')         #ab dikhega"""

#NEW SCREEN 10

"""scr=Tk()
v=StringVar()
e=Entry(scr,bg='yellow',font=('times',20,'bold'))
e.pack()
v.trace('w',lambda*args:v.set(v.get()[:2]))       #to limit the input limit
"""

#NEW SCREEN 11
"""scr=Tk()
t=Text(scr,font=('times',20,'italic'))
t.pack()
t.get('1.0',END)   #1.0 hi phela line h , 1.5 pahle line ke pachwa charector to dikhaega"""


#ADJUSTING SIZE OF SCREEN  (by Utube)

#NEW SCREEN 12

"""scr=Tk()
scr.geometry("600x300+120+130")   #600x300 size hai, 120 left se duri and 130 upae se duri
scr.mainloop()"""


#Drop doWn MENU (by Utube)

#NEW SCREEN
"""def do_nothing():
    print("okay")
root=Tk()
main_menu=Menu(root)
root.config(menu=main_menu)

filemenu=Menu(main_menu)
main_menu.add_cascade(label="file",menu=filemenu)
filemenu.add_command(label="new file",command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label="open",command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label="save",command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label="rename",command=do_nothing)


editmenu=Menu(main_menu)
main_menu.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="insert",command=do_nothing)

root.mainloop()"""

#NEW SCREEN
"""scr=Tk()
l=Listbox(scr)
l.pack()
l.insert(0,"A")
l.insert(1,"B")
l.insert(2,"C")
l.insert(3,"D")
l.insert(4,"E")
l.curselection()
#l.get(l.curselection())  error line"""

#NEW SCREEN
"""scr=Tk()
v=StringVar()
l=[1,2,3,4,5,6,7,8,9]   # l=["python","java","ML","DL","Django"]
o=OptionMenu(scr,v,*l)
o.pack()
v.get()
v.set(l[0])
"""

#NEW SCREEN
from PIL import ImageTk,Image     #pahele tkinter import kro fir pillow ,kuki Image nam ka module done me h pahele wala overwrite ho jaata hai


#NEW SCREEN
"""scr=Tk()
c=Canvas(scr,bg="white",width=300,height=300)
c.pack()
c.create_arc((10,10,100,100),start=0,extent=90,outline="blue",fill="yellow")
c.create_arc((10,10,100,100),start=90,extent=270,outline="blue",fill="green")
c.create_line(10,110,100,110,100,200,200,200,fill="green")
c.create_oval((100,10,200,200),fill="blue")
c.create_polygon(10,110,100,110,100,200)
c.create_rectangle((200,10,300,200))
c.create_text(150,150,text="Python",font=("times",20,"italic"),fill="white")
c.create_bitmap(150,240,bitmap="question")
c.pack()"""



#MENU
#NEW SCREEN
from tkinter import filedialog
scr=Tk()
m=Menu(scr)
scr.config(bg="blue")
scr.config(menu=m)
fm=Menu(m,tearoff=False)
m.add_cascade(label="file",menu=fm)
fm.add_command(label="open",command=lambda:print(filedialog.askdirectory()))
fm.add_command(label="open1",command=lambda:print(filedialog.askopenfile()))
fm.add_command(label="open2",command=lambda:print(filedialog.askopenfilename()))
fm.add_separator()
fm.add_command(label="open3",command=lambda:print(filedialog.askopenfilenames()))
fm.add_command(label="save",command=lambda:print(filedialog.asksaveasfile()))
sb=Menu(fm)
sb.add_command(label="project",command=lambda : print("reset project"))
sb.add_command(label="file",command=lambda : print("recent file"))
fm.add_cascade(label="recent",menu=sb)
fm.add_checkbutton(label="check")
fm.add_radiobutton(label="radio1")
fm.add_radiobutton(label="radio2")










