imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
         'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
         'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
         'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
         'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

rezultati = {}

for ime in imena:
    if ime in rezultati:
        rezultati[ime] += 1
    else:
        rezultati[ime] = 1

# print(rezultati)

for ime in rezultati:
    if rezultati[ime] != 1:

        print(ime, rezultati[ime])
