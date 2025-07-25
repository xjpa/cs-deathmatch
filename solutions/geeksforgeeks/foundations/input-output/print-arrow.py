# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Print-Statement/problem/print-arrow

#User function Template for python3

def utility():
    #The following 4 lines take the inputs. Don't change them!
    a=input()
    b=int(input())
    c=int(input())
    d=int(input())
    
    
    # write your code below to prints the pattern
    print(a*d,">","\n"*(b-1),sep="")
    print(" "*c,a*d,">","\n"*b,sep="",end="")
    print(a*d,">",sep="")
    # write your code above to prints the pattern
    
