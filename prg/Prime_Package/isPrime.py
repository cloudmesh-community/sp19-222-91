
from flask import jsonify
#from markdown import markdown

def checkPrime(n):
    if(n == 0 or n == 1):
        #print(markdown('%d is neither prime nor composite.' % n))
        outstr = str(n) + ' is neither prime nor composite.'
        #return
    elif(n < 0):
        #print(markdown('%d cannot be prime.' % n))
        outstr = str(n) + ' cannot be prime.'
        #return
    else:
        for i in range(2, n):
            if(n % i == 0):
                #print(markdown('%d is not prime because %d / %d = %d' % (n, n, i, n/i)))
                outstr = str(n) + ' is not prime because ' + str(n) + ' / ' + str(i) + ' = ' + str(n/i);
                #return
                break
    #print(markdown('%d is prime.' % n))
    return(jsonify(outstr))

