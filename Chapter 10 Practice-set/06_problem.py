class Train:

    def __init__(slf, name, train_no):
        slf.name = name
        slf.train_no = train_no
        print(f'Thanks for choosing IRCTC {slf.name}')
    
    def book(slf, boarding, destination):
        print(f'Ticket is booked in train number {slf.train_no} from {boarding} to {destination}')

    @staticmethod
    def getStatus():
        from random import randint
        print('Ticket is booked successfully.')
        print(f'Number of seats available: {randint(1, 60)}')
    
    def getFare(slf, boarding, destination):
        from random import randint
        print(f'Fare of ticket in train number {slf.train_no} from {boarding} to {destination} is ₹{randint(2200, 5555)}')
    
t = Train('Divyanshu', 22134)
t.book('Patna', 'Mumbai')
t.getStatus()
t.getFare('Patna', 'Mumbai')
