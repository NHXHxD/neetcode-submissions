class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {        
        vector<int> tmp;
        dfs(nums, 0, 0, tmp, target);
        return res;

    }
    void dfs(vector<int>nums, int i, int curr, vector<int>& tmp, int target) {
            if (curr == target) {
                res.push_back(tmp);
                return; 
            }
            if (i >= nums.size() || curr > target) {
                return;
            }

            tmp.push_back(nums[i]);
            dfs(nums, i, curr + nums[i], tmp, target);
            tmp.pop_back();
            dfs(nums, i + 1, curr, tmp, target);
        }
};
