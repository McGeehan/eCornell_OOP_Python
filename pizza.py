# Define a class called 'Pizza'
class Pizza:
    # Constructor method to initialize the object's attributes
    def __init__(self, size, crust, toppings):
        self.size = size      # Size of the pizza (e.g. 'small', 'medium', 'large')
        self.crust = crust    # Type of crust (e.g. 'thin', 'regular', 'deep dish')
        self.toppings = toppings  # List of toppings (e.g. ['pepperoni', 'mushrooms', 'olives'])

    # Method to calculate the pizza's price based on its size and toppings
    def calculate_price(self):
        # Base price for each size
        size_prices = {'small': 10, 'medium': 15, 'large': 20}
        # Price for each topping
        topping_price = 2

        # Calculate the total price based on the size and toppings
        total_price = size_prices[self.size] + (len(self.toppings) * topping_price)
        return total_price

    # Method to display the pizza's information
    def display_info(self):
        print(f'Size: {self.size}, Crust: {self.crust}, Toppings: {", ".join(self.toppings)}')


# Create objects of the 'Pizza' class
pizza1 = Pizza('medium', 'regular', ['pepperoni', 'mushrooms'])  # Create a pizza object with size 'medium', crust 'regular', and toppings ['pepperoni', 'mushrooms']
pizza2 = Pizza('large', 'deep dish', ['olives', 'onions', 'green peppers'])  # Create a pizza object with size 'large', crust 'deep dish', and toppings ['olives', 'onions', 'green peppers']

# Call the 'display_info' method on the objects to display their information
pizza1.display_info()  # Output: Size: medium, Crust: regular, Toppings: pepperoni, mushrooms
pizza2.display_info()  # Output: Size: large, Crust: deep dish, Toppings: olives, onions, green peppers

# Call the 'calculate_price' method on the objects to calculate and display the price of each pizza
print(f'Price of pizza 1: ${pizza1.calculate_price()}')  # Output: Price of pizza 1: $19
print(f'Price of pizza 2: ${pizza2.calculate_price()}')  # Output: Price of pizza 2: $26
