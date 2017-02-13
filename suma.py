from Tkinter import *
import tkMessageBox as tmsg

def Sumando():
    texto1=txtnum1.get()
    texto2=txtnum2.get()
    a=int(texto1)
    b=int(texto2)
    res=a+b
    et3=Label(ventana, text='respuesta : '+ str(res))
    et3.grid(row=4,column=2)


    #tmsg.showinfo('Sumando','El resultado es: '+ res)


if __name__ == '__main__':
    ventana=Tk()

    et1=Label(ventana, text='numero 1 : ')
    et1.grid(row=1,column=1)
    txtnum1=Entry(ventana)
    txtnum1.grid(row=1,column=2)
    et2=Label(ventana, text='numero 2 : ')
    et2.grid(row=2,column=1)
    txtnum2=Entry(ventana)
    txtnum2.grid(row=2,column=2)
    btn=Button(ventana,text='Sumar',command=Sumando)
    btn.grid(row=3,column=1)
    et3=Label(ventana, text='respuesta : ')
    et3.grid(row=4,column=2)
    #et1.pack()
    #txtnum1.pack()
    ventana.mainloop()
