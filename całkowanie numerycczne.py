def f(x):
    return x * x + x + 2

def oblicz_pole(a, b, n):
    x = (b - a) / n  
    S = 0  
    srodek = a + (b - a) / (2.0 * n)  

    for i in range(n):
        S += f(srodek)  
        srodek += x 

    return S * x 

a = int(input("podaj pierwszą liczbę przedziału "))
b = int(input("podaj ostatnią liczbę przedziału "))
n = int(input("podaj liczbę trapezów "))
wynik = oblicz_pole(a, b, n)
print("Pole figury wynosi: ", wynik)
