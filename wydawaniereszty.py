def wydaj_reszte(kwota):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    i = 0
    wynik = []

    while kwota > 0 and i < len(nominaly):
        if kwota >= nominaly[i]:
            ile = kwota // nominaly[i]
            kwota -= nominaly[i] * ile
            wynik.append((nominaly[i], ile))
        i += 1

    return wynik

kwota = int(input('Podaj reszte do wyplacenia: '))
reszta = wydaj_reszte(kwota)

for nom, ile in reszta:
    print(f"{nom} zł: x {ile}")
