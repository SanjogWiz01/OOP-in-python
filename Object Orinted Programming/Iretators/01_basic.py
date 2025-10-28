fruits = ["apple", "banana", "mango"]

# Get iterator
fruit_iter = iter(fruits)

print(next(fruit_iter))  # apple
print(next(fruit_iter))  # banana
print(next(fruit_iter))  # mango
# next(fruit_iter) -> StopIteration
