#include <iostream>
#include <vector>

using namespace std;
int pivotIndex(vector<int>& nums) {
    int right_sum = 0, left_sum = 0;
    for(int i = 0; i<nums.size(); i++){
        right_sum += nums[i];
    }
 for(int i = 0; i<nums.size(); i++){
        if(left_sum == right_sum - left_sum-nums[i])
            return i;
        left_sum += nums[i];
    }
    return -1;

    }
int main(){
    int length, num;
    cout<<"How many numbers?"<<endl;
    cin>>length;
    vector<int> nums;
    for(int i = 0; i < length; i++){
        cin>>num;
        nums.push_back(num);
    }
    cout<<nums.size()<<endl;

    cout<<pivotIndex(nums)<<endl;


    return 0;
}
