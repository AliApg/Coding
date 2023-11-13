#include <iostream>
using namespace std;

int main(){
	int r1,c1,c2;
	cout<<"Enter row for first matrix \n";
	cin>>r1;
	cout<<"Enter column for first matrix \n";
	cin>>c1;
	cout<<"Enter column for first matrix \n";
	cin>>c2;
		int a[r1][c1],b[c1][c2],c[r1][c2];//r1=2,c1=3;r2=3;c2=2;
		cout<<"Enter Elements of First Matrix \n";
		for(int i=0;i<r1;i++){
			for(int j=0;j<c1;j++){
				cin>>a[i][j];
			}	
		}
		cout<<"Enter Elements of Second Matrix \n";
		for(int i=0;i<c1;i++){
			for(int j=0;j<c2;j++){
				cin>>b[i][j];
			}	
		}
		for(int i=0;i<c2;i++){
			for(int j=0;j<r1;j++){
				c[i][j]=0;				
			}	
		}		
		for(int i=0;i<c2;i++){
			for(int j=0;j<r1;j++){
				for(int k=0;k<c1;k++){
					c[i][j]+=a[i][k]*b[k][j];
				}	
				cout<<c[i][j]<<"\t \n";
			}
		}
}
