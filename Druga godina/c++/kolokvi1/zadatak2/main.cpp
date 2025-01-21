/*
Napisati program koji od korisnika traži unos brojeva sve dok ne unese 0.
Unesene brojeve spremati u niz i zatim koristeći algoritam “Bubble sort” sortirati niz.
Napomena: niz ograničiti na 100 brojeva.

*/

#include <iostream>
using namespace std;

void bubleSort(int niz[], int brojElemenata)
{
    for (int i = 0; i < brojElemenata - 1; i++)
    {
        for (int j = 0; j < brojElemenata - i - 1; j++)
        {
            if (niz[j] > niz[j + 1])
            {
                int temp = niz[j];
                niz[j] = niz[j + 1];
                niz[j + 1] = temp;
            }
        }
    }
}
int main()
{
    int niz[100] = {0};
    int brojElemenata = 0;
    while (true)
    {
        int broj;
        cout << "Unesite broj: ";
        cin >> broj;
        if (broj == 0)
        {
            break;
        }
        niz[brojElemenata] = broj;
        brojElemenata++;
    }

    bubleSort(niz, brojElemenata);

    for (int i = 0; i < brojElemenata; i++)
    {
        cout << niz[i] << ",";
    }

    return 0;
}
