#include<iostream>

using namespace std;

//function to return length of string without [] (indexing operator)
int sLength(char *string)
{
    char *ptr1 = string;

    int counter = 0;
    while( *ptr1 != '\0')
    {
        counter++;
        ptr1++;
    }

    return counter;
}

//function that swaps 2 values with call by reference
void swap(int &a, int &b)
{
    int temp = a;

    a = b;
    b = temp;

    return;
}

//function that swaps 2 values with pointers
void swap(int *a, int *b)
{
    int *temp = a;

    *a = *b;
    *b = *temp;

    return;
}

//function that swaps where 2 pointers point ***tricky***

int main()
{
    char string[] = {'T','e','s','t', '\0'};

    cout << "The length of the string is: " << sLength(string) << endl;;

    int a = 43; int b = 930;

    // swap with call by reference
    cout << "a = " << a << ", b = " << b << endl;
    swap(a, b);
    cout << "a = " << a << ", b = " << b << endl;
    cout << endl;

    // swap with pointers
    cout << "a = " << a << ", b = " << b << endl;
    swap(&a, &b);
    cout << "a = " << a << ", b = " << b << endl;
    cout << endl;

    // swap where pointers point

    return 0;
}