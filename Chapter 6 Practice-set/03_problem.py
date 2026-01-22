P1 = "make a lot of money"
P2 = "buy now"
P3 = "click this"
P4 = "subscribe this"

message = input("Enter your message: ")

if((P1 in message.lower()) or (P2 in message.lower()) or (P3 in message.lower()) or (P4 in message.lower())): # '==' sign can also be used
    print("This is a spam message.")

else:
    print("This is not a spam message.")
    