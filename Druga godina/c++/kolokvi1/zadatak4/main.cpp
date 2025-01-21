/*
U glavnom programu od korisnika zatražiti unos cijelog broja.

Definirati pokazivač na taj broj te ispisati adresu i vrijednost definiranog pokazivača.

Definirati funkciju "uvecaj" koja uvecava broj za vrijednost poslanu kao parametar.

Koristeći ranije definiranu funkciju uvecaj korisnikov broj za 10 i uvećani broj ispiši u glavnom programu.

Napomena: Funkcija "uvecaj" ne vraća ništa, a prima pokazivac kao parametar
*/

#include <iostream>
using namespace std;

void uvecaj(int *pokazivac)
{
    *pokazivac += 10;
}
int main()
{
    int broj = 0;
    cout << "Unesite broj: ";
    cin >> broj;

    int *pokazivac = &broj;
    cout << "Adresa broja: " << pokazivac << endl;
    cout << "Vrijednost broja: " << *pokazivac << endl;

    uvecaj(pokazivac);

    cout << "Uvečani broj: " << *pokazivac << endl;

    return 0;
}