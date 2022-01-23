#include<iostream>

using namespace std;

void squareInt(int *a)
{
    *a = *a * *a;
}

int main()
{
    int x = 5;

    cout << "Input number to square: ";
    cin >> x;
    squareInt(&x); //dereferences x aka passes a pointer (memory address)
    cout << endl << x << endl;

}