#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	char a[20],R[20],S[20],B[20];
	cout<<"Enter your name: ";
	gets(a);
//	cout<<sizeof(S)<<"\n"<<sizeof(B)<<"\n"<<sizeof(R)<<"\n";
	for (int i=0;a[i];i++)
	{
//		cout<<b<<"\n";
		if (a[i]>='A'&&a[i]<='Z'){
			R[i]=a[i]+32;
			S[i]=a[i]+32;
			B[i]=a[i];
		}else if (a[i]>='a'&&a[i]<='z'){
			R[i]=a[i]-32;
			S[i]=a[i];
			B[i]=a[i]-32;
		}else if (a[i]==' '){
			R[i]=a[i];
			S[i]=a[i];
			B[i]=a[i];
		}/*else
		cout<<"Wrong input!";*/
	}
//	for (int i=0;B[i];i++)
//	{
//		cout<<B[i];
//	}
//	cout<<"\n";
//	for (int i=0;S[i];i++)
//	{
//		cout<<S[i];
//	}
//	cout<<"\n";
//	for (int i=0;R[i];i++)
//	{
//		cout<<R[i];
//	}
	cout<<S<<"\n"<<B<<"\n"<<R;
//	cout<<"\n"<<strlen(a)<<"\n"<<strlen(S)<<"\n"<<strlen(B)<<"\n"<<strlen(R);
}
