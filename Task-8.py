
# Example of Help function in python:
print(help("str"))
print(help("math"))
print(help("functools"))

# Example of Python |import() function:
a =13.55678
from math import *
print(trunc(a))
"""
# Example of python| range () does not return an iterator:
example = range(0,8) #  it gives the list from 1 to,7
print(example)

print(next(example)) #It will generate error"""
# Example of Coroutine in python:
def searcher():
    import time
    #it takes 4 sec to consuming task
    time.sleep(4)
    letters = "here is 7 letters which conatin larger data"
    while True:
        words = (yield)
        if words in letters:
            print("The word in letters")
        else:
            print("The word is not found in the letters")

search = searcher()
next(search)
search.send("larger")
input("press any key")
search.send("contain data")

search.close()

# Example of Python bit function on int:
# int.bit_length():
num = 9
print(num.bit_length())

num2 = 7
print(num2.bit_length())

# int.to_bytes(length, byteorder, *, signed=False):
k = 1024
print(k.to_bytes(2,byteorder = 'big'))

# int.from_bytes(bytes, byteorder, *, signed=False):
print(int.from_bytes(b'\x00\x11',byteorder = 'little'))

# Example of User defined Exception:
class eligible_age(Exception):
    "Raised when the input value is less then 18"
    pass
age = 18
try:
    get = int(input("Enter your age: "))
    if get<age:
        raise eligible_age
    else:
        print("You are eligible for casting vote")

except:
    print("invalid age")

# Example of Built-in Exception:
# Built-in Exception--->SyntaxError
try:
  #  if True       #it gives syntax error
        print("hi")
except SyntaxError:
    print("SyntaxError is occured")

# Example of Clean up action:
def div(a,b):
    try:
        result = a // b
    except ZeroDivisionError:
        print('sorry! you are dividing by zero')
    else:
        print("yahoo! you'r answer is: ",result)
    finally:
        print("clean up action is performed")


# Example of try and ecept in python:
a = input("please enter the number")
print(f"multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except:
    print("invalid input!")


print("Code of table is run")
# Example of File handling (read,write,update):
#read():
f = open("hello",mode='r') # Open a file for reading
data=f.read(5)
print(data)
f.close()

#write():
f = open("hello",mode='w') # Open a file for writing
data=f.write()
print(data)
f.close()

#update files:
f = open("hello",mode='a') # Open a file for appending
data=f.write()
print(data)
f.close()
