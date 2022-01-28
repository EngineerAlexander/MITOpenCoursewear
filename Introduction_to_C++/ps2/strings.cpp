#include<iostream>

using namespace std;

int main()
{
    char *OddOrEven = "Never odd or even";

    char *nthCharPtr = &OddOrEven[5];

    nthCharPtr-=2;

    cout << *nthCharPtr << endl;

    char **pointerPtr = &nthCharPtr;

    cout << pointerPtr << endl;

    cout << **pointerPtr << endl;

    nthCharPtr++;

    cout << nthCharPtr - OddOrEven;

    return 0;
}