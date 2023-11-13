#include <iostream>
using namespace std;
int main()
{
	int a[4][2],b[2][3],c[4][3],i,j;
		cout<<"Enter first matrix (4 rows & 2 columns):"<<"\n";
		cout<<"\n";
		for (i=0;i<4;i++)
		{
			cout<<"Row number: "<<i+1<<"\n";
			for (j=0;j<2;j++)
			{
				cin>>a[i][j];
			}
			cout<<"\n";
		}
		cout<<"Enter second matrix (2 rows & 3 columns):"<<"\n";
		cout<<"\n";
		for (i=0;i<2;i++)
		{
			cout<<"Row number: "<<i+1<<"\n";
			for (j=0;j<3;j++)
			{
				cin>>b[i][j];
			}
			cout<<"\n";
		}
		cout<<"Answer:\n";
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
