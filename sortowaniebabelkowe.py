tablica = [7, 3, 1, 2, 5]
rozmiar = len(tablica)

print("zawartosc przed sortowaniem: ", tablica)

for i in range(rozmiar):
    for j in range(0, rozmiar-i-1):
        if tablica[j] > tablica[j+1]:
            tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
            print(tablica)

print("Po sortowaniu: ", tablica)
