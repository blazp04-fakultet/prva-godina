/*
Napisati program u kojem korisnik unosi elemente matrice dimenzije MxN ( koje također definira korisnik na početku programa ).

 Nakon unosa svih elemenata potrebno je izračunati zbroj elemenata koji nisu na glavnoj dijagonali.

*/
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int M, N;
    cout << "Unesite broj redova matrice (M): ";
    cin >> M;
    cout << "Unesite broj kolona matrice (N): ";
    cin >> N;

    int **matrica = new int *[M];
    for (int i = 0; i < M; ++i)
    {
        matrica[i] = new int[N]();
    }

    cout << "Unesite elemente matrice:\n";
    for (int i = 0; i < M; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            cout << "Unesite element na poziciji [" << i << "][" << j << "]: ";
            cin >> matrica[i][j];
        }
    }

    cout << "\nUnesena matrica:\n";
    for (int i = 0; i < M; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            cout << setw(8) << fixed << setprecision(2) << matrica[i][j];
        }
        cout << endl;
    }

    int zbroj = 0;
    for (int i = 0; i < M; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            if (i != j)
            {
                zbroj += matrica[i][j];
            }
        }
    }
    cout << "\nZbroj elemenata koji nisu na glavnoj dijagonali: " << zbroj << endl;

    for (int i = 0; i < M; ++i)
    {
        delete[] matrica[i];
    }
    delete[] matrica;

    return 0;
}