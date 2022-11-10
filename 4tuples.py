t=()
l=[]

from pprint import pprint

def menu():
    print("""MENU
    1 create and display
    2 display details of student 'Python'
    3 sort the nested tuple
    4 Exit""")

    return int(input("Enter a  choice: "))

def read():
    global t
    global n
    n = int(input("Enter the number of students: "))
    for i in range(0,n):
        print("Enter the details of ", i+1, " student")
        name = input("Enter name: ")
        roll_no = input("Enter roll no.: ")
        print("Enter marks of 3 subjects: ")
        marks = [int(x) for x in input().split()]
        t1 = (roll_no, name, marks)
        l.append(t1)
    t = tuple(l)
    print("Display student  individually: ")
    for i in range(0,n):
        print("Roll No.: ", t[i][0])
        print("Name: ", t[i][1])
        print("Marks: ", t[i][2])
    return n

def find(n):
    flag = 0
    for x in t:
        if x[1] == "python":
            print("'Python' present")
            pprint(x)
            flag = 1
            break
        elif flag == 0:
            print("Not found")

def sort():
    sortedt = sorted(t, key = lambda x:x[1])
    print("The sorted tuple is: ")
    pprint(sortedt)

c = 0
while c<=4:
    c = menu()
    if c==1:
        read()
    elif c==2:
        find(n)
    elif c==3:
        sort()
    else:
        break