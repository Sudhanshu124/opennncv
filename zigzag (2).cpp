#include<iostream>
using namespace std;
int main()
{
	int i,j,n;
	cin>>n;
	int a[n][n];
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			cin>>a[i][j];
		}
	}
	for(i=0;i<n;i++)
	{
		if(i==0||i%2==0)
		{
			for(j=n-1;j>=0;j--)
			{
				cout<<a[i][j]<<" ";
			}cout<<"\n";
		}
		else
		{
			for(j=0;j<n;j++)
			{
				cout<<a[i][j]<<" ";
			}cout<<"\n";
		}
	}
}
