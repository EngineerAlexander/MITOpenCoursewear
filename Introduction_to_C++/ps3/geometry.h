#include<iostream>

using namespace std;

double getX();
double getY();

class Point {
    private:
        double x, y;
    public:
        Point(double x = 0.0, double y = 0.0) {
            Point::x = x;
            Point::x = y;
        }
        int getX() {
            return Point::x;
        }
        int getY() {
            return Point::y;
        }
};