//maxheap: store small half
//minheap: store big half
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<double> result;
        multiset<double> minheap;
        multiset<double> maxheap;

        for (int i = 0; i < n; ++i) {
            if (minheap.size() > 0 && *(minheap.begin()) < nums[i])
                minheap.insert(nums[i]);
            else
                maxheap.insert(nums[i]);

            adjustTwoHeaps(minheap, maxheap);

            if (i >= k - 1) {
                if (minheap.size() == maxheap.size()) {
                    result.push_back((*(minheap.begin()) + *(maxheap.rbegin())) / 2);
                } else {
                    if (minheap.size() > maxheap.size())
                        result.push_back(*(minheap.begin()));
                    else
                        result.push_back(*(maxheap.rbegin()));
                }

                if (minheap.find(nums[i-k+1]) != minheap.end()) {
                    minheap.erase(minheap.find(nums[i-k+1]));
                } else {
                    maxheap.erase(maxheap.find(nums[i-k+1]));
                }
            }
        }
        return result;
    }

    void adjustTwoHeaps(multiset<double>& minheap, multiset<double>& maxheap) {
        while (abs(minheap.size() - maxheap.size()) > 1) {
            if (minheap.size() > maxheap.size()) {
                maxheap.insert(*(minheap.begin()));
                minheap.erase(minheap.begin());
            } else {
                minheap.insert(*(maxheap.rbegin()));
                maxheap.erase((++(maxheap.rbegin())).base());
            }
        }
    }
};
