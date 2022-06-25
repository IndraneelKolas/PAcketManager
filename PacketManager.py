class Car(object):

    def __init__(self, model, color, company, speed, tire, seats):
        
        self.model = model
        self.color = color
        self.company = company
        self.speed = speed
        self.tire = tire
        self.seats = seats
        
    def start(self):
        print("The car has started!")
    def stop(self):
        print("The car has stopped!")
    def isStarting(self):
        print("The car is starting!")
    def isSlowingDown(self):
        print("The car is slowing down!")

carName = Car("C-220", "Red", "Mercedez", 220, "Tire", 6)
print(carName.start())
print(carName.model)
print(carName.company)
print(carName.speed)
print(carName.seats)
print(carName.color)
print(carName.speed)