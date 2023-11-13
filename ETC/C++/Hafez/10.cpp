#include "iostream"
#include "cstring"
#include "windows.h"
using namespace std;
int main()
{
	system("cls");
	int s,g,x,i=0,j,c;
	cout<<"\aEnter number of students: ";
	cin>>s;
	cout<<"Enter number of grades per student: ";
	cin>>g;
	system("cls");
	float a[s][g+4],ar[s][g],b[s*g],sum,min,max;
//	Students name:
	char A[s][100];
	string N;
	gets(A[i-1]);
	while (i<s)
	{
		cout<<"Student number "<<i+1<<" name: ";
		gets(A[i]);
		i++;
	}

//	Input:
	for (i=0;i<s;i++)
	{
		system("cls");
		sum=0;
		cout<<"Student number "<<i+1<<" ( "<<A[i]<<" ):\n";
		for (j=0;j<g;j++)
		{
			cout<<"Grade "<<j+1<<": ";
			cin>>a[i][j];
			if (a[i][j]<0||a[i][j]>20)
			{
				cout<<"Enter a number between 0 and 20\a\n";
				j--;
				continue;
			}
			sum+=a[i][j];
		}
		a[i][j]=sum;
		a[i][j+1]=sum/g;
	}
	do
	{
		system("cls");
		cout<<"Menu:\n\n1: Sum of each student grades\n2: Sum of these "<<s<<
		" students grades\n3: Mean of each student grades\n4: Mean of these "<<s
		<<" students grades\n5: Lowest grade of each student\n6: Lowest grade"
		" between these "<<s<<" students\n7: Highest grade of each student\n8:"
		" Highest grade between these "<<s<<" students\n9: Odd grades\n10: Even"
		" grades\n11: Raw grades\n12: Sorted grades for each of these students\n"
		"13: Sorted grades of all of these "<<s<<" students\n14: Info for an spe"
		"cific student\n15: Exit program!\n\n";
		cin>>x;
		system("cls");
		switch (x)
		{
//	Original:
			case 11:
				for (i=0;i<s;i++)
				{
					cout<<"Student number "<<i+1<<" ( "<<A[i]<<" ) grades:\n";
					for (j=0;j<g;j++)
					{
						cout<<a[i][j]<<"\t";
					}
					cout<<"\n\n";
				}
				system("pause");
				break;
//	Overall sum:
			case 2:
				sum=0;
				j=g;
				for (i=0;i<s;i++)
				{
					sum+=a[i][j];
				}
				cout<<"Overall sum of these "<<s<<" students grades is "<<sum<<"\n\n";
				system("pause");
				break;
//	Overall mean:
			case 4:
				sum=0;
				j=g;
				for (i=0;i<s;i++)
				{
					sum+=a[i][j+1];
				}
				cout<<"Overall mean of these "<<s<<" students grades is "<<sum/s<<"\n\n";
				system("pause");
				break;
//	Sum of each student:
			case 1:
				for (i=0;i<s;i++)
				{
					j=g;
					cout<<"Sum of student number "<<i+1<<" ( "<<A[i]<<" ) grades is "<<a[i][j]<<"\n";
				}
				cout<<"\n";
				system("pause");
				break;
//	Mean of each student:
			case 3:
				for (i=0;i<s;i++)
				{
					j=g;
					cout<<"Mean of student number "<<i+1<<" ( "<<A[i]<<" ) grades is "<<a[i][j+1]<<"\n";
				}
				cout<<"\n";
				system("pause");
				break;
//	Lowest grade for each student:
			case 5:
				for (i=0;i<s;i++)
				{
					a[i][g+2]=a[i][0];
					for (j=1;j<g;j++)
					{
						if (a[i][j]<a[i][g+2])
						{
							a[i][g+2]=a[i][j];
						}
					}
				}
				for (i=0;i<s;i++)
				{
					cout<<"Lowest grade of student number "<<i+1<<" ( "<<A[i]<<" ) is "<<a[i][g+2]<<"\n";
				}
				cout<<"\n";
				system("pause");
				break;
//	Highest grade for each student:
			case 7:
				for (i=0;i<s;i++)
				{
					a[i][g+3]=a[i][0];
					for (j=1;j<g;j++)
					{
						if (a[i][j]>a[i][g+3])
						{
							a[i][g+3]=a[i][j];
						}
					}
				}
				for (i=0;i<s;i++)
				{
					cout<<"Highest grade of student number "<<i+1<<" ( "<<A[i]<<" ) is "<<a[i][g+3]<<"\n";
				}
				cout<<"\n";
				system("pause");
				break;
//	Lowest grade overall:
			case 6:
				min=a[0][0];
				for (i=0;i<s;i++)
				{
					for (j=0;j<g;j++)
					{
						if (a[i][j]<min)
						{
							min=a[i][j];
						}
					}
				}
				cout<<min<<" is the lowest grade between these "<<s<<" students and it belonges to:\n";
				for (i=0;i<s;i++)
				{
					for (j=0;j<g;j++)
					{
						if (a[i][j]==min)
						{
							cout<<"Grade "<<j+1<<" of student number "<<i+1<<" ( "<<A[i]<<" )\n";
						}
					}
				}
				cout<<"\n";
				system("pause");
				break;
//	Highest grade overall:
			case 8:
				max=a[0][0];
				for (i=0;i<s;i++)
				{
					for (j=0;j<g;j++)
					{
						if (a[i][j]>max)
						{
							max=a[i][j];
						}
					}
				}
				cout<<max<<" is the highest grade between these "<<s<<" students and it belonges to:\n";
				for (i=0;i<s;i++)
				{
					for (j=0;j<g;j++)
					{
						if (a[i][j]==max)
						{
							cout<<"Grade "<<j+1<<" of student number "<<i+1<<" ( "<<A[i]<<" )\n";
						}
					}
				}
				cout<<"\n";
				system("pause");
				break;
//	Odd grades:
			case 9:
				c=0;
				for (i=0;i<s;i++)
				{
					for (j=0;j<g;j++)
					{
						if ((int)a[i][j]%2!=0&&a[i][j]!=0)
						{
							cout<<"Grade "<<j+1<<" of student number "<<i+1<<" ( "<<A[i]<<" ) is an odd number: "<<a[i][j]<<"\n";
							c++;
						}
					}
				}
				cout<<"\nThere is "<<c<<" odd grades in total.\n\n";
				system("pause");
				break;
//	Even grades:
			case 10:
			c=0;
				for (i=0;i<s;i++)
				{
					for (j=0;j<g;j++)
					{
						if ((int)a[i][j]%2==0&&a[i][j]!=0)
						{
							cout<<"Grade "<<j+1<<" of student number "<<i+1<<" ( "<<A[i]<<" ) is an even number: "<<a[i][j]<<"\n";
							c++;
						}
					}
				}
				cout<<"\nThere is "<<c<<" even grades in total.\n\n";
				system("pause");
				break;
//	Sorting each student grades:
			case 12:
				for (i=0;i<s;i++)
				{
					for (j=0;j<g;j++)
					{
						ar[i][j]=a[i][j];
					}
				}
				for (i=0;i<s;i++)
				{
					for (c=1;c<g;c++)
					{
						for (j=0;j<g-1;j++)
						{
							if (ar[i][j]>ar[i][j+1])
							{
								ar[i][j+1]+=ar[i][j];
								ar[i][j]=ar[i][j+1]-ar[i][j];
								ar[i][j+1]-=ar[i][j];
							}	
						}
					}
				}
				for (i=0;i<s;i++)
				{
					cout<<"Student number "<<i+1<<" ( "<<A[i]<<" ) sorted grades:\n";
					for (j=0;j<g;j++)
					{
						cout<<ar[i][j]<<"\t";
					}
					cout<<"\n\n";
				}
				system("pause");
				break;
//	Sorting all grades:
			case 13:
				c=0;
				for (i=0;i<s;i++)
				{
					for (j=0;j<g;j++,c++)
					{
						b[c]=a[i][j];
					}
				}
				for (i=1;i<s*g;i++)
				{
					for (j=0;j<(s*g)-1;j++)
					{
						if (b[j]>b[j+1])
						{
							b[j+1]+=b[j];
							b[j]=b[j+1]-b[j];
							b[j+1]-=b[j];
						}	
					}
				}
				cout<<"Sorted grades:\n\n";
				for (i=0;i<s*g;i++)
				{
					cout<<b[i]<<"\t";
				}
				cout<<"\n\n";
				system("pause");
				break;
//	Student info:
			case 14:
				cout<<"Name of the student you want info for: ";
				getline (cin, N);
				getline (cin, N);
				for (i=0;i<s;i++)
				{
					if (A[i]==N)
					{
						cout<<A[i]<<" grades are:\n";
						for (j=0;j<g;j++)
						{
							cout<<a[i][j]<<"\t";
						}
						a[i][g+2]=a[i][0];
						for (j=1;j<g;j++)
						{
							if (a[i][j]<a[i][g+2])
							{
								a[i][g+2]=a[i][j];
							}
						}
						a[i][g+3]=a[i][0];
						for (j=1;j<g;j++)
						{
							if (a[i][j]>a[i][g+3])
							{
								a[i][g+3]=a[i][j];
							}
						}
						cout<<"\n\nSum of "<<N<<" grades is: "<<a[i][g];
						cout<<"\n\nMean of "<<N<<" grades is: "<<a[i][g+1];
						cout<<"\n\nLowest grade of "<<N<<" is: "<<a[i][g+2];
						cout<<"\n\nHighest grade of "<<N<<" is: "<<a[i][g+3]<<"\n\n";
						for (j=0;j<g;j++)
						{
							ar[i][j]=a[i][j];
						}
						for (c=1;c<g;c++)
						{
							for (j=0;j<g-1;j++)
							{
								if (ar[i][j]>ar[i][j+1])
								{
									ar[i][j+1]+=ar[i][j];
									ar[i][j]=ar[i][j+1]-ar[i][j];
									ar[i][j+1]-=ar[i][j];
								}	
							}
						}
						c=0;
						for (j=0;j<g;j++)
						{
							if ((int)a[i][j]%2!=0&&a[i][j]!=0)
							{
								cout<<"Grade "<<j+1<<" is an odd number: "<<a[i][j]<<"\n";
								c++;
							}
						}
						cout<<"\n"<<A[i]<<" has "<<c<<" odd grades in total.\n\n";
						c=0;
						for (j=0;j<g;j++)
						{
							if ((int)a[i][j]%2==0&&a[i][j]!=0)
							{
								cout<<"Grade "<<j+1<<" is an even number: "<<a[i][j]<<"\n";
								c++;
							}
						}
						cout<<"\n"<<A[i]<<" has "<<c<<" even grades in total.\n\n";
						cout<<A[i]<<"'s sorted grades:\n";
						for (j=0;j<g;j++)
						{
							cout<<ar[i][j]<<"\t";
						}
						cout<<"\n\n";
						break;
					}
				}
				if (i==s)
				{
					cout<<N<<" wasn't in the students list!\a\n\n";
				}
				system("pause");
				break;
//	Exit:
			case 15:
				cout<<"Thank you for using this program! :)\n\n";
				Sleep(3000);
				break;
//	Wrong input:
			default:
				cout<<"Wrong input; Please enter a number between 1 and 15 from the menu below\a\n\n";
				system("pause");
				break;	
		}
	}
	while (x!=15);
}
