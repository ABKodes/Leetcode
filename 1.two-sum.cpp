/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int result [2];
        for (int i=0; i<nums.size(); i++)
            for (int j = i+1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target){
                    result[0] = i;
                    result[1] = j;
                }
            }
        return vector<int> (result, result+2);
    }
};
// @lc code=end

