from typing import List, Tuple, Union, Dict, Any
n : int = 7

name: str = "Saad"

print(type(n))

print(f"Hello, {name}! Your number is {n}.")

def sum(a:int, b:int) -> int:
    return a + b

print(sum(3, 8))


# These annotations help in making the code self-documenting and allow developers to
# understand the data structures used at a glance.

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
print(numbers)

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
print(f"Name: {person[0]}, Age: {person[1]}")

scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
print(f"Alice's score: {scores['Alice']}")


identifier: Union[int, str] = "ID123"
print(f"Identifier: {identifier}") # Output: Identifier: ID123


identifier = 12345 # Also valid


