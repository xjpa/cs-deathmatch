# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Data-Types/problem/implement-dictionary-in-python--141631

#User function Template for python3

# insert into dictionary and print "Inserted"
def insert_dict(key, value, dict):
    #code here
    dict[key] = value
    print("Inserted")
    

# deleting from dictionary and print "Deleted" if key present else "-1"
def del_dict(key, dict):
    #code here
    if key in dict:
        del dict[key]
        print("Deleted")
    else:
        print("-1")
    

# print marks of student whos name is key if student name is present in Dict else "-1"
def print_dict(key, dict):
    
    # Your code here
    if key in dict:
        print("Marks of " + key + " is " + str(dict[key]))
    else:
        print("-1")
    