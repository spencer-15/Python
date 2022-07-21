def sum(num1,num2):
    ans = num1 + num2
    print(ans)

def mul(num1,num2):
    ans = num1 * num2
    print(ans)

def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

def info():
    print("Python is the best language")
