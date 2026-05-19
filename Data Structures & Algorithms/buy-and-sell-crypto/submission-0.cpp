class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int curr = INT_MAX;
        for (int price: prices) {
            if (curr == INT_MAX) {
                curr = price;
                continue;
            }
            if (price > curr) res = max(res, price - curr);
            else if (price < curr) curr = price;

        }
        return res;
    }
};
