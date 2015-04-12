#include <iostream>
using namespace std;
int main()
{
	int n,a,j;
	int dice[200001];
	int sum =0;
	cin >> n >> a;
	for (int i=1;i<=n;i++)
	{
		cin >>dice[i];
		sum += dice[i];
	}
	for (int i=1;i<=n;i++)
	{
		if (a<=sum-dice[i])
			cout << 0 << " ";
		else if (n+dice[i]-1>a)
		{
			cout << a-(n-1)+1 << " ";
		}
		else
		{
			cout << a-(sum-dice[i])-1 << " ";
		}
	}
	cout << endl;
	return 0;
}