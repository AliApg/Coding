#include "iostream"
using namespace std;
int main()
{
	int x,i,f=1;
	cout<<"Enter a number: ";
	cin>>x;
	while (x!=0)
	{
		if (x<0)
		{
			cout<<x<<" is not a possetive number";
		}
		else
		{
		for (i=1;i<=x;i++)
		{
			f*=i;
		}
		cout<<x<<" factoriel is: "<<f;
		f=1;
		}
		cout<<"\nEnter a number: ";
		cin>>x;
	}
	cout<<"End!";
}
