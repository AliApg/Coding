#include <iostream>
#include <string>
#include <limits>
using namespace std;
int main()
{
	int x,c=1,max;
	cout<<"Num: ";
	cin.clear();
	cin.ignore(numeric_limits<streamsize>::max());
	cin>>x;
	max=x;
	string line;
		while (getline(cin, line)&&line!="Stop")
		{
			cout<<"Num: ";
			cin>>x;
			line=x;
			if (max==x)
			{
				c++;
			}
			if (x>max)
			{
				max=x;
				c=1;
			}
		}
	cout<<"Max: "<<max<<"\t"<<" repeat: "<<c;
}
