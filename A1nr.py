# Non-recursive program to calculate Fibonacci numbers

def non_recursive(n):
    fibo = []
    fibo.append(1)
    fibo.append(1)
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo


n = int(input("Enter a positive number: "))
print(f"First {n} Fibonacci numbers are")
print(non_recursive(n))

# ----------------------------------------------------------------------

# OUTPUT- 

# Enter a positive number: 9
# First 9 Fibonacci numbers are
# [1, 1, 2, 3, 5, 8, 13, 21, 34]