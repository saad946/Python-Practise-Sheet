import random


class Train:
    country = "Pakistan"

    def __init__(self, train_number):
        self.train_number = train_number

    def book_ticket(self, from_station, to_station):
        print(f"Booked a ticket for {self.train_number} train from {from_station} to {to_station}.")

    def cancel_ticket(self, from_station, to_station):
        print(f"Cancelled ticket for {self.train_number} train from {from_station} to {to_station}.")  # Method to cancel a ticket for the train
        pass # Method to cancel a ticket for the train
    def getfare(self, from_station, to_station):
        print(f"Fare for train{self.train_number} from {from_station} to {to_station} is {random.randint(222, 5555)}.") 
        pass # Method to get the fare for the train


t = Train("T-1234")
t.book_ticket("Islamabad", "Karachi")
t.getfare("Islamabad", "Karachi")




        