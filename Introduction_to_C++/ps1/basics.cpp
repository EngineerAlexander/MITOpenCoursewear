#include<iostream>

using namespace std;

// test of conflicting declaration in scope
// int main(){

//     int arg1;
//     arg1 = -1;
//     int x, y, z;
//     char myDouble = '5';
//     char arg1 = 'A';
//     cout << arg1 << "\n";
//     return 0;

// }

// example using same variable names in different blocks with different scopes
// int main (){
//     int arg1;
//     arg1 = -1;
//     {
//         char arg1 = 'A';
//         cout << arg1 << "\n";
//     }
//     cout << arg1 << "\n";
//     return 0;
// }

// simple program: given N (list size), and N integers, compute basic math
int main(){

    int n;
    float sum = 0.0;
    int min;
    int max;
    cout << "Please input number of elements: ";
    cin >> n;
    cout << "\n";

    int array[n];
    // note ++i vs i++ act the same in a for loop. they are only different when being used in same line for assingment
    for(unsigned int i = 1; i <= n; i++){

        cout << "Please input number element #" << i <<": ";
        cin >> array[i];
        cout << endl;

        sum += (float)array[i];

        if(i == 1)
        {
            min = array[i];
            max = array[i];
        }
        else
        {
            if(array[i] > max)
            {
                max = array[i];
            }
            if(array[i] < min)
            {
                min = array[i];
            }
        }
    }

    float average = sum / n;


    cout << "Average: " << average << endl;
    cout << "Max: " << max << endl;
    cout << "Min: " << min << endl;
    cout << "Range: " << max - min << endl;

}