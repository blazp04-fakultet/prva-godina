/*
Definiraj strukturu Automobil koja kao atribute ima: proizvođača, model, godinu, predjenu kilometrazu i vlasnika.
Vlasnik je posebna struktura koja kao atribute ima ime, prezime i godine.

Unutar strukture Automobil definiraj funkciju "vozi" koja povećava kilometrazu auta za broj proslijeđen kao parametar.
Funkcija vraća novo stanje kilometraže.

U glavnom programu definiraj niz od 3 automobila.
Pozvati funkciju vozi na jednome od njih te prikazati vrijednost kilometraže prije i poslije pozivanja.
Ispisati sve automobile cij je vlasnik mladji od 30 godina.
*/

#include <iostream>
#include <string>
using namespace std;

struct Vlasnik
{
    string ime;
    string prezime;
    int godine;
};
struct Automobil
{
    string proizvodjac;
    string model;
    int godina;
    int kilometraza;
    Vlasnik vlasnik;

    void vozi(int k)
    {
        kilometraza += k;
    }
};

int main()
{
    Automobil automobili[3] = {
        {"Toyota", "Yaris", 2012, 50000, {"Petar", "Petrovic", 25}},
        {"Volkswagen", "Golf", 2015, 20000, {"Marko", "Markovic", 18}},
        {"Ford", "Focus", 2018, 1000, {"Ana", "Anic", 42}},
    };

    cout << "Kilometraza prije voznje: " << automobili[0].kilometraza << endl;
    automobili[0].vozi(1000);
    cout << "Kilometraza nakon voznje: " << automobili[0].kilometraza << endl;

    cout << "Automobili cij je vlasnik mladji od 30 godina: " << endl;
    for (int i = 0; i < 3; i++)
    {
        if (automobili[i].vlasnik.godine < 30)
        {
            cout << automobili[i].proizvodjac << " " << automobili[i].model << " - " << automobili[i].vlasnik.ime << " " << automobili[i].vlasnik.prezime << endl;
        }
    }
    return 0;
}