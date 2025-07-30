#include<iostream>
using namespace std;
int main(){
    int n;
    int arr[100];
    cout<<"Enter the size of array ";
    cin>>n;
    int sum=0;
    for(int i=0;i<n;i++){
        cout<<"Enter element "<<i+1<<" ";
        cin>>arr[i];
        sum+=arr[i];
    }
    
    // for(int i=0;i<n;i++){
    //     sum+=arr[i];
        
    // }
    int ans=0;
    ans=sum/n;
    cout<<"Average is "<<ans;

}