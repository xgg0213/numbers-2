# Create a function that returns `True` if the first value is a perfect square
# of the second value; otherwise return `False`.

# A perfect square is a positive integer that can be expressed as the product of an integer by itself or as that integer squared.  For example, 25 is a perfect square of 5 as `5 x 5 = 25` and `5**2 = 25`.

# Write your function here.
def perfect_square(a,b):
    return a==b**2

print(perfect_square(15, 5)) #> False
print(perfect_square(25, 5)) #> True
print(perfect_square(81, 9)) #> True
print(perfect_square(9, 2))  #> False