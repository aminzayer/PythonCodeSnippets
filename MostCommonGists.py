# 10 more Python code snippets for common programming tasks
# Calculate Factorial:
# Calculate the factorial of a number using a recursive function.
def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

# Reverse a String:
# Reverse a string using slicing.
def reverse_string(s):
    return s[::-1]  # Slice the string with a step of -1 to reverse it

# Find the Intersection of Two Lists:
# Find the common elements between two lists.

def intersection(list1, list2):
    return list(set(list1) & set(list2))  # Convert lists to sets, then use set intersection

# Calculate Fibonacci Series:
# Generate the Fibonacci series up to a specified number of terms.
def fibonacci(n):
    a, b = 0, 1
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a + b  # Generate the next Fibonacci number
    return result

# Check for a Palindrome:
# Determine whether a given string is a palindrome.
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Compare the string to its reverse

# Calculate Square Root:
# Calculate the square root of a number.
import math

def square_root(x):
    return math.sqrt(x)  # Use the math module's sqrt function to calculate the square root

# Sum of Digits:
# Calculate the sum of the digits of a number.
def sum_of_digits(n):
    return sum(map(int, str(n)))  # Convert the number to a string, map digits to integers, and sum them

# Count Vowels in a String:
# Count the number of vowels in a string.
def count_vowels(s):
    vowels = "AEIOUaeiou"  # Define a string containing vowels
    return sum(1 for char in s if char in vowels)  # Count vowels in the input string

# Generate Random Password:
# Generate a random password of a specified length.
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation  # Define characters for the password
    password = ''.join(random.choice(characters) for _ in range(length))  # Generate a random password
    return password

# Check for Prime Number:
# Determine whether a given number is prime.
def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Check for divisibility by numbers in the form 6k +/- 1
        i += 6
    return True  # The number is prime