class Train:

    def __init__(self, name, Train_no):
        self.train_no = Train_no
        self.name = name
        print(f'Thanks for using IRCTC {self.name}')

    def book(self, Boarding, Destination):
        print(f'Ticket is booked in train no. {self.train_no} that is Boarding from {Boarding} to {Destination}')

    @staticmethod # no use of object for this funcion
    def getsatus():
        from random import randint
        print('Ticket is successfully confirmed.')
        print(f'Number of seats available: {randint(1, 60)}')

    def getFare(self, Boarding, Destination):
        from random import randint
        print(f'Ticket fare in train no. {self.train_no} from {Boarding} to {Destination} is ₹{randint(222, 5555)}')
            
t = Train('Divyanshu', 15708) # object t is created
t.book('Patna', 'Mumbai')
t.getsatus()
t.getFare('Patna', 'Mumbai')
