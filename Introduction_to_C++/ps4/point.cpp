#include<iostream>
using namespace std;

class Point
{
    private:
        int x;
        int y;

    public:
        Point(int a = 0.0, int b = 0.0)
        {
            x = a;
            y = b;
        }
        int getX()
        {
            return x;
        }
        int getY()
        {
            return x;
        }
        void setX()
        {
            
        }

    
};

int main()
{
    Point test(1.0, 2.0);

    return 0;
}