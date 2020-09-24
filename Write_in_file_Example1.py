#Example1:use context manager using class
class OpenFile():

#sets attributes
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

#setup file accessibility  as per provided information
#file must be returned in order to makeit writable, otherwise write() will throw an "AttributeError: 'NoneType' object has no attribute 'write'" error

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


#file name pass as an argument might or might not be already available in the dictionary, in such case it will either create a new on or wrote above old one
with OpenFile('E:\\answer.txt', 'w') as f:
    print('Enter Input: ')

    #write command will only accept one parameter, input() will input strings sequence from command line and write it in file as is it
    f.write(input())

#it will show whether the file is closed or now i.e. status of the file
#it must be written outside the function in order to work
print(f.closed)

'''program flow:
1. OpenFile('E:\\answer.txt', 'w'): it will first set the parameter using constructor.
2. with statement will run the code within __enter__ method, which will open file and return it to the 'with' statement.
3. f is a file object that will accept the file inside the context manager.
4. f.write(input()) will perform the operation
5. as the with block ends i.e. context manager reach its end line, control will return to __exit__ method which is responsible for closing the file
6. print(f.closed) will print the file's status in boolean
'''


