import random

random_number = random.randint(1, 10)

print("Komputer wylosował liczbę z zakresu od 1 do 10. Odgadnij ją, by wygrać!")
picked_number = int(input("Podaj liczbę: "))

if picked_number == random_number:
    print("Zgadza się! Wylosowana liczba to %d! Wygrałeś!" % random_number)
else:
    print("Nie zgadłeś. Wylosowaną liczbą było %d." % random_number)
