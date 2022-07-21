f = open("file3.txt","a")

status = True
while True:
    name = input("Enter student name : ")
    f.write("\n "+name)
    choice = input("do you want to add more student press y for yes or press n for no : ")
    if choice == 'y':
        status = True
    else:
        status = False
        
f.close()