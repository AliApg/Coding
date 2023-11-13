#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int c=0,i;
	char a[1];
	char str[100];
	cout<<"Input your characters: ";
	cin>>str;
	cout<<"Input the character you want to find : ";
	cin>>a;
	for (i=0;i<strlen(str);i++)
		{
			if (a[0]==str[i])
				c++;
		}
	if (c==0)
	{
		cout<<"There was no '"<<a[0]<<"' in your input characters!";
	}	
	else
	{
		cout<<"'"<<a[0]<<"' was repeated "<<c<<" times!";
	}
}
