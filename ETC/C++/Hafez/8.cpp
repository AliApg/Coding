#include <iostream>
using namespace std;
int main()
{
	float a,b,min,max;
	char c;
	cout<<"Enter a: ";
	cin>>a;
	cout<<"Enter b: ";
	cin>>b;
	if (a>=b)
	{
		min=b;
		max=a;
	}else{
		min=a;
		max=b;
	}
	cout<<"Max= "<<max<<"\tmin= "<<min;
	cout<<"\nDo you want to Continue?\n";
	cin>>c;
	if (c=='y')
		cout<<"Yes";
	else if (c=='n')
		cout<<"No";
	else
		cout<<"Invalid character";
}
