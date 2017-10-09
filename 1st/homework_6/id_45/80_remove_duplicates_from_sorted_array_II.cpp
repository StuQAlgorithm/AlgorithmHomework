//Solution 1
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        if (len == 0)
            return 0;

        map<int, int> res_map;
        for (int i = 0; i < len; ++i) {
            ++res_map[nums[i]]; 
        }

        nums.clear();
        map<int, int>::iterator it;
        for (it = res_map.begin(); it != res_map.end(); ++it) {
            if (it->second > 1) {
                nums.push_back(it->first);
            }
            nums.push_back(it->first);
        }
        return nums.size();
    }
};

//Solution 2
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (k < 2 || nums[i] > nums[k - 2]) 
                nums[k++] = nums[i];
        }
        return k;
    }
};
