/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//Solution 1
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head)
            return NULL;

        bool hasCycle = false;
        ListNode *walk = head;
        ListNode *run = head;
        ListNode *result = NULL;

        if (run->next) {
            if (run == run->next)
                return run;
            else 
                run = run->next;
        } else {
            return result;
        }

        walk->val = INT_MIN;
        while (walk && run) {
            walk = walk->next;
            if (run->next) {
                run = run->next->next;
            }
            if (walk == run)
                hasCycle = true;

            if (walk) {
                if (walk->val == INT_MIN) {
                    result = walk;
                    break;
                } else {
                    walk->val = INT_MIN;
                }
            }
        }
        return result;
    }
};

//Solution 2
/*
 * L1: the distance between start point and entry point of the cycle
 * L2: the distance between entry point and meeting point
 * CL: the length of cycle
 * because walk one step and run two steps each time, so that we can 
 * conclude: 2 * (L1 + L2) = L1 + L2 + n * CL ==>
 * L1 = (n - 1) * CL + CL - L2
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next)
            return NULL;

        bool hasCycle = false;
        ListNode *walk = head;
        ListNode *run = head;
        ListNode *result = NULL;

        while (run->next && run->next->next) {
            walk = walk->next;
            run = run->next->next;
            if (walk == run) {
                hasCycle = true;
                break;
            }
        }
        if (hasCycle) {
            result = head;    
            while (result != walk) {
                result = result->next;
                walk = walk->next;
            }
        }
        return result;
    }
};
