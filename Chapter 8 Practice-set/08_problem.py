def multiplication_table():
    num = int(input("Enter : "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")

multiplication_table()
