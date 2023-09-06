# Task-8

## Help function in python:
The Python help function is used to display the documentation of modules, functions, classes, keywords, etc.

syntax :help([object])
## Python |import() function:
We use import statement to import modules and thier contents.

It helps to import modules in runtime also.
## python| range () does not return an iterator:
Python range() function generates a list of numbers.

it is used in for loops to iterate the object present in list but range() it self is not the iterator.

Still if we want to iterate range with keyword next() it gives error.
## Coroutine in python:
In Python, coroutines are similar to generators but with few extra methods and slight changes in how we use yield statements. Generators produce data for iteration while coroutines can also consume data.
## Python bit function on int(bit_length,to_bytes and from_bytes):
The least significant bit is on the far right,and the most significant bit is far left.
### 1. int.bit_length():
Returns the number of bits required to represent an integer in binary, excluding the sign and leading zeros.
### 2. int.to_bytes:
Return an array of bytes representing an integer.
### 3. int.from_bytes:
Returns the integer represented by the given array of bytes.
## Exception handling:
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.. Exception handling deals with these events to avoid the program or system crashing.
## User defined Exception:
User-defined exceptions are also known as custom exceptions.

A programmer can create his own exception is known as user defined exception or custom Exception.
raise statement is used to raise the user defined exception.
## Built-in Exception:
Python has a number of built-in exceptions, such as the well-known errors SyntaxError, NameError, and TypeError. These Python Exceptions are thrown by standard library routines or by the interpreter itself.
## Clean up action:
Clean-up actions are typically used to release resources, close files, or perform other necessary tasks that should occur at the end of a block of code. Python provides the try, except, else, finally blocks to handle clean-up actions effectively.

“finally” to perform clean up actions.
## Nzec error:
NZEC (non zero exit code) as the name suggests occurs when your code is failed to return 0. When a code returns 0 it means it is successfully executed otherwise it will return some other number depending on the type of error.
## try and ecept in python:
Try and Except statement is used to handle these errors within our code in Python.

Try block check the errors if thier is not error it will execute.

Except block is run only when the error is detect in Try block.
## File handling (read,write,update):
Python provides several built-in functions and methods for these (read,write,update)operations.

#### read():
This method is used to read data/content from a file.and return string in text mode.It returns bytes in binary mode.

Syntax:
     file_object.read(size)
here size is optional argument.in binary mode you dont need to give size argument but in string you need it.
#### Writing to Files:
To write data to a file, you can open a file in write ('w') or append ('a') mode and use the write() method to add content to the file.
#### Updating Files:
If you want to update an existing file without overwriting its content, you can open it in append ('a') mode and use the write() method to add new data to the end of the file.
