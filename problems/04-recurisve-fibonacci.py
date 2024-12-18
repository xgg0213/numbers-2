# Create a function that returns the Fibonacci sequence of the given value.

# Write your function here.
def recursive_fib(a):
    arr=[0,1,1]
    if a<=2:
        return arr[a]
    i=3
    while i<=a:
        arr.append(int(arr[i-1])+int(arr[i-2]))
        i+=1
    return arr[a]

print(recursive_fib(1))     #> 1
print(recursive_fib(2))     #> 1
print(recursive_fib(4))     #> 3
print(recursive_fib(6))     #> 8
print(recursive_fib(12))    #> 144

# 0,1,1,2,3,5,8,13,21