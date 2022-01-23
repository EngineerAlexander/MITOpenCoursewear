#include<iostream>

using namespace std;

// won't worry about ranges of inputs for now or error handling
int power(int a, int b)
{
    long long result = 1;
    while(b>0)
    {
        result *= a;
        b--;
    }
    
    return result;
}

int main()
{

    int a;
    int b;
    long long result;

    cout << "Input integer: ";
    cin >> a;
    cout << endl;

    cout << "Input integer to raise to: ";
    cin >> b;
    cout << endl;

    result = power(a, b);

    cout << "The result is: " << result << endl;
    
    return 0;
}