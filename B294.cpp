#include <iostream>
using namespace std;
int main()
{
    int n,i,j,tt;
    long a,b,c;
    a=0;
    b=0;
    c=0;
    cin >> n;
    for (i=0;i<n;i++)
    {
        cin >> tt;
        a += tt;
    }
    for (i=0;i<n-1;i++)
    {
        cin >> tt;
        b += tt;
    }
    for (i=0;i<n-2;i++)
    {
        cin >> tt;
        c += tt;
    }
    cout << a-b << endl;
    cout << b-c << endl;
}
