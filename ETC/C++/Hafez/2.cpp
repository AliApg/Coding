#include <iostream>
using namespace std;

int main()
{
	int n,f1=0,f2=1,f3;
	cout<<"Input N: ";
	cin>>n;
	while (n>0){
	n--;
	cout<<f2<<"\n";
	f3=f1+f2;
	f1=f2;
	f2=f3;
	}
}
