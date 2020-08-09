#include<bits/stdc++.h>
#include<vector>
using namespace std;
int main()
{
    vector<int>v1;
    //assign the vector with 5 times 50
    v1.assign(5,50);
    cout<<"After assign the vector is: ";
    for(int i=0;i<v1.size();i++)
    {
        //v1.size() will return size of vector
        cout<<v1[i]<<" ";
    }
    cout<<"\n";
    //====================================================================================//
    
    //insert 100 at the last of the vector
    //using push_back()
    v1.push_back(100);
    int n=v1.size();
    cout<<"The last element of the vector right now is: "<<v1[n-1]<<" and size: "<<n<<"\n";
    
    //====================================================================================//
    
    //delete the last element of the vector
    //using pop_back()
    v1.pop_back();
    n=v1.size();
    cout<<"After removing the size of vector is "<<n<<" & last element is "<<v1[n-1]<<"\n";
    
    //====================================================================================//
    
    //insert 70 at the front of the vector
    //using insert()
    v1.insert(v1.begin(),70);
    cout<<"After inserting at begining the front value is: "<<v1[0]<<"\n";
    
    //======================================================================================//
    
    //remove the first element using erase
    v1.erase(v1.begin());
    cout<<"After inserting at begining the front value is: "<<v1[0]<<"\n";
    
    //=====================================================================================//
    
    //swap first and last element of the vector
    //using swap()
    n=v1.size();
    cout<<"Before swapping the fisrt value is "<<v1[0]<<" last value: "<<v1[n-1]<<"\n";
    swap(v1[0],v1[n-1]);
    cout<<"After swapping the fisrt value is "<<v1[0]<<" last value: "<<v1[n-1]<<"\n";
    
    //======================================================================================//
    
    //insert element at front using emplace()
    v1.emplace(v1.begin(),12);
    v1.emplace(v1.begin(),12);
    cout<<"After inserting at begining the front value is: "<<v1[0]<<"\n";
    
    //=======================================================================================//
    
    //insert element at the back of the vector
    //using emplace_back()
    v1.emplace_back(60);
    n=v1.size();
    cout<<"After inserting at back of the back value is: "<<v1[n-1]<<"\n";
    
    //========================================================================================//
    
    //clear all the element of the vector
    v1.clear();
    n=v1.size();
    cout<<"After clearing the size of vector is: "<<n<<"\n";
    
    //================================================================================================//
    return 0;
}
