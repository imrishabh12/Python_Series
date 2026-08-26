# Q2. Create a Car class with attributes and methods.

class Car:

    def start(self):
        print(self.brand, "is starting")

    def stop(self):
        print(self.brand, "is stopping")


car = Car()

car.brand = "Toyota"
car.model = "Camry"

print("Brand:", car.brand)
print("Model:", car.model)

car.start()
car.stop()