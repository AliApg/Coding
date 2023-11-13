#include "iostream"
using namespace std;
float mean(float num,int rep)
{
	float sum,mean;
	sum+=num;
	mean=sum/(rep+1);
	return mean;
}
int main()
{
	int r,i;
	cout<<"How many numbers do you want to enter? ";
	cin>>r;
	float x[r],s=0,y;
	for (i=0;i<r;i++)
	{
		cout<<"Number "<<i+1<<": ";
		cin>>x[i];
		mean(x[i],i);
	}
	cout<<"Average of these "<<r<<" numbers is= "<<mean(x[i],i-1);
}
