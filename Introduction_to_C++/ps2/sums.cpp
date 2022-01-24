#include<iostream>

using namespace std;

int sum(const int a, const int b)
{
    return a + b;
}

int sum(const int a, const int b, const int c)
{
    return c + sum(a, b);
}

int sum(const int a, const int b, const int c, const int d)
{
    return d + sum(a, b, c);
}

double sum(const double a, const double b)
{
    return a + b;
}


// note this does not work because it has identical variable types and name
// int sum(const int a, const int b, const int c = 0, const int d = 0)
// {
//     return a + b + c + d;
// }

// sum from user inputs using loop, non-pointer, non-recursion------------------

// int sum(int array[], int size = 1)
// {
//     int sum = 0;
//     for(int i = 0; i < size; i++)
//     {
//         sum = sum + array[i];
//     }

//     return sum;
// }

// int main()
// {
//     int size;

//     cout << "Input number of elements to sum: ";
//     cin >> size;
//     cout << endl;

//     int inputs[size];
//     for(int counter = 0; counter < size; counter++)
//     {
//         cout << "Input element number " << counter << ": ";
//         cin >> inputs[counter];
//         cout << endl;
//     }

//     int ans = sum(inputs, size);

//     cout << "The resulting sum is: " << ans << endl;

//     return 0;
// }

// sum from user inputs using pointers and recursion-----------------------------

int sum(int array[], int size = 1)
{
    int *ptr1 = array;
    int *ptr2 = array + size - 1;

    if(size == 0)
    {
        return 0;
    } 

    return *ptr1 + sum(ptr1+1, size - 1);
}

int main()
{
    int size = 5;
    int inputs[size] = {1, 2, 3, 4, 5};

    int ans = sum(inputs, size);

    cout << "Hardcoded answer is: " << ans << endl;
}

