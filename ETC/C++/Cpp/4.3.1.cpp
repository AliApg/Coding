#include <iostream>
using namespace std;
int main()
{
	int x,c=1,max;
	cout<<"Num: ";
	cin>>x;
	max=x;
	string line;
		while (getline(cin, line)
		{
			cout<<"Num: ";
			cin>>x;
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
