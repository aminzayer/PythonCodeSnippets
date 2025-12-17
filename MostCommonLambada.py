import math
from functools import reduce

from buscador.flask_app.models.user import EMAIL_REGEX
# 1. Calculate the square of a number
square = lambda x: x**2

# 2. Calculate the cube of a number
cube = lambda x: x**3

# 3. Calculate the factorial of a number
factorial = lambda x: 1 if x < 2 else x * factorial(x-1)

# 4. Calculate the nth Fibonacci number
fibonacci = lambda n: reduce(lambda x, _: (x[1], x[0] + x[1]), range(n), (0, 1))[0]

# 5. Check if a number is even
is_even = lambda x: x % 2 == 0

# 6. Check if a number is odd
is_odd = lambda x: x % 2 != 0

# 7. Check if a number is positive
is_positive = lambda x: x > 0

# 8. Check if a number is negative
is_negative = lambda x: x < 0

# 9. Reverse a string
reverse_string = lambda s: s[::-1]

# 10. Check if a string is a palindrome
is_palindrome = lambda s: s == reverse_string(s)

# 11. Check if a string is a digit
is_digit = lambda s: s.isdigit()

# 12. Check if a string is a lowercase letter
is_lowercase = lambda s: s.islower()

# 13. Check if a string is a uppercase letter
is_uppercase = lambda s: s.isupper()

# 14. Convert a string to lowercase
to_lowercase = lambda s: s.lower()

# 15. Convert a string to uppercase
to_uppercase = lambda s: s.upper()

# 16. Convert a string to a list of characters
to_list = lambda s: list(s)

# 17. Check if a character is a digit
is_char_digit = lambda c: c.isdigit()

# 18. Check if a character is a lowercase letter
is_char_lowercase = lambda c: c.islower()

# 19. Check if a character is a uppercase letter
is_char_uppercase = lambda c: c.isupper()

# 20. Convert a character to lowercase
to_char_lowercase = lambda c: c.lower()

# 21. Convert a character to uppercase
to_char_uppercase = lambda c: c.upper()

# 22. Check if a number is prime
is_prime = lambda n: all(n % i for i in range(2, int(n**0.5) + 1)) and n > 1

# 23. Calculate the sum of two numbers
sum = lambda x, y: x + y

# 24. Calculate the difference of two numbers
difference = lambda x, y: x - y

# 25. Calculate the product of two numbers
product = lambda x, y: x * y

# 26. Calculate the quotient of two numbers
quotient = lambda x, y: x / y

# 27. Check if a number is divisible by another number
is_divisible_by = lambda x, y: x % y == 0

# 28. Check if a number is a power of another number
is_power_of = lambda x, y: x == y**round(math.log(x, y))

# 29. Check if a string contains another string
contains = lambda s, t: t in s

# 30. Calculate the length of a string
length = lambda s: len(s)

# 31. Calculate the length of a list
list_length = lambda l: len(l)

# 32. Calculate the length of a tuple
tuple_length = lambda t: len(t)

# 33. Check if a string starts with another string
starts_with = lambda s, t: s.startswith(t)

# 34. Check if a string ends with another string
ends_with = lambda s, t: s.endswith(t)

# 35. Calculate the minimum of two numbers
minimum = lambda x, y: min(x, y)

# 36. Calculate the maximum of two numbers
maximum = lambda x, y: max(x, y)

# 37. Check if a string is a whitespace string
is_whitespace = lambda s: s.isspace()

# 38. Check if a string is a alphanumeric string
is_alphanumeric = lambda s: s.isalnum()

# 39. Calculate the absolute value of a number
absolute_value = lambda x: abs(x)

# 40. Round a number to the nearest integer
round_number = lambda x: round(x)

# 41. Round a number to a specified number of decimal places
round_decimal = lambda x, n: round(x, n)

# 42. Check if a string is a alphabetic string
is_alphabetic = lambda s: s.isalpha()

# 43. Convert a number to a string
to_string = lambda x: str(x)

# 44. Check if a number is an integer
is_integer = lambda x: x.is_integer()

# 45. Calculate the greatest common divisor of two numbers
gcd = lambda x, y: math.gcd(x, y)

# 46. Calculate the least common multiple of two numbers
lcm = lambda x, y: x * y // gcd(x, y)

# 47. Calculate the number of digits in a number
number_of_digits = lambda x: len(str(x))

# 48. Check if a number is a float
is_float = lambda x: isinstance(x, float)

# 49. Check if a number is a complex number
is_complex = lambda x: isinstance(x, complex)

# 50. Calculate the complex conjugate of a complex number
complex_conjugate = lambda x: x.conjugate()

# 51. Check if a string is a hexadecimal string
is_hexadecimal = lambda s: s.isascii() and all(c in string.hexdigits for c in s)

# 52. Check if a string is a octal string
is_octal = lambda s: s.isascii() and all(c in octdigits for c in s)

# 53. Check if a string is a binary string
is_binary = lambda s: s.isascii() and all(c in bdigits for c in s)

# 54. Check if a string is a valid email address
is_email = lambda s: bool(EMAIL_REGEX.match(s))

# 55. Check if a string is a valid URL
is_url = lambda s: bool(url_regex.match(s))

# 56. Check if a string is a valid IPv4 address
is_ipv4 = lambda s: bool(ipv4_regex.match(s))

# 57. Check if a string is a valid IPv6 address
is_ipv6 = lambda s: bool(ipv6_regex.match(s))

# 58. Check if a string is a valid MAC address
is_mac_address = lambda s: bool(mac_address_regex.match(s))

# 59. Calculate the average of a list of numbers
average = lambda l: sum(l) / len(l)

# 60. Flatten a list of lists
flatten = lambda l: [item for sublist in l for item in sublist]

# 61. Convert a string to a list of words
words = lambda s: s.split()

# 62. Calculate the factorial of a number using a loop
factorial_loop = lambda x: 1 if x < 2 else factorial_loop(x-1) * x

# 63. Check if a string is a palindrome using a loop
is_palindrome_loop = lambda s: s == s[::-1]