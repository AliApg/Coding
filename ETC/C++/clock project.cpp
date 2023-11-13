#include <iostream>
#include <windows.h>
using namespace std;
int main()
{
 	int sec=0,min=0,hour=0,day=0,month=0,year=0;
	while(1)
	{
		if(sec>=60)
		{
			sec=0;
			min++;
				if(min>59)
				{
					min=0;
					hour++;
						if(hour>23)
						{
							hour=0;
							day++;
								if(day>30)
								{
									day=0;
									month++;
										if(month>12)
										{
											month=0;
											year++;
										}
								}
						}
				}
		}
		system("cls");
		cout<<year<<" : "<<month<<" : "<<day<<" : "<<hour<<" : "<<min<<" : "<<sec<<"\n\nYear: "<<year
		<<"\nMonth: "<<month<<"\nDay: "<<day<<"\nHour: "<<hour<<"\nMinute: "<<min<<"\nSecond: "<<sec<<"\n";
		sec++;
		Sleep(1000);
	}
 }
