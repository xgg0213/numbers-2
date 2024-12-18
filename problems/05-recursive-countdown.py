# Create a function that recursively prints a countdown from 5 to 1.

# Write your function here.
def recursive_countdown(a):
    strA=''
    while a>0:
        strA= strA+str(a)
        a-=1
    return strA

print(recursive_countdown(5)) #> 5 4 3 2 1