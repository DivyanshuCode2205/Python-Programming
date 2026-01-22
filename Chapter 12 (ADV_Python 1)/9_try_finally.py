def main():
    try:
        a = int(input('Enter: '))
        print(a)
        return 1

    except Exception as e:
        print(e)
        return 1

    finally:
        print('finally block will be excuted regardless of error.') # its mainly useful in function 
    # even if there is return statment finally block will be executed.
main()
