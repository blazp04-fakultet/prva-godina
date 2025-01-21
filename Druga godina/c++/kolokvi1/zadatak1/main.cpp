/*
Napisati funkciju koja kao argumente prima 2 cijela broja te kao rezultat vraća sumu neparnih brojeva u intervalu između njih.

U glavnom programu od korisnika zatražiti unos intervala te vratiti rezultat prethodno definirane funkcije


*/

#include <iostream>
using namespace std;

int sumaNeparnihBrojeva(int start, int end)
{
    int suma = 0;
    for (int i = start; i <= end; i++)
    {
        if (i % 2 != 0)
        {
            suma += i;
        }
    }
    return suma;
}

int main()
{
    int start, end;
    cout << "Unesite pocetni broj intervala: ";
    cin >> start;
    cout << "Unesite krajnji broj intervala: ";
    cin >> end;

    int suma = sumaNeparnihBrojeva(start, end);
    cout << "Suma neparnih brojeva izmedju " << start << " i " << end << " je: " << suma << endl;
    return 0;
}
