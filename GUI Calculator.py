from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("200x240")
lb = Label(root,text="Calculator",font=("Arial",14,"bold"))
lb.place(x=50,y=0)
et = Entry(root,width=50)
et.place(x=0,y=50)
def on_click1():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '%')
def on_click2():
    et.delete(0,END)
def on_click3():
    current = et.get()
    et.delete(len(current)-1,END)
def on_click4():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '7')
def on_click5():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '8')
def on_click6():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '9')
def on_click7():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '4')
def on_click8():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '5')
def on_click9():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '6')
def on_click10():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '1')
def on_click11():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '2')
def on_click12():
    current_text = et.get()
    et.delete(0, END) 
    et.insert(0, current_text + '3')
def on_click13():
    current_text = et.get()
    if et.get().endswith("/") or et.get().endswith("+") or et.get().endswith("-") or et.get().endswith("*"):
        et.delete(len(current_text)-1,END)
        et.insert(len(current_text),"/")
    else:
        et.delete(0, END) 
        et.insert(0, current_text + '/')
def on_click14():
    current_text = et.get()
    if et.get().endswith("/") or et.get().endswith("+") or et.get().endswith("-") or et.get().endswith("*"):
        et.delete(len(current_text)-1,END)
        et.insert(len(current_text),"*")
    else:
        et.delete(0, END) 
        et.insert(0, current_text + '*')
def on_click15():
    current_text = et.get()
    if et.get().endswith("/") or et.get().endswith("+") or et.get().endswith("-") or et.get().endswith("*"):
        et.delete(len(current_text)-1,END)
        et.insert(len(current_text),"-")
    else:
        et.delete(0, END) 
        et.insert(0, current_text + '-')
def on_click16():
    current_text = et.get()
    if et.get().endswith("/") or et.get().endswith("+") or et.get().endswith("-") or et.get().endswith("*"):
        et.delete(len(current_text)-1,END)
        et.insert(len(current_text),"+")
    else:
        et.delete(0, END) 
        et.insert(0, current_text + '+')
def on_click17():
    ct = et.get()
    et.delete(0,len(ct))
    et.insert(0,eval(ct))
bt1 = Button(root,text="%",command=on_click1,width=4,height=2)
bt1.place(x=0,y=80)
bt2 = Button(root,text="C",command=on_click2,width=4,height=2)
bt2.place(x=30,y=80)
bt3 = Button(root,text="<-",command=on_click3,width=4,height=2)
bt3.place(x=65,y=80)
bt4 = Button(root,text="7",command=on_click4,width=4,height=2)
bt4.place(x=0,y=120)
bt4 = Button(root,text="8",command=on_click5,width=4,height=2)
bt4.place(x=30,y=120)
bt4 = Button(root,text="9",command=on_click6,width=4,height=2)
bt4.place(x=65,y=120)
bt4 = Button(root,text="4",command=on_click7,width=4,height=2)
bt4.place(x=0,y=160)
bt4 = Button(root,text="5",command=on_click8,width=4,height=2)
bt4.place(x=30,y=160)
bt4 = Button(root,text="6",command=on_click9,width=4,height=2)
bt4.place(x=65,y=160)
bt4 = Button(root,text="1",command=on_click10,width=4,height=2)
bt4.place(x=0,y=200)
bt4 = Button(root,text="2",command=on_click11,width=4,height=2)
bt4.place(x=30,y=200)
bt4 = Button(root,text="3",command=on_click12,width=4,height=2)
bt4.place(x=65,y=200)
bt4 = Button(root,text="/",command=on_click13,width=4,height=2)
bt4.place(x=101,y=80)
bt4 = Button(root,text="X",command=on_click14,width=4,height=2)
bt4.place(x=101,y=120)
bt4 = Button(root,text="-",command=on_click15,width=4,height=2)
bt4.place(x=101,y=160)
bt4 = Button(root,text="+",command=on_click16,width=4,height=2)
bt4.place(x=101,y=200)
bt4 = Button(root,text="=",command=on_click17,width=7,height=10,bg="light blue")
bt4.place(x=138,y=80)
root.mainloop()