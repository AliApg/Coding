#include <iostream>
using namespace std;
int main()
{
	int i,j,k,p,q,r;
	cout<<"Enter the number of rows for first matrix: ";
	cin>>i;
	
	cout<<"\n"<<"Enter the number of columns for first matrix: ";
	cin>>j;
	
	cout<<"\n"<<"Enter the number of columns for second matrix: ";
	cin>>k;
	
	system("cls");

	int a[i][j],b[j][k],c[i][k];
	
//	First matrix:

	cout<<"Enter first matrix values ("<<i<<" rows & "<<j<<" columns)\n";
	for (q=0;q<j;q++)
	{
		cout<<"\n";
		cout<<"Column number "<<q+1<<":\n";
		for (p=0;p<i;p++)
		{
			cin>>a[p][q];
		}
	}
	system("cls");
	
//	Second matrix:

	cout<<"Enter second matrix values ("<<j<<" rows & "<<k<<" columns)\n";
	for (q=0;q<k;q++)
	{
		cout<<"\n";
		cout<<"Column number "<<q+1<<":\n";
		for (r=0;r<j;r++)
		{
			cin>>b[r][q];
		}
	}
	system("cls");

//	Make c zero:

	for (q=0;q<k;q++)
	{
		for (p=0;p<i;p++)
		{
			c[p][q]=0;
		}
	}
	
//	Multiply:
	
	cout<<"Answer:\n";
	for (p=0;p<i;p++)
	{
		cout<<"\n";
		for (q=0;q<k;q++)
		{
			for (r=0;r<j;r++)
			{
				c[p][q]+=(a[p][r]*b[r][q]);
			}
			cout<<c[p][q]<<"\t";
		}
	}
}
