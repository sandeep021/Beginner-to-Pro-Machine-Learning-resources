from tkinter import *
from tkinter import messagebox


#LISTBOX
"""scr=Tk()
l=Listbox(scr,bg="white",font=("times",20,'bold'))   #to generate vertical list
l.pack()
l.insert(0,'A')
l.insert(1,'B')
l.insert(2,'C')
l.insert(3,'D')
l.insert(4,'E')
#l.curselection()
l.config(selectmode='multipe')
#print(l.get(l.curselection()))
l.delete(0)    #to delete 0 index element
l.delete(0,END)  #to delete all"""


#MENUBUTTON
"""scr=Tk()
m=Menubutton(scr,text='file',font=('times',20,'bold'),bg='blue')
m.pack()
fm=Menu(m,tearoff=0)
m.config(menu=fm)        #Not Working
fm.add_command(label='open')"""

#NEW SCREEN
"""
scr=Tk()
s=Scale(scr,from_=1, to= 10)
s.pack()
s.config(tickinterval=1)
s.config(sliderlength=5)
s.config(orient='horiz')    #slider horizontal krne ke liye
s.config(resolution=0.5)    #slider kitna move kre
s.set(2)                    #ab 2 se start hoga
"""

#OPTION MENU
"""scr=Tk()
v=StringVar()
o=OptionMenu(scr,v,*'abcd')
o.pack()
v.set('kiiinonio')
      """

"""scr=Tk()
v=IntVar()
o=OptionMenu(scr,v,1,2,3,4)
o.pack()
v.set(1)"""





#NEW LOADING BAR
"""from tkinter.ttk import Progressbar
scr=Tk()
v=IntVar()
p=Progressbar(scr,length=200,mode='determinate',variable=v)  #determinate matlab total kitna kam hua
p.pack()
v.set(40)
p.config(mode='indeterminate')   #indeterminate matlab kya kam ho rha h
v.set(70) 
"""
#NEW

"""scr=Tk()                     #pheli screen Tk aur dusari screen Toplevel ,Toplevel scr ki subscreen hogi connected
def fun():
    new=Toplevel(scr)
    msg = Message(new, text="about_message")
    msg.pack()
    l=Label(new,text='new screen',font=('times',20,'bold'))
    l.pack()
b=Button(scr,text='click',command=fun)
b.pack()"""

#NEW

"""from tkinter import messagebox
scr=Tk()
scr.option_add('*font', 'Helvetica -12')
def fun():
    messagebox.showinfo('python','welcome to sunday')
    
b=Button(scr,text='click',command=fun)
b.pack()"""



"""from tkinter import messagebox
scr=Tk()
def fun():
    messagebox.askyesnocancel('python','welcome to sunday')
b=Button(scr,text='click',command=fun)
b.pack()"""



#NEW
"""scr=Tk()
f=Frame(scr,bg="blue",width=200,height=800)
f.grid(row=0,column=0)
f1=Frame(scr,bg="yellow",width=200,height=800)
f1.grid(row=0,column=1)
f2=Frame(scr,bg="green",width=200,height=800)
f2.grid(row=0,column=2)




b=Button(f,text='click')
b.place(x=100,y=150)
b1=Button(f1,text='click1')
b1.place(x=100,y=150)"""



#NEW


"""scr=Tk()
def fun(a):
    print(a)

scr.bind('<Button-1>',fun)
scr.bind('<Button-1>',fun)
scr.bind('<Button-1>',fun)"""

#NEW
"""scr=Tk()
m=Menu(scr)
m.add_command(label='refresh')
m.add_command(label='copy')
m.add_command(label='paste')
m.add_command(label='cut')
m.add_command(label='view')

def fun(a):
    if a.num==3:
        m.post(x=a.x,y=a.y)         #jha click hoga wha post kr dega menun(m) ko
    if a.num==1:
        print('left clickn at',a.x,a.y)
scr.bind("<Button-1>",fun)
scr.bind("<Button-3>",fun)"""


#NEW (uTUBE)

#scr.geometry("400x400")

"""def fun1():
    ans=messagebox.askquestion("exit","Do you really want to exit?")
    if ans=="yes":
         scr.quit()
scr=Tk()
b=Button(scr,text="quit",command=fun1)
b.pack()
scr.mainloop()"""


#new SCREEN COMBOBOX
"""from tkinter.ttk import Combobox
scr=Tk()
v=["12","swsws","dqwdqwdw"]
co=Combobox(scr,values=v,height=2)  #height matlab kitna show krna h ek abr open krne pe
co.pack()
    """


"""from tkinter.font import Font
def print_me():
    #result=text.get(1.0,END)
    selected_result=text.selection_get()
    pos=text.search(selected_result,1.0,stopindex=END)
    #print(result)
    print(selected_result)
    print(pos)
def clear_me():
    text.delete(1.0,END)"""




"""scr=Tk()
font=Font(family="Times New Roman" ,size=16,weight='bold',slant='italic',underline=1,overstrike=1)
label=Label(scr,text='hello python',font=font)
label.pack()
text=Text(scr,width=20,height=10,wrap ='word',padx=10,pady=10,bd=5,selectbackground='blue',font=font)
text.pack()    

b=Button(scr,text='print me',command=print_me).pack()
b=Button(scr,text='clear me',command=clear_me).pack()"""



from tkinter import simpledialog
"""scr=Tk()
def get_me():
    s=simpledialog.askstring("input string",'enter your name')
    print(s)
    

#s=Scale(scr, from = 0, to = 100,orient=HORIZONTAL,length=200,weidth=10,sliderlength=50).pack()


b=Button(scr,text='popup',command=get_me).pack()"""

from tkinter import colorchooser

def clr(event=""):
    c=colorchooser.askcolor(title='select color')
    scr.config(bg=c[1])


scr=Tk()
scr.bind("<Control-c>",clr)

b=Button(scr,text="change color",command=clr).pack()











