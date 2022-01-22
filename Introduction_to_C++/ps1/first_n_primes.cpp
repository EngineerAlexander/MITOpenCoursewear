#include<iostream>

using namespace std;

// O(n) time
bool isPrime(int n)
{
    if (n == 1 || n ==2)
    {
        return false;
    }

    for(int i = 2; i <= n/2; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }

    return true;
}

// O(n^2) = O(n) * O(n)
int main()
{
    int n;

    cout << "Please input an integer n to find the first n primes: ";
    cin >> n;
    cout << "\n";

    int primes[n];
    int num_found = 0;
    int cur = 1;

    // O(n) time
    while(num_found < n)
    {
        // O(n) time on the check
        if(isPrime(cur))
        {
            cout << cur << endl;
            primes[num_found] = cur;
            num_found++;
        }
        cur++;
    }
}