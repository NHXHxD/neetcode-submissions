class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num: nums) {
            freq[num]++;
        }
        priority_queue<pair<int, int>> pq;
        for (auto [key, val]: freq) {
            pq.push({val, key});
        }
        vector<int> res;
        for (int i = 0; i < k; i++) {
            auto [c, num] = pq.top();
            res.push_back(num);
            pq.pop();
        }
        return res;
    }
};
