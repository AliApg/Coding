#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int a,b,c,r;
	cout<<"a: ";
	cin>>a;
	cout<<"b: ";
	cin>>b;
	cout<<"c: ";
	cin>>c;
	((pow(a, 2)==pow(b, 2)+pow(c, 2))||(pow(b, 2)==pow(c, 2)+pow(a, 2))||(pow(c, 2)==pow(a, 2)+pow(b, 2)))?cout<<"True":cout<<"False";
}
