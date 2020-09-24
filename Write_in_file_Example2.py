#Example2:only with function and context manager
from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file,mode)
        yield f
    finally:
        f.close()


with open_file('E:\\1.txt', 'w') as f:
    f.write(input())
print(f.closed)

'''program flow:
1. OpenFile('E:\\1.txt', 'w') will pass parameters to function open_file
2. f = open(file,mode) will open file and return it to the 'with' statement.
3. f is a file object that will accept the file inside the context manager.
4. yield f will perform the context manager block
5. as the 'with' block ends i.e. context manager reach its end line, control will return to f.close() method which is responsible for closing the file
6. print(f.closed) will print the file's status in boolean
'''