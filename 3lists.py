l=[]
l1=[]
l2=[]
names = []

def menu():
    print("""MENU
    1 even-odd
    2 merge and sort
    3 update and delete
    4 max and min
    5 add name in list
    6 exit""")
    return int(input("Enter your choice: "))

def evenodd():
    for i in l:
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)

def merge():
    l3 = l1+l2
    l3.sort()
    return l3

def maxmin():
    mini = min(l)
    maxi = max(l)
    return mini, maxi

def name():
    n = int(input("Enter number of elements:"))
    for i in range(n):
        t = input("Enter name: ")
        names.append(t)
    for i in names:
        if i == "python":
            print("python is there in the list")
            break
    else:
        print("python isn't in the list")

def new():
    x = int(input("Enter name to replace first one: "))
    l[0]=x
    print(l)
    l.remove(l[len(l)//2])
    print("After removing middle element: ", l)

n = int(input("Enter no. of. elements for list: "))
for i in range(0, n):
    ele = int(input())

    l.append(ele)

c=0
while(c<=6):
    c = menu()
    if c==1:
        evenodd()
        print("even: ", l1)
        print("odd", l2)
    elif c==2:
        print("Merged and Sorted: ", merge())
    elif c==3:
        new()
    elif c==4:
        print("min and max is: ", maxmin())
    elif c==5:
        name()
    else:
        break


