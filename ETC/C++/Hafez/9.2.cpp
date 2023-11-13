#include <iostream>
using namespace std;
int main()
{
	int x,r=0,c;
	cout<<"Enter a number: ";
	cin>>x;
	c=x;
	while (x!=0)
	{
		for (x;x!=0;x=x/10)
		{
			r*=10;
			r=r+x%10;
		}
		cout<<"Reverse of "<<c<<" is "<<r<<"\n";
		r=0;
		cout<<"Enter a number: ";
		cin>>x;
		c=x;
	}
	cout<<"End!";
}
