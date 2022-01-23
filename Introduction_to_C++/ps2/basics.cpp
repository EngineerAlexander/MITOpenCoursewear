#include<iostream>
#include<cstdlib>
#include<ctime>

using namespace std;

// default arguments if there's a common value for something being passed VERY SIMPLE EXAMPLE
// void printNTimes(char *msg , int n = 1)
// {

//     for (int i = 0; i < n ; ++ i )
//     {
//         cout << msg ;
//     }
//     // don't need return in void function
// }
//--------------------------------------------------------------------------------------------
// if passing values by reference you can make stuff immutable with const
// void print(const long &x) //pass-by-reference avoids overhead of copying large number
// {
//     cout << x;
// }

// int main()
// {
//     long x = 1234321443;
//     print(x); //gurantee no change in x

//     return 0;
// }
//--------------------------------------------------------------------------------------------
// int main()
// {
//     srand(time(0)); //sets the time seed. time (0) returns current time as a number

//     //note if called quickly, will get the same number with this implementation
//     int ranNum = rand();

//     cout << "A random number: " << ranNum << endl;

//     return 0;
// }
//--------------------------------------------------------------------------------------------

// note for functions that return pointers, the variable is normally cleared from memory after the function exits scope
// if it is defined locally. return &x in this case will likely throw a runtime error


// again ensure functions used are defined beforehand. or define their header beforehand
// void printNum(int number)
// {
//     cout << number;
// }

void printNum(int a); //header

int main()
{
    printNum(35);
    return 0;

}

void printNum(int a)
{
    cout << a;
}