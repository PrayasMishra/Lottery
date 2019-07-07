from tkinter import *
w=Tk()
def generate():
    import random
    n=random.sample(range(10),6)
    print(n)
    l1.configure(text=n[0])
    l2.configure(text=n[1])
    l3.configure(text=n[2])
    l4.configure(text=n[3])
    l5.configure(text=n[4])
    l6.configure(text=n[5])
    
def reset():
    l1.configure(text="...")
    l2.configure(text="...")
    l3.configure(text="...")
    l4.configure(text="...")
    l5.configure(text="...")
    l6.configure(text="...")
    
bLuck=Button(w,command=generate,text="Get your lucky number..",font=("Algerian",18,"bold"))
bReset=Button(w,command=reset,text="RESET",font=("Algerian",18,"bold"))
l1=Label(w,text="...",width=2,font=("Algerian",18,"bold"),relief="solid")
l2=Label(w,text="...",width=2,font=("Algerian",18,"bold"),relief="solid")
l3=Label(w,text="...",width=2,font=("Algerian",18,"bold"),relief="solid")
l4=Label(w,text="...",width=2,font=("Algerian",18,"bold"),relief="solid")
l5=Label(w,text="...",width=2,font=("Algerian",18,"bold"),relief="solid")
l6=Label(w,text="...",width=2,font=("Algerian",18,"bold"),relief="solid")

bLuck.grid(row=2,column=2,columnspan=4)
bReset.grid(row=2,column=6,columnspan=4)
l1.grid(row=1,column=2)
l2.grid(row=1,column=3)
l3.grid(row=1,column=4)
l4.grid(row=1,column=5)
l5.grid(row=1,column=6)
l6.grid(row=1,column=7)
w.mainloop()
# goto F:/python/lottery.py 
