#include <iostream>
using namespace std;
int main()
{
	int n,x,max,min;
	cout<<"Input N: ";
	cin>>n;
	cout<<"Input x: ";
	cin>>x;
	min=x;
	max=x;
		for (n;n>1;n--) {
			if (x>max)
				max=x;
			else if(x<min)
				min=x;
		cout<<"Input x: ";
		cin>>x;
		}
	cout<<"Max= "<<max<<" Min= "<<min;
}
