def greetings():
    print("Good morning, welcome to python.")

    print(__name__)

if __name__ == "__main__":
    '''
    If the code is executed from the file where it is written then __name__ = '__main__',
    but when the file(i.e. module.py) is imported as module to another file(i.e. main.py) then
    __name__ = name of the imported file

    Note: When we import a file into another file then some of the functions of imported file might get executed
    in the file, it is imported to. That is why this check is important.
    '''
    greetings()
