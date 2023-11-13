#include <iostream>
#include <windows.h>
using namespace std;
int main()
{
	int s=0,m=0,h=0,d=0,M=0,y=0;
	while(1)
	{
		if (s!=60)
		{
			cout<<"Time:\n"<<y<<" Year "<<M<<" Month "<<d<<" Day "<<h<<" Houre "<<m<<" Minute "<<s<<" Second"<<"\n";
			Sleep(1000);
			system("cls");
			s++;
		}else if (s==60){
				m++;
				s=0;
		}
		if (m==60)
		{
			h++;
			m=0;
		}
		if (h==24)
		{
			d++;
			h=0;
		}
		if (d==30)
		{
			M++;
			d=0;
		}
		if (M==12)
		{
			y++;
			M=0;
		}
	}
}
