# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

numbers = read_numbers()

if not numbers:
    sys.exit("Error: no numbers provided")

print(numbers)
print("minimum = ", min(numbers))
print("maximum = ", max(numbers))
print("mean = ", sum(numbers)/len(numbers))
print(sorted(numbers))
if len(numbers) % 2 == 0:
    median = sorted(numbers)[int(len(numbers)/2)] + sorted(numbers)[int(len(numbers)/2)-1]
    print(median/2)
else:
    median = sorted(numbers)[int(len(numbers)/2 - 0.5)]
    print(median)