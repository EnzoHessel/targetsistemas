def fibonacciNumber(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

number = int(input("Informe um número: "))

if fibonacciNumber(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")

