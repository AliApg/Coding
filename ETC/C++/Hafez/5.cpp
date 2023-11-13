#include <iostream>
using namespace std;
int main()
{
	int a[10],i,j;
	cout<<"Input 10 numbers: "<<"\n";
	for (i=0;i<10;i++)
	{
		cout<<i+1<<": ";
		cin>>a[i];
	}
	cout<<a[0]<<"\t";
	for (i=1;i<10;i++)
	{
		for (j=0;j<i;j++)
		{
			if (a[j]==a[i])
			{
				break;
			}
		}
		if (j==i)
			cout<<a[i]<<"\t";
	}
}
