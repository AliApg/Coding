#include <iostream>
using namespace std;
int main()
{
	int a[3][3],b[3][3],c[3][3],i,j;
		cout<<"Enter first matrix:"<<"\n";
		for (i=0;i<3;i++)
		{
			for (j=0;j<3;j++)
			{
				cin>>a[i][j];
			}
		}
		cout<<"Enter second matrix:"<<"\n";
			for (i=0;i<3;i++)
		{
			for (j=0;j<3;j++)
			{
				cin>>b[i][j];
			}
		}
		for (i=0;i<3;i++)
			{
				cout<<"\n";
				for (j=0;j<3;j++)
				{
					c[i][j]=a[i][j]+b[i][j];
					cout<<c[i][j]<<"\t";
				}
				cout<<"\n";
			}
}
