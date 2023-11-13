#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	float a,sum=0;
	for (int i=1;i<1001;i++)
	{
		sum+=i;
	}
	a=1;
	cout<<pow(sum, a/2);
}
