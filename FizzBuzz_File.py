import numpy as np

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)

    for i in range(len(objvec)):
        if objvec[i] % 15 == 0:
            objvec[i] = 'fizzbuzz'
        elif objvec[i] % 3 == 0:
            objvec[i] = 'fizz'
        elif objvec[i] % 5 == 0:
            objvec[i] = 'buzz'

    return objvec
