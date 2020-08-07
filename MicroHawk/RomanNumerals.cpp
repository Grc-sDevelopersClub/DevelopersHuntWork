#include<iostream>
#include<limits>
#include<string>
#include<map>
#include<unordered_map>

using namespace std;
// long long int uni(string s) 
// { 
//     // int cnt=0;
//     // for(int i=0;i<10;i++)
//     // {
//     //     string j=to_string(i);
//     //     // bool found = bool(s.find(j)); 
//     //     if (s.find(j) != std::string::npos) 
//     //     {
//     //         cnt++;
//     //     }
//     // }
//     // return cnt;
//     // create a map to store the 
//     // frequency of characters 
//     unordered_map<char, int> m; 
  
//     // traverse the string 
//     for (int i = 0; i < s.length(); i++) { 
//         // increase the frequency of character 
//         m[s[i]]++; 
//     } 
  
//     return m.size(); 
// } 
long long int uni(long long int num)
{
    string str = to_string(num);
    unordered_map<char, int> m; 

    for (int i = 0; i < str.length(); i++) { 
        m[str[i]]++; 
    } 

    return m.size(); 
} 


void roman(int number)
{
    int num[] = {1,4,5,9,10,40,50,90,100,400,500,900,1000}; 
    string sym[] = {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
    int i=12;
    while(number>0)
    {
        int div= number/num[i];
        number=number%num[i];
        while(div--)
        {
            cout<<sym[i];
        }
        i--;
    }
    cout<<endl;
    
}

int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
    long long int number,dist;
    cin>>number;
    // string str=to_string(number);
    // dist=uni(str);
    dist=uni(number);
    roman(dist);
    cout<<dist<<endl;
    }
    return 0;
}


