def cedeovi(player, slusanje):
    for cd in slusanje:
        for i in range(len(player)):
            if player[i] == cd:
                temp = player[-1]
                player[-1] = player[i]
                player[i] = temp

                break

    return player[:-1]


player = ["SEVERINA",
          "ROZGA",
          "MAGAZIN",
          "JACQUES"]

slusanje = ["ROZGA", "MAGAZIN", "JACQUES"]

print(cedeovi(player, slusanje))
