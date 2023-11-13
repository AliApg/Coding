#include <iostream>
using namespace std;

int main()
{
	int x;
	cout<<"Input a double diget number: ";
	cin>>x;
	if (x/10<1||x/10>=10){
	cout<<x<<" is not a double diget number: ";
	} else {
	cout<<x/10+x%10;
	}
}


/*
{
	int time;
	cout<<"Enter time: ";
	cin>>time;
	string result= (time<18)?"Good day":"Good evening";
	cout<<result;
}
*/
