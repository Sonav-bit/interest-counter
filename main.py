from tkinter import *
root=Tk()
root.title('Interest')
root.geometry('400x400')
l1=Label(root,text=('Enter the principle'))
l2=Label(root,text=('Enter the time(In year)'))
l3=Label(root,text=('Enter the rate of interest'))
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
def intg():
    pr=int(e1.get())
    y=int(e2.get())
    r=int(e3.get())
    t='The interest is'
    k=pr*y*r/100
    l4=Label(root,text=(t+k))
    l4.grid(row=4,column=1)
b1=Button(root,text='Click me',command=intg)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
b1.grid(row=3,column=1)

root.mainloop()