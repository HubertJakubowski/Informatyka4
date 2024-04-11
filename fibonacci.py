def f(n):
    if n < 3:
        return 1
    else:
        return f(n-2) + f(n-1)


n = int(input('podaj liczbę: '))
print("Liczba Fibonacciego dla n =", n, "to", f(n))
