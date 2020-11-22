num1 = int(input("Podaj pierwszą liczbę "))
num2 = int(input("podaj drugą liczbę "))

print("Dostępne operacje: dod, odj, mnż, dziel, potęga")
action = input("Twój wybór: ")

if action == "dod":
    print("Wynik dodawania to ", num1 + num2)
elif action == "odj":
    print("Wynik odejmowania to ", num1 - num2)
elif action == "mnż":
    print("Wynik mnożenia to: ", num1 * num2)
elif action == "dziel":
    print("Wynik dzielenia to: ", num1 / num2)
elif action == "potęga":
    print("Wynik potęgowania to: ", num1 ** num2)
else:
    print("Nie wybrano poprawnego działania.")
