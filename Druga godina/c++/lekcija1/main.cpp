#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cout << "Unesite stranice pravokutnika: " << endl;
    cin >> a >> b;

    if (a <= 0 || b <= 0)
    {
        cout << "Nekorektne stranice!" << endl;
        return -1;
    }
    cout << "Povrsina pravokutnika je: " << a * b << endl;

    for (int i = 0; i < b; i++)
    {
        for (int j = 0; j < a; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
