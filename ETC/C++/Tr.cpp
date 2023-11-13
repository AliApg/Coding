#include <iostream>
using namespace std;
int main()
{
	int i;
	float b[32],a[32]={20,21,30,32,51.1,51.2,96,100,106,127,130,148,158,159.2,171.2,172,178,182,184,192,300,341,360,342,346,349,366,368,375,377,379,380};
	for (int i=0;i<32;i++)
	{
		cout<<"pic "<<i+1<<":\t";
		cin>>b[i];
	}
	for (int j=0;j<32;j++)
	{
		for (i=0;i<32;i++)
		{
			if (b[j]==a[i])
			break;
		}
		if (i==32)
		cout<<b[j]<<" was not found!\n";
	}
}
