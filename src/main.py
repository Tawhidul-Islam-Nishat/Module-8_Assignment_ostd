from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Tawhidul Islam Nishat")
print("Today's date:", date.today())

print("10 + 5 =", add(10, 5))
print("10 - 5 =", subtract(10, 5))
print("10 * 5 =", multiply(10, 5))
print("10 / 5 =", divide(10, 5))

try:
    print(divide(10, 0))
except ZeroDivisionError as error:
    print("Error:", error)

try:
    print(add("10", 5))
except TypeError as error:
    print("Error:", error)
