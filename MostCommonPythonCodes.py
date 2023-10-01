# ----------------------------------------------------------------------
# Reading and Writing Files:

# Reading a file
with open('file.txt', 'r') as file:
    content = file.read()

# Writing to a file
with open('file.txt', 'w') as file:
    file.write('New content')

# ----------------------------------------------------------------------
iterable =[]
#for Loop:
for item in iterable:
    # Code to be executed
    pass

# ----------------------------------------------------------------------
condition = True
# if Statement:
if condition:
    # Code to be executed if the condition is true
    pass

# ----------------------------------------------------------------------
# Defining a Function:
def my_function(parameter1, parameter2):
    # Function code
    return result

# ----------------------------------------------------------------------
# Using Lists:
my_list = [1, 2, 3, 4, 5]

# ----------------------------------------------------------------------
#Using Dictionaries:
my_dict = {'key1': 'value1', 'key2': 'value2'}

# ----------------------------------------------------------------------
# while Loop:
while condition:
    # Code to be executed
    pass

# ----------------------------------------------------------------------
#Using Standard Modules:
import math
result = math.sqrt(16)

# ----------------------------------------------------------------------
# List Comprehension:
squares = [x**2 for x in range(10)]

# ----------------------------------------------------------------------
# Exception Handling:
try:
    # Code that may raise an exception
    pass
except Exception as e:
    # Handling the exception
    pass


# ----------------------------------------------------------------------
# Working with Strings:
my_string = "Hello, World!"

# ----------------------------------------------------------------------
# Using Sets:
my_set = {1, 2, 3}

# ----------------------------------------------------------------------
# Using Tuples:
my_tuple = (1, 2, 3)

# ----------------------------------------------------------------------
# Getting User Input:
user_input = input("Enter something: ")

# ----------------------------------------------------------------------
# Converting Data Types:
number = int("42")

# ----------------------------------------------------------------------
# Finding the Length of a List:
length = len(my_list)

# ----------------------------------------------------------------------
# Sorting a List:
sorted_list = sorted(my_list)

# ----------------------------------------------------------------------
# Appending to a List:
my_list.append(6)

# ----------------------------------------------------------------------
# Removing an Item from a List:
my_list.remove(3)

# ----------------------------------------------------------------------
# Checking Membership in a List:
if item in my_list:
    # Code to handle membership
    pass

# ----------------------------------------------------------------------
# Creating a Dictionary:
my_dict = dict(key1='value1', key2='value2')

# ----------------------------------------------------------------------
# Accessing Dictionary Values:
value = my_dict['key1']

# ----------------------------------------------------------------------
# Updating Dictionary Values:
my_dict['key1'] = 'new_value'

# ----------------------------------------------------------------------
# Deleting Dictionary Items:
del my_dict['key1']

# ----------------------------------------------------------------------
# Checking Dictionary Keys:
if 'key1' in my_dict:
    # Code to handle key existence
    pass

# ----------------------------------------------------------------------
# Using enumerate with Lists:
for index, item in enumerate(my_list):
    # Code using index and item
    pass

# ----------------------------------------------------------------------
# Using zip to Combine Lists:
list1,list2 = []
combined = list(zip(list1, list2))

# ----------------------------------------------------------------------
# Creating a Function with Default Arguments:
def greet(name="Guest"):
    # Function code
    pass

# ----------------------------------------------------------------------
# Using the range Function:
for i in range(5):
    # Code that runs 5 times
    pass

# ----------------------------------------------------------------------
# String Formatting with f-strings:
name = "Alice"
greeting = f"Hello, {name}!"


# ----------------------------------------------------------------------
# Using the in Operator with Strings:
if "substring" in my_string:
    # Code to handle substring presence
    pass

# ----------------------------------------------------------------------
# Checking for None:
my_variable = None
if my_variable is None:
    # Code to handle None
    pass


# ----------------------------------------------------------------------
# Creating and Using Classes:
class MyClass:
    def __init__(self):
        # Constructor code
        pass

    def my_method(self):
        # Method code
        pass
    

# ----------------------------------------------------------------------
# Working with Dates and Times:
from datetime import datetime
now = datetime.now()

# ----------------------------------------------------------------------
# Using map to Apply a Function to a List:
doubled = list(map(lambda x: x * 2, my_list))

# ----------------------------------------------------------------------
# Using filter to Filter a List:
even_numbers = list(filter(lambda x: x % 2 == 0, my_list))

# ----------------------------------------------------------------------
# Creating a List of Unique Values:
unique_values = list(set(my_list))

# ----------------------------------------------------------------------
# Handling Keyboard Interrupt (Ctrl+C):
try:
    while True:
        # Code that runs indefinitely
        pass
except KeyboardInterrupt:
    # Code to handle Ctrl+C
    pass

# ----------------------------------------------------------------------
# Working with JSON Data:
import json
json_string = '{"key": "value"}'
data = json.loads(json_string)

# ----------------------------------------------------------------------
# Using itertools for Iteration:
from itertools import combinations
combos = combinations(my_list, 2)

# ----------------------------------------------------------------------
# Creating a Virtual Environment:
"""
shell command

python -m venv myenv
"""

# ----------------------------------------------------------------------
# Activating a Virtual Environment:
"""
shell command

source myenv/bin/activate  # On Unix/Linux
myenv\Scripts\activate    # On Windows
"""

# ----------------------------------------------------------------------
# Installing Packages with pip:

"""
shell command

pip install package_name
"""

# ----------------------------------------------------------------------
# Using a try...except Block with File Operations:
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    # Handle file not found
    pass

# ----------------------------------------------------------------------
# Working with Command-Line Arguments:
import sys
arg1 = sys.argv[1]


# ----------------------------------------------------------------------
# Using defaultdict for Default Values in Dictionaries:
from collections import defaultdict
my_dict = defaultdict(int)

# ----------------------------------------------------------------------
# Reading CSV Files with csv Module:
import csv
with open('data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # Process rows
        pass

# ----------------------------------------------------------------------
# Using Regular Expressions:
import re
pattern = r'\d+'
result = re.findall(pattern, my_string)

# ----------------------------------------------------------------------
# Creating and Using Generators:
def my_generator():
    yield 1
    yield 2

# ----------------------------------------------------------------------
# Using os Module for File Operations:
import os
file_exists = os.path.exists('file.txt')