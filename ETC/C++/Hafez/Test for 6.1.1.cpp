//	test:

#include <iostream>
using namespace std;
int main()
{
	int a[2][3],b[3][2],c[2][2],i,j,m,n,o;
		cout<<"Enter first matrix:"<<"\n";
		for (i=0;i<2;i++)
		{
			for (j=0;j<3;j++)
			{
				cin>>a[i][j];
			}
		cout<<"\n";
		}
		cout<<"Enter second matrix:"<<"\n";
		for (i=0;i<3;i++)
		{
			for (j=0;j<2;j++)
			{
				cin>>b[i][j];
			}
		cout<<"\n";
		}
		for (i=0;i<2;i++)
		{
			for (j=0;j<2;j++)
			{
				c[i][j]=0;
			}
		}
		for (m=0;m<2;m++)
		{
			for (n=0;n<2;n++)
			{
				for (o=0;o<3;o++)/*o j*/
				{
					c[m][n]+=(a[m][o]*b[o][m]);
				}
				cout<<c[m][n]<<"\t";
			}
			cout<<"\n";
		}
//		for (i=0;i<3;i++)
//			{
//				cout<<"\n";
//				for (j=0;j<3;j++)
//				{
//					c[i][j]=a[i][j]+b[i][j];
//					cout<<c[i][j]<<"\t";
//				}
//				cout<<"\n";
//			}
}
