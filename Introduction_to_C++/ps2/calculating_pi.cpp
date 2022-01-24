#include<iostream>
#include<ctime>
#include<cmath>
//#include<stdlib>

using namespace std;

// calculate pi by using dartboard throwing method
// my own way
// ratio of darts in the circle to total darts should be circle area of square area
// ratio = (pi r^2)/(4r^2) = pi/4 -----> pi = ratio*4
// can simplify problem to top right quadrant only!!!

bool inCircle(double cords[2], double r)
{

    double d = sqrt(pow(*cords, 2) + pow(*(cords+1), 2));

    if(d <= r)
    {
        return true;
    }
    return false;
}

// implemented radius argument to check that the radius should not matter
double calculatePi(long sim_nums, double r = 1.0)
{
    srand(time(0)); //sets random number generator seed with clock

    long in_num = 0;
    long throw_num = 1;

    for(;throw_num < sim_nums; throw_num++)
    {
        double cords[2] = {r*(rand()/ (double)RAND_MAX), r*(rand()/ (double)RAND_MAX)};
        if(inCircle(cords, r))
        {
            in_num++;
        }
    }

    return 4*(in_num/ (double)throw_num);
}

int main()
{
    double r = 1.256; //sets radius of circle in experiment

    long sim_nums = 100000000;

    double pi_experimental = calculatePi(sim_nums, r);

    cout << "The result of pi is: " << pi_experimental << endl;

    return 0;
}