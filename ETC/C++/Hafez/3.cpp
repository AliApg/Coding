#include <iostream>
using namespace std;
int main()
{
	double long sum=0,a,n,x,y,mult;
	cout<<"Enter N: ";
	cin>>n;
		while (n<=0)
		{
			if (n<=0)
			{
				cout<<n<<" is a wrong number, please try another number!"<<"\n"<<"Enter a new N: ";
				cin>>n;
			}
		}
	cout<<"Enter X: ";
	cin>>x;
	a=n;
		while (n>0)
		{
			mult=1;
			y=2*n-1;
				while (y>0)
				{
					mult*=(1/x);
					y--;
				}
			sum+=mult;
			n--;
		}
	cout<<"Addition of first "<<a<<" sentences of this sequence is= "<<sum;
}
