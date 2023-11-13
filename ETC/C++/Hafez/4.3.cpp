#include <iostream>
using namespace std;
int main()
{
	int n,x,c=0,max;
	cout<<"N: ";
	cin>>n;
	cout<<"Num: ";
	cin>>x;
	max=x;
		for (n;n>1;n--)
		{
			cout<<"Num: ";
			cin>>x;
			if (max==x)
			{
				c++;
			}
			if (x>max)
			{
				max=x;
				c=0;
			}
		}
	cout<<"Max: "<<max<<"\t"<<" repeat: "<<c+1;
}
