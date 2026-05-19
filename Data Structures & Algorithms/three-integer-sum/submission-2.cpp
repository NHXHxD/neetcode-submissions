class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        set<vector<int>> trips;
        for (int i = 0; i < n;i++) {
            unordered_set<int> numSet;
            for (int j = i + 1; j < n;j++) {
                int target = -1 * (nums[i] + nums[j]);
                if (numSet.find(target) != numSet.end()) {
                    vector<int> trip = {nums[i], nums[j], target};
                    sort(trip.begin(), trip.end());
                    trips.insert(trip);                
                    }

                numSet.insert(nums[j]);
            }

        }
        vector<vector<int>> res(trips.begin(), trips.end());
        return res;
    
    }
};
