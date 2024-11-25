#include <iostream>
using namespace std;

void matrice()
{
    int matrica[4][4];
    cout << "Unesite elemente matrice: " << endl;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cout << "Unesite element [" << i + 1 << "][" << j + 1 << "]: ";
            cin >> matrica[i][j];
        }
    }

    cout << "Unesena matrica:" << endl;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cout << matrica[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    matrice();

    int niz[10] = {12, 32, 43, 54, 51, 16, 27, 18, 79, 210};
    cout << "\nSortirani niz:" << endl;

    // Bubble sort
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9 - i; j++)
        {
            if (niz[j] > niz[j + 1])
            {
                swap(niz[j], niz[j + 1]);
            }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        cout << niz[i] << " ";
    }
    cout << endl;

    return 0;
}