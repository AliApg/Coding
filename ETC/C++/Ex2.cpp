#include "iostream"
using namespace std;
float mean(float sum,int rep)
{
	return sum/rep;
}
int main()
{
	int r,i;
	cout<<"How many numbers do you want to enter? ";
	cin>>r;
	float x[r],s=0;
	for (i=0;i<r;i++)
	{
		cout<<"Number "<<i+1<<": ";
		cin>>x[i];
		s+=x[i];
	}
	cout<<"Average of these "<<r<<" numbers is= "<<mean(s,r);
}
