# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Data-Types/problem/test-if-tuple-is-distinct

#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"
print(len(set(arr)) == len(arr))

# set(arr) removes dups bcos set is only designed to store unique elements
# len set arr gives count of unique elements
# and if that is equal to length of arr, then all elements = distinct

########### Write your code above ###############