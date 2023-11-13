#include <iostream>
using namespace std;
int main()
{
	int a=1,b=1,c;
	cout<<"Enter a number: ";
	cin>>a;
	c=a;
	while (a!=0)
	{
		while (a/10!=0)
		{
			a=a/10;
			b++;
		}
		cout<<c<<" has "<<b<<" digites\n";
		b=1;
		cout<<"Enter a number: ";
		cin>>a;
		c=a;
	}
	cout<<"End!";
}
