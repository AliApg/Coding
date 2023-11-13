#include <iostream>
#include <windows.h>
using namespace std;
int main()
{
	int s,m,h,d,M,y=0;
	while (1)
	{
		for (M;M!=12;M++)
		{
			d=0;
			for (d;d!=30;d++)
			{
				h=0;
				for (h;h!=24;h++)
				{
					m=0;
					for (m;m!=60;m++)
					{
						s=0;
						for (s;s!=60;s++)
						{
							cout<<"Time:\n"<<y<<" Year "<<M<<" Month "<<d<<" Day "<<h<<" Houre "<<m<<" Minute "<<s<<" Second"<<"\n";
							Sleep(1000);
							system("cls");
						}
					}
				}
			}
		}
		y++;
	}
}
