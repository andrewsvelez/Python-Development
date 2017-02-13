#programa  muestra
#prmuestra.py

def Enumerar(n):
    for i in range(1,n,2):
        print i

def Nueva_lista(n):
    l=[]
    for i in range(n):
        val=raw_input('digite valor: ')
        l.append(val)
    return l



if __name__ == '__main__':
    s_n=int(raw_input('digite numero:  '))
    print s_n, 'tipo de dato: ' , type(s_n)
    i_n=int(s_n)
    print i_n, 'tipo de dato: ' , type(i_n)
    a=3
    b=2.5
    c=a+b
    print 'resultado: ', c , type(c)
    ls=Nueva_lista(3)
    print ls
    Enumerar(5)
