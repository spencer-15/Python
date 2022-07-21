import mymodule

menu = """
        press 1 for sum
        press 2 for mul
        press 3 for addition
"""
print(menu)

choice = int(input("Enter your choice: "))
if choice == 1:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    mymodule.sum(n1,n2)
elif choice == 2:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    mymodule.mul(n1,n2)
elif choice == 3:
    print(mymodule.addition(45,23,5,7,2,46))
else:
    print("invalid input")