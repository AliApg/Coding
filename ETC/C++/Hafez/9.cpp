#include <iostream>
using namespace std;
int main ()
{
	int a,b,c,sum=0;
	cout<<"Enter first number: ";
	cin>>a;
	cout<<"Enter second number: ";
	cin>>b;
	if (a>b)
	{
		c=b;
		b=a;
		a=c;
	}
	else
		c=a;
	cout<<"Even numbers between "<<c<<" and "<<b<<":\n";
	for (a;a<=b;a=a+2)
	{
		if (a%2==0&&a!=0)
		{
			cout<<a<<"\t";
			sum+=a;
		}
		else if (a%2!=0)
			a--;
	}
	cout<<"\nSum of even numbers between "<<c<<" and "<<b<<" is= "<<sum;
}

