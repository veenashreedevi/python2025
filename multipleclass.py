class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model 
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print()  
car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")
car3 = Car("Chevrolet", "Camaro")
car4 = Car("Tesla", "Model 3")
car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()
