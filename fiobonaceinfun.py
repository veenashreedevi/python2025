def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fib_sequence = fibonacci(terms)
print("Fibonacci sequence:", fib_sequence)
