#include <iostream>
using namespace std;
int main()
{
	int n,i,j,k;
	cin>>n;
	for (i=1;i<=n;i++)
	{
		for (j=n-i;j>=1;j--)
		{
			cout<<" ";
		}
		for (k=1;k<=2*i-1;k++)
		{
			cout<<'*';
		}
		cout<<"\n";
	}
}
