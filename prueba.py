from Tkinter import *

if __name__ == '__main__':
    window=Tk()
    lab1=Label(window, text="Hola")
    lab2=Label(window,text="otro hola")
    getname=Entry(window)
    bot1=Button(window,text="Aceptar")    
    lab1.pack()
    lab2.pack()
    getname.pack()
    bot1.pack()
    window.mainloop()
