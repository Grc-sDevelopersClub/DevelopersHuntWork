// ROMAN TO INTEGERS :) 
//@MICROHAWK 2020;
#include<iostream>
using namespace std;
int value(char roman)
{
    switch (roman)
    {
    case 'I': 
        return 1; 
        break;
    case 'V':
        return 5;
        break;
    case 'X':
        return 10;
        break;
    case 'L':
        return 50;
        break;
    case 'C':
        return 100;
        break;
    case 'D':
        return 500;
        break;
    case 'M':
        return 1000;
        break;
    }
}

int roman_int(string A)
{
    int n, result, current_value;
    n = A.length() - 1;
    for (int i=n; i>=0; i--)
    {
        if(value(A[i]) >= current_value)
        {
            result = result + value(A[i]);
        }
        else
        {
            result = result - value(A[i]);
        }
        current_value = value(A[i]);
    }
    return result;
}

int main()
{
    string r;
    int num;
    cout << "Please enter in UpperCase." << endl;
    cout << "Roman To Int: " << endl;
    cin >> r;
    num = roman_int(r);
    cout << num << endl;
    return 0;
}