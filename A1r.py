# Recursive program to calculate Fibonacci numbers

def recursive(n):
    if (n < 2):
        return 1

    return recursive(n-1) + recursive(n-2)


n = int(input("Enter a positive number: "))
print(f"First {n} Fibonacci numbers are")
for i in range(n):
    print(recursive(i), end=" ")

# ----------------------------------------------------------------------

# OUTPUT-

# Enter a positive number: 9
# First 9 Fibonacci numbers are
# 1 1 2 3 5 8 13 21 34 
