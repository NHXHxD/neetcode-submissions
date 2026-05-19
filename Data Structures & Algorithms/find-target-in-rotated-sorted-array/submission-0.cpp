class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (nums[m] < nums[r]) r = m;
            else l = m + 1;
        }
        int result = bin(nums, target, 0, l - 1);
        if (result != -1) return result;
        return bin(nums, target, l, nums.size() - 1);
    }
    int bin(vector<int> nums, int target, int l, int r) {
        while (l <= r) {
            int m = (l + r) / 2;
            if (nums[m] ==  target) return m;
            else if (nums[m] > target) r = m - 1;
            else l = m + 1;
        }
        return -1;
    }
};

