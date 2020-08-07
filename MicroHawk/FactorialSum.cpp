#include<iostream>
using namespace std;

long long int fact(int number)
{
    if (number==0) return 1;
    else return number*fact(number-1);
}
void add(long long int prod)
{
    int sum=0;
    while(prod!=0)
    {
        sum=sum + prod%10;
        prod=prod/10;
    }
    cout<<sum<<endl;
    
}
int main() {
    // int n;
    // cin>>n;
    // for(int i=0;i<n;i++)
    // {
    int num;
    cin>>num;
    long long int prod=fact(num);
    add(prod);
    // }
    return 0;
}