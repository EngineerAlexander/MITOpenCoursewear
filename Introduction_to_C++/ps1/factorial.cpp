#include<iostream>

using namespace std;

long long factorial(int num)
{
    long long result = 1;

    // for error handling we will just print out message for now and return -1 from the function
    // we will assume error handling for Windows 11 64-bit OS
    if(num<0)
    {
        cout << "Factorial is not defined on negative numbers." << endl;
        return -1;
    }
    else if(num>20)
    {
        cout << "Operating systems give garbage results for factorials greater than 16" << endl;
        return -1;
    }

    while(num>1)
    {
        result *= num--;
    }

    return result;
}

int main()
{
    short num;
    long long result;

    cout << "Please input a number to compute factorial: ";
    cin >> num;
    cout << endl;

    result = factorial(num);

    cout << "The Resulting factorial is: " << result << endl;

    return 0;
}