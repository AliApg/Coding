#include "iostream"
using namespace std;
int main()
{
	int y,m,d,by,bm,bd,fy,fm,fd;
	
//	Today

	cout<<"Current date\n\n";
	while (1)
	{
		cout<<"Year: ";
		cin>>y;
		if (y<0)
		{
			cout<<"Year cannot be a negative number!\n";
			continue;
		}
		break;
	}
	while (1)
	{
		cout<<"Month: ";
		cin>>m;
		if (m<1||m>12)
		{
			cout<<"Month must be between 1 & 12\n";
			continue;
		}
		break;
	}
	while (1)
	{
		cout<<"Day: ";
		cin>>d;
		if (m<7&&(d<1||d>31))
		{
			cout<<"Day must be between 1 & 31\n";
			continue;
		}
		if (m>6&&(d<1||d>30))
		{
			cout<<"Day must be between 1 & 30\n";
			continue;
		}
		break;
	}
	
//	Birthday

	cout<<"\nYour birth date\n\n";
	while (1)
	{
		cout<<"Year: ";
		cin>>by;
		if (by>y)
		{
			cout<<"Your birt year cannot be greater than current year!\n";
			continue;
		}
		if (by<0)
		{
			cout<<"Year cannot be a negative number!\n";
			continue;
		}
		break; 
	}
	while (1)
	{
		cout<<"Month: ";
		cin>>bm;
		if (bm<1||bm>12)
		{
			cout<<"Month must be between 1 & 12\n";
			continue;
		}
		if (by==y&&bm>m)
		{
			cout<<"Your birth month cannot be greater than current month!\n";
			continue;
		}
		break;
	}
	while (1)
	{
		cout<<"Day: ";
		cin>>bd;
		if (bm<7&&(bd<1||bd>31))
		{
			cout<<"Day must be between 1 & 31\n";
			continue;
		}
		if (bm>6&&(bd<1||bd>30))
		{
			cout<<"Day must be between 1 & 30\n";
			continue;
		}
		if (by==y&&bm==m&&bd>d)
		{
			cout<<"Your birth day cannot be greater than current day!\n";
			continue;
		}
		break;
	}
	
//	Fuck fest

	fy=y-by;
	if (m<bm)
	{
		fy--;
		fm=m+12-bm;
	}
	else
	{
		fm=m-bm;
	}
	if (d<bd&&bm<7)
	{
		fm--;
		fd=d+31-bd;
	}
	else if (d<bd&&bm>6)
	{
		fm--;
		fd=d+30-bd;
	}
	else
	{
		fd=d-bd;
	}

//	Display

	system("cls");
	cout<<"Current date: "<<y<<"/"<<m<<"/"<<d<<"\nYour birth date: "
	<<by<<"/"<<bm<<"/"<<bd;
	if(fy!=0||fm!=0||fd!=0)
	{
		cout<<"\n\nYou are ";
		if (fy==0)
		{
		}
		else if (fy==1)
		{
			cout<<fy<<" year ";
		}
		else
		{
			cout<<fy<<" years ";
		}
		if (fm==0)
		{
		}
		else if (fm==1)
		{
			cout<<fm<<" month ";
		}
		else
		{
			cout<<fm<<" monthes ";
		}
		if (fd==0)
		{
		}
		else if (fd==1)
		{
			cout<<"& "<<fd<<" day ";
		}
		else
		{
			cout<<"& "<<fd<<" days ";
		}
		cout<<"old";
	}
	else
	{
		cout<<"\nGo fuck yourself!\n     ||\n     ||\n     ||"
		"\n  |||||||||\n||||||||||||\n ||||||||||\n  ||||||||";
	}	
}
