def razlika(brojevi):
    najmanji = [0, 0]
    razlika = 10000
    for i in range(len(brojevi)):
        for j in range(i+1, len(brojevi)):
            tr = abs(brojevi[i]-brojevi[j])
            if tr < razlika:
                razlika = tr
                najmanji[0] = brojevi[i]
                najmanji[1] = brojevi[j]
    return (najmanji[0], najmanji[1])


brojevi = [0, -3, 16, -1]
print(razlika(brojevi))
