//Solution 1: TLE
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int a, c;
        map<int,int> record;
        map<int,int>::iterator map_it;
        vector<vector<int> > result;
        set<multiset<int> > result_set;
        set<multiset<int> >::iterator set_it;

        if (nums.size() < 3)
            return result;

        for (int i = 0; i < nums.size() - 2; ++i) {
            c = nums[i];
            record.clear();
            for (int j = i + 1; j < nums.size(); ++j) {
                a = -c - nums[j];
                map_it = record.find(a);
                if (map_it != record.end()) {
                    if (map_it->second == 0) {
                        multiset<int> set_element;
                        set_element.insert(a);
                        set_element.insert(c);
                        set_element.insert(nums[j]);
                        result_set.insert(set_element);

                        record[a] = 1;
                        record[nums[j]] = 1;
                    }
                } else {
                    record[nums[j]] = 0;
                }
            }
        }

        for (set_it = result_set.begin(); set_it != result_set.end(); ++set_it) {
            vector<int> vec((*set_it).begin(), (*set_it).end());
            result.push_back(vec);
        }

        return result;
    }
};

//Solution 2
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int l, r, c;
        vector<vector<int> >result;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size();) {
            c = nums[i];
            l = i + 1;
            r = nums.size() - 1;
            while (l < r) {
                if (nums[l] + nums[r] > -c) {
                    --r;
                } else if(nums[l] + nums[r] < -c) {
                    ++l;
                } else {
                    vector<int> vec;
                    vec.push_back(c);
                    vec.push_back(nums[l]);
                    vec.push_back(nums[r]);
                    result.push_back(vec);

                    int l_val = nums[l];
                    ++l;
                    while (l < r) {
                        if (l_val == nums[l]) {
                            ++l;
                        } else {
                            break;
                        }
                    }

                    int r_val = nums[r];
                    --r;
                    while (l < r) {
                        if (r_val == nums[r]) {
                            --r;
                        } else {
                            break;
                        }
                    }
                }
            }       
            ++i;
            while (i < nums.size()) {
                if (c == nums[i]) {
                    ++i;
                } else {
                    break;
                }
            }
        }
        return result;
    }
};
