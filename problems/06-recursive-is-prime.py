# Create a function called `is_prime` that takes in a number and a variable that
# equates to 2. The function should return True/False if the number is a prime
# number. Bonus: Try to do this recursively.

# Write your solution here.
def is_prime(a):
    if a==1:
        return False
    if a==2:
        return True
    i=2
    while i<a:
        if a % i == 0:
            return False
        i+=1
    return True

print(is_prime(1))  #> False
print(is_prime(2))  #> True
print(is_prime(3))  #> True
print(is_prime(5))  #> True
print(is_prime(9))  #> False
print(is_prime(15)) #> False