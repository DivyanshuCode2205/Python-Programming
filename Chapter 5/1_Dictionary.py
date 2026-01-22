# creating dictionary as usual

D = {} # creates empty dictionary

dict_1 = {"Car" : "BMW", "Bike" : "Royal Enfield", "Rating" : 10, "Devices" : "Custom OS"
        , "email" : "divyanshuxd3@gmail.com"}

print(f"Dictionary dict_1 : {dict_1}")
print(f"Length of first dictionary, {len(dict_1)}")

# creating dictionary using dict() constructor

dict_2 = dict(a = 'Ronaldo', b = 'Lionel Messi', c = 'Sunil Chhetri', d = 'Mbbape')
print(f"Dictionary dict_2 : {dict_2}")
print(f"Length of second dictionary, {len(dict_2)}")

# accessing values from dictionary by using keys

dict_3 = {1 : "Ronaldo", 2: "Lionel Messi", 3: "Sunil Chhetri", 4 : "Mbbape"}

print(f"GOAT footballer {dict_3[1]}")
print(f"GOAT footballer in India {dict_3[3]}")

print(f"Email {dict_1['email']}")

# adding and updating the dictionary

dict_1["Age"] = 20 # adds new key-value pair to dict_1 or dict_1.update({'Age':20})
dict_3[5] = "Franz Beckenbauer" # adds new key-value pair to dict_3
dict_1["Devices"] = "Android" # updates key 'Devices' in dict_1

print(f"Age: {dict_1.get("Age")}") # using get() to access values at specified key in a dictionary
print(f"Operating system: {dict_1.get("Devices")}")
