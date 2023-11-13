#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int p=0,s=0;
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
			s++;
		}else if (a[i]=='.'){
			p++;
		}
		else
		cout<<"Wrong input!";
	}
	cout<<S<<"\n"<<B<<"\n"<<R<<"\n"<<"Points: "<<p<<"\n"<<"Spaces: "<<s;
//	cout<<"\n"<<strlen(a)<<"\n"<<strlen(S)<<"\n"<<strlen(B)<<"\n"<<strlen(R);
}
