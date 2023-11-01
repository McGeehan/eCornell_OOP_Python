# Define a class called 'Car'
class Car:
    # Constructor method to initialize the object's attributes
    def __init__(self, make, model, year):
        self.make = make    # Make of the car (e.g. Toyota, Honda, etc.)
        self.model = model  # Model of the car (e.g. Camry, Civic, etc.)
        self.year = year    # Year of the car (e.g. 2020, 2021, etc.)

    # Method to start the car
    def start(self):
        print(f'The {self.year} {self.make} {self.model} is starting...')

    # Method to stop the car
    def stop(self):
        print(f'The {self.year} {self.make} {self.model} is stopping...')

    # Method to display the car's information
    def display_info(self):
        print(f'{self.year} {self.make} {self.model}')


# Create objects of the 'Car' class
car1 = Car('Toyota', 'Camry', 2020)  # Create a car object with make 'Toyota', model 'Camry', and year 2020
car2 = Car('Honda', 'Civic', 2021)   # Create a car object with make 'Honda', model 'Civic', and year 2021

# Call the 'display_info' method on the objects to display their information
car1.display_info()  # Output: 2020 Toyota Camry
car2.display_info()  # Output: 2021 Honda Civic

# Call the 'start' and 'stop' methods on the objects to start and stop the car
car1.start()  # Output: The 2020 Toyota Camry is starting...
car1.stop()   # Output: The 2020 Toyota Camry is stopping...
car2.start()  # Output: The 2021 Honda Civic is starting...
car2.stop()   # Output: The 2021 Honda Civic is stopping...
