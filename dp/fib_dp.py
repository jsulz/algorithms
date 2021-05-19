def fib():
    fibs = 10
    fib_tab = []
    fib_tab.append( 0 )
    fib_tab.append( 1 )
    for i in range( 2, fibs + 1 ):
        curr = fib_tab[i - 1] + fib_tab[ i - 2]
        print( curr )
        fib_tab.append( curr ) 

    print( fib_tab )

if __name__ == '__main__':
    fib()