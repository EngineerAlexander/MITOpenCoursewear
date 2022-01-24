#include<iostream>

using namespace std;

void printArray(const char arr[], const char sep)
{
    const char *ptr1 = arr;
    while(*ptr1 != '\0')
    {
        if(*ptr1 == sep)
        {
            cout << endl;
            ptr1++;
            continue;
        }
        else if(*ptr1 == ' ')
        {
            ptr1++;
            continue;
        }
        cout << *ptr1;
        ptr1++;
    }

    return;
}

// non pointer method
void reverse(int arr[], const int size)
{
    for(int i = 0; i < size / 2; i++) //loop through size of array
    {
        int tmp = arr[i]; //pull a value into tmp so it doesn't get overwritten

        int reverse_index = size - i - 1; //find index it's going to and vice versa

        arr[i] = arr[reverse_index]; //replace current value with new value
        arr[reverse_index] = tmp; //put old value in proper place
    }

    return;
}

// pointer method ***tricky***
void reverseWithPointers(int arr[], const int size)
{

    for(int i = 0; i < size / 2; i++) //loop through size of array
    {
        int tmp = *(arr + i);

        int reverse_index = size - i - 1; //find index it's going to and vice versa
        
        *(arr + i) = *(arr + reverse_index);
        *(arr + reverse_index) = tmp;
    }
}

void printArray(int array[], int size)
{
    cout <<"Array is currently: ";
    for(int i = 0; i < size; i++)
    {
        cout << array[i];
        if (i != (size-1))
        {
            cout << ", ";
        }
    }
    cout << endl;
    return;
}

// assume these exist for now
const int WIDTH = 5;
const int LENGTH = 5;

void transpose(const int input[][LENGTH], int output[][WIDTH])
{
    for(int i = 0; i < WIDTH; i++)
    {
        for(int j = 0; j < LENGTH; j++)
        {
            output[j][i] = input[i][j];
        }
    }

    return;
}

void printMatrix(int array[][LENGTH], int rows, int columns)
{
    cout <<"Matrix is currently: " << endl;
    for(int row = 0; row < rows; row++)
    {
        for(int column = 0; column < columns; column++)
        {
            cout << array[row][column] <<" ";
        }
        cout << endl;
    }
    cout << endl;
    return;
}

int main()
{
    // string literal stored in array print out substrings seperated by ,
    const char string[] = "The, One, Is, Trueeee";
    const char sep = ',';

    printArray(string, sep);
    cout << endl;

    // -------------------------------------------------------------------

    int size = 10;
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    
    printArray(array, size);
    reverse(array, size);
    printArray(array, size);

    // -------------------------------------------------------------------

    int input[5][5] = {1, 2, 3 , 4, 5, 1, 2, 3 , 4, 5, 1, 2, 3 , 4, 5, 1, 2, 3 , 4, 5, 1, 2, 3 , 4, 5};
    int output[5][5] = {};

    printMatrix(input, 5, 5);
    transpose(input, output);
    printMatrix(output, 5, 5);

    return 0;
}