#include <iostream>
using namespace std;
int main()
{
	int x,c=0,max;
	cout<<"Num: ";
	cin>>x;
	max=x;
		while (x!=0)
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
				c=0;
			}
			/*else if (x>!max||x<=!max)
			{
				break;
			}*/
		}
	cout<<"Max: "<<max<<"\t"<<" repeat: "<<c+1;
}
