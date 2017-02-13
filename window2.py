from Tkinter import *
import tkMessageBox

def Mostrar():
    texto=Txinfo.get()
    tkMessageBox.showinfo('Titulo','Mensaje a mostrar: '+ texto)

if __name__ == '__main__':
    window2=Tk()
    window2.title("Ventana con mensaje")

    etq1=Label(window2,text='Ejemplo de texto')
    Txinfo=Entry(window2)
    btn=Button(window2,text='mensaje',command=Mostrar)

    etq1.pack()
    Txinfo.pack()
    btn.pack()
    window2.mainloop()
