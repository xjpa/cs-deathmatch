# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Operators/problem/bitwise-operators-1597314674

def operators(a, b, c):
    #Do a^a below
    d= a^a
    #Do c^b below
    e= c^b
    #Do a&b below
    f= a&b
    #Do c|(a^a) below
    g= c|(a^a)
    #Do ~e below
    e= ~e

    #The line below prints the output. Don't change it!
    print(d,e,f,g)