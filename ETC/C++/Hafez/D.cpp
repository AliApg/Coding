#include <iostream>
#include <windows.h>
using namespace std;
int main()
{
	int s=0,m=0,h=0;
	while (1)
	{
		if (s==60)
		{
			s=0;
			m++;
		}
		else if (m>59)
		{
			m=0;
			h++;
		}
		cout<<h<<"\t"<<m<<"\t"<<s<<" \r";
		s++;
		Sleep(1000);
	}
}
