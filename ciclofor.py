#ciclo for
if __name__ == '__main__':
    '''
    #Arranca desde 0
    for i in range (5):
        print i
    print '-----------'
    #Arranca desde 1 a 5
    for i in range (1,5):
        print i
    print '-----------'
    #Arranca desde 0 y se incrementa de a 3 hasta 10
    for i in range(0,10,3):
        print i
    '''
    #Crear lista -- la lista se comporta como arreglo
    ls=[1,2,4,6,8,9,-1,4]
    print ls
    #mostrar elemento dependiendo la posicion
    print 'elementos: ', ls[0]
    # Desde el principio tome algunos elementos
    print 'algunos: ' , ls[:5]
    # Desde 2 tome elementos hasta el 5
    print 'algunos: ' , ls[2:5]
    print 'algunos: ', ls[5:]
    for elemento in ls:
        print elemento
    print '--------------------'
    ols=[1,2.4,'hola',[2,3,4],True]
    for e in ols:
        print e
    print 'valor lista interna: ', ols [2]
    #sublista
    print 'valor lista interna: ', ols [2][3]
    #adicionar valor a una lista
    ols.append('nuevo')
    print ols
