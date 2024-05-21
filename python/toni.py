brojevi = [1, 5, 8, 7, 14, 16, 18, 0, 6, 100, 200, 600, 555, -8, -66, 99]

najmanji_broj = int(0)
najveci_broj = int(0)

for broj in brojevi:
    if broj < najmanji_broj:
        najmanji_broj = broj
    if broj > najveci_broj:
        najveci_broj = broj

print("Najmanji broj je:", najmanji_broj)
print("Najveci broj je:", najveci_broj)
