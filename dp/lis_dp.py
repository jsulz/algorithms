import numpy as np

def lis( sequence ):
    length = np.ones( len(sequence))
    for i in range( len(sequence) ):
        length[i] = 1
        for j in range( 0, i ):
            if sequence[j] < sequence[i] and length[i] < length[j] + 1:
                length[i] = length[j] + 1
    print( max(length))
    print( length )
    return max(length)



if __name__ == '__main__':
    lis( [5, 7, 4, -3, 8, 1, 10, 4, 5, 8, 9, 3] )