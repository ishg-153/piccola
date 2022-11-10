import os

def menu():
    print("\n///MENU///")
    print("1. To read content of one file and write it to another file")
    print("2. To append data at the end of existing file")
    print("3. To count number of lines, words and characters in a file")
    print("4. To display files in current directory")
    print("5. Exit")
    return(int(input("\nEnter your choice: ")))

c=0
while c!=5:
    c = menu()
    if c==1:
        fname1 = input("\nEnter the file name of first file: ")
        fname2 = input("\nEnter the file name of second file: ")
        f1 = open(fname1+".txt", "r")
        f2 = open(fname2+".txt", "w+")
        s = f1.read()
        f2.write(s)
        f1.close()
        f2.seek(0,0)
        s = f2.read()
        print("\nThe contents of second file are:-\n")
        print(s)
        f2.close()
    elif c==2:
        fname = input("\nEnter the file name: ")
        f = open(fname+".txt", "a+")
        s = input("\nEnter the string to append:\n")
        f.write(s)
        f.seek(0,0)
        s = f.read()
        print("\nThe contents of the updated file are:-\n")
        print(s)
        f.close()
    elif c==3:
        c=l=w=0
        fname = input("\nEnter the file name: ")
        f = open(fname+".txt", "r")
        for x in f:
            words = x.split()
            l+=1
            w+=len(words)
            c+=len(x)
        print("\nNo. of lines = ", l)
        print("\nNo. of words = ", w)
        print("\nNo. of characters = ", c)
        f.close()
    elif c==4:
        files = os.listdir('.')
        print("\nThe files in current directory are:-\n")
        for i in files:
            print(i)
    elif c!=5:
        print("\nIncorrect choice")