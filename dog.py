# Define a class called 'Dog'
class Dog:
    # Constructor method to initialize the object's attributes
    def __init__(self, name, breed, age):
        self.name = name  # Name of the dog
        self.breed = breed  # Breed of the dog
        self.age = age  # Age of the dog

    # Method to make the dog bark
    def bark(self):
        print(f'{self.name} says Woof!')

    # Method to display the dog's information
    def display_info(self):
        print(f'Name: {self.name}, Breed: {self.breed}, Age: {self.age}')


# Create objects of the 'Dog' class
dog1 = Dog('Buddy', 'Golden Retriever', 5)  # Create a dog object with name 'Buddy', breed 'Golden Retriever', and age 5
dog2 = Dog('Bella', 'Labrador Retriever', 3)  # Create a dog object with name 'Bella', breed 'Labrador Retriever', and age 3

# Call the 'display_info' method on the objects to display their information
dog1.display_info()  # Output: Name: Buddy, Breed: Golden Retriever, Age: 5
dog2.display_info()  # Output: Name: Bella, Breed: Labrador Retriever, Age: 3

# Call the 'bark' method on the objects to make the dogs bark
dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Bella says Woof!
