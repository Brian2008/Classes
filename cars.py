class Car(object):
    def __init__(self,model ,color ,company ,speedlimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedlimit

    def start(self): 
        print("starting")
    def stop(self):
        print("stoping")
    def accelerate(self):
        print("accelterating")

car1 = Car("k1", "blue", "honda", "100")
print(car1.color)
car1.start()
car1.accelerate()
car1.stop()
