user_name = input("Enter user name: ")

if(len(user_name) < 10):
    print(f"It contains less than 10 characters around {len(user_name)}")

else:
    print(f"It contains more than 10 characters around {len(user_name)}")