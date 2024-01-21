'''
Created on 13-Jan-2024

@author: leand
'''
from os import name

#List Operations:
#1.Write a program to remove duplicates from a given list.
#def remove_duplicates(input_list):
#    unique_list = list(set(input_list))
#    return unique_listGenerate a list of squares of numbers from 1 to 10.


# Example Usage:
#input_list = [1, 2, 2, 3, 4, 4, 5]
#result = remove_duplicates(input_list)
#print("Original List:", input_list)
#print("List with Duplicates Removed:", result)

#2.Create a function that returns the intersection of two lists.
#def find_intersection(list1, list2):
#    set1 = set(list1)
#    set2 = set(list2)
#    intersection = set1.intersection(set2)
#    return list(intersection)

# Example Usage:
#list1 = [1, 2, 3, 4, 5]
#list2 = [3, 4, 5, 6, 7]
#result = find_intersection(list1, list2)
#print("List 1:", list1)
#print("List 2:", list2)
#print("Intersection:", result)

#3.Generate a list of squares of numbers from 1 to 10.
#squares_list = [x**2 for x in range(1, 10)]

#print("List of Squares:", squares_list)

#4.Create a list of words that have more than 5 characters from a given list of words (you can create your own list of words for given list).
# Example list of words
#word_list = ["bengaluru", "goa", "mysuru", "hassan", "ladak"]

# Create a new list of words with more than 5 characters
#filtered_words = [word for word in word_list if len(word) > 5]

#print("Original Word List:", word_list)
#print("Filtered Word List (more than 5 characters):", filtered_words)

#Dictionary Operations:
#1.Write a program to merge two dictionaries.
#def merge_dicts(dict1, dict2):
#    return {**dict1, **dict2}

# Example Usage:
#dict1 = {'a': 1, 'b': 2}
#dict2 = {'b': 3, 'c': 4}

#result = merge_dicts(dict1, dict2)
#print("Dictionary 1:", dict1)
#print("Dictionary 2:", dict2)
#print("Merged Dictionary:", result)

#2.Create a function to find keys with duplicate values in a dictionary.

#def find_duplicate_value_keys(input_dict):
#    value_set = set()
#    duplicate_keys = set()

#    for key, value in input_dict.items():
#        if value in value_set:
#            duplicate_keys.add(key)
#        else:
#            value_set.add(value)

#    return duplicate_keys

# Example Usage:
#my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4}

#result = find_duplicate_value_keys(my_dict)
#print("Original Dictionary:", my_dict)
#print("Keys with Duplicate Values:", result)

#Dictionary Iteration:
#1. Write a program to iterate through keys and values of a dictionary and perform a specific operation on them.

#def perform_operation_on_dict(dictionary):
#    for key, value in dictionary.items():
        # Perform a specific operation (e.g., print key and square of the value)
#        result = value ** 2
#        print(f"Key: {key}, Value: {value}, Result: {result}")

# Example Usage:
#my_dict = {'a': 2, 'b': 3, 'c': 4, 'd': 5}

#perform_operation_on_dict(my_dict)

#2. Create a function to check if a certain key exists in a dictionary.

#def key_exists(dictionary, key_to_check):
#    return key_to_check in dictionary

# Example Usage:
#my_dict = {'a': 1, 'b': 2, 'c': 3}

#key_to_check1 = 'b'
#key_to_check2 = 'd'

#if key_exists(my_dict, key_to_check1):
#    print(f"The key '{key_to_check1}' exists in the dictionary.")
#else:
#    print(f"The key '{key_to_check1}' does not exist in the dictionary.")

#if key_exists(my_dict, key_to_check2):
#    print(f"The key '{key_to_check2}' exists in the dictionary.")
#else:
#    print(f"The key '{key_to_check2}' does not exist in the dictionary.")
'''
#Tuple Operations:
#1.Write a program to reverse a tuple.

def reverse_tuple(input_tuple):
    reversed_tuple = input_tuple[::-1]
    return reversed_tuple

# Example Usage:
original_tuple = (1, 2, 3, 4, 5)

reversed_tuple = reverse_tuple(original_tuple)

print("Original Tuple:", original_tuple)
print("Reversed Tuple:", reversed_tuple)
'''
'''
#2.Create a function that returns the common elements between two tuples.

def common_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    common_elements_set = set1.intersection(set2)
    return tuple(common_elements_set)

# Example Usage:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

result = common_elements(tuple1, tuple2)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Common Elements:", result)
'''

#Set Operations:
'''
#1.Write a program to perform set operations like union, intersection, and difference between two sets.
def perform_set_operations(set1, set2):
    # Union
    union_result = set1.union(set2)

    # Intersection
    intersection_result = set1.intersection(set2)

    # Difference (elements in set1 but not in set2)
    difference_result1 = set1.difference(set2)

    # Difference (elements in set2 but not in set1)
    difference_result2 = set2.difference(set1)

    return union_result, intersection_result, difference_result1, difference_result2

# Example Usage:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set, intersection_set, difference_set1, difference_set2 = perform_set_operations(set1, set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 - Set1):", difference_set2)
'''
'''
#2.Create a function to check if a set is a subset of another set.
def is_subset(set1, set2):
    return set1.issubset(set2)

# Example Usage:
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

result = is_subset(set1, set2)

print("Set 1:", set1)
print("Set 2:", set2)

if result:
    print("Set 1 is a subset of Set 2.")
else:
    print("Set 1 is not a subset of Set 2.")
'''
#*String Operations using Lists:*
'''
#1.Write a program to count the occurrences of each character in a string.

def count_characters(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

# Example Usage:
input_str = "programming is fun"

result = count_characters(input_str)

print(f"Input String: '{input_str}'")
print("Character Counts:")
for char, count in result.items():
    print(f"'{char}': {count}")
'''
'''
#2.Create a function to reverse words in a given sentence without using built-in methods.
def reverse_words(sentence):
    reversed_sentence = ""
    word = ""
    for char in sentence:
        if char == ' ':
            reversed_sentence = word + ' ' + reversed_sentence
            word = ""
        else:
            word += char
    reversed_sentence = word + ' ' + reversed_sentence  # Adding the last word
    return reversed_sentence

# Example Usage:
input_sentence = "Hello World! Python is awesome."

result = reverse_words(input_sentence)

print("Original Sentence:", input_sentence)
print("Reversed Sentence:", result)
'''
'''
#Functions:

#1.Create a function that takes two numbers as arguments and returns their sum.
def add_numbers(num1, num2):
    return num1 + num2

# Example Usage:
result = add_numbers(5, 7)
print("Sum:", result)

'''
'''
#2.Write a function that takes a string and an optional parameter to specify the number of times the string should be repeated (default should be 1).
def repeat_string(input_string, times=1):
    """Repeats the input string a specified number of times."""
    return input_string * times

# Example usage:
result1 = repeat_string("Hello")
print(result1)  

result2 = repeat_string("Hi", times=3)
print(result2)  
'''
'''
#3.Implement a function that takes a variable number of arguments and returns their sum.
def sum_of_arguments(*args):
    """Returns the sum of the provided arguments."""
    return sum(args)

# Example usage:
result1 = sum_of_arguments(1, 2, 3)
print(result1)

result2 = sum_of_arguments(4, 5, 6, 7)
print(result2)  
'''
'''
#4. Write a recursive function to calculate the factorial of a given number.
def factorial(n):
    """Calculates the factorial of a given number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(4)
print(result)
'''
'''
#5.Create a recursive function to generate the Fibonacci sequence up to a specified limit.
def fibonacci_sequence(limit, sequence=None):
    """Generates the Fibonacci sequence up to a specified limit using recursion."""
    if sequence is None:
        sequence = []

    if not sequence or sequence[-1] + sequence[-2] <= limit:
        if not sequence:
            sequence.extend([0, 1])
        else:
            sequence.append(sequence[-1] + sequence[-2])
        fibonacci_sequence(limit, sequence)

    return sequence

# Example usage:
limit = 50
fibonacci_result = fibonacci_sequence(limit)
print(fibonacci_result)
''''''
#6.Write a function that takes another function as an argument and applies it to a list of numbers.
def apply_function_to_list(func, numbers):
    """Applies the specified function to each element in the list of numbers."""
    return [func(number) for number in numbers]

# Example usage:
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
result = apply_function_to_list(square, numbers)
print(result)
'''
'''
#7. Create a function that returns another function based on the given parameters.
def create_square_function(additional_constant):
    """Returns a function that calculates the square of a number with an additional constant term."""
    def square_with_constant(x):
        return x ** 2 + additional_constant
    return square_with_constant

# Example usage:
square_function_with_5 = create_square_function(5)
result1 = square_function_with_5(3)
print(result1)

square_function_with_10 = create_square_function(10)
result2 = square_function_with_10(3)
print(result2)
'''
'''
#Online Shopping Platform:Design an online shopping platform with classes for products, users, and a shopping cart. Utilize data structures like lists or dictionaries to store products and user information. Implement functionalities like adding items to a cart, calculating the total amount, managing user orders, and applying discounts based on certain conditions. Use control flow statements for user interaction and exception handling for errors during checkout or product selection.
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = {}

    def add_to_cart(self, product, quantity=1):
        if product.product_id in self.cart:
            self.cart[product.product_id]['quantity'] += quantity
        else:
            self.cart[product.product_id] = {'product': product, 'quantity': quantity}

    def calculate_cart_total(self):
        total_amount = 0
        for item in self.cart.values():
            total_amount += item['product'].price * item['quantity']
        return total_amount

    def checkout(self):
        try:
            total_amount = self.calculate_cart_total()
            # Apply discounts based on certain conditions (e.g., order amount, user type, etc.)
            # For simplicity, let's assume a flat 10% discount on orders above Rs5000
            if total_amount > 100:
                total_amount *= 0.9

            # Simulate payment processing
            print(f"Total amount after discount: Rs{total_amount:.2f}")
            print("Payment successful. Order placed!")

            # Clear the cart after successful checkout
            self.cart = {}

        except Exception as e:
            print(f"Error during checkout: {e}")

# Example usage:
# Create products
product1 = Product(1, "Laptop", 45000)
product2 = Product(2, "Headphones", 2500)
product3 = Product(3, "Mouse", 600)

# Create a user
user1 = User(101, "Leander")

# Add items to the cart
user1.add_to_cart(product1, quantity=2)
user1.add_to_cart(product2)
user1.add_to_cart(product3, quantity=3)

# Calculate and print the cart total
cart_total = user1.calculate_cart_total()
print(f"Cart Total: Rs{cart_total:.2f}")

# Checkout
user1.checkout()
'''
class CarClass():
    def __init__(self, name, color):
        self.name=name
        self.color=color
     
    def display_details(self):
        print(f"My car is {self.name} and it is {self.color} color")
        
    def move_forward(self):
        print(f"My {self.name} car is moving forward")
        
car1=CarClass("Swift", "White")
car1.display_details()
print(car1.name)
print(car1.color)

car2=CarClass("Brezza", "Black")
car2.display_details()
print(car2.name)
print(car2.color)
print(type(car1))
print(type(car2))






