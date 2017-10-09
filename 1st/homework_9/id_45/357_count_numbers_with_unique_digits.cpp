class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int digit_choice_cnt[10] = {9, 9, 8, 7, 6, 5, 4, 3, 2, 1};
        n = n > 10? 10 : n;
        int result = 1, s = 1;
        for (int i = 0; i < n; ++i) {
            s *= digit_choice_cnt[i];
            result += s;
        }
        return result;
    }
};
