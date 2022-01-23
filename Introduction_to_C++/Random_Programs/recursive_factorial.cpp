#include<iostream>

using namespace std;

// return nth number of fib sequence. won't worry about error handling.
long fib(int a)
{
    if(a == 1 || a == 2)
        return 1;
    else
        return fib(a-1) + fib(a-2);
}

int main()
{
    int a;
    cout << "Please input fib sequence number: ";
    cin >> a;
    cout << endl;

    cout << fib(a);
}