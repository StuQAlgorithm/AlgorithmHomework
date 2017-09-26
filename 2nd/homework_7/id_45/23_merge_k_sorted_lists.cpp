/**
 *  * Definition for singly-linked list.
 *  * struct ListNode {
 *  *     int val;
 *  *     ListNode *next;
 *  *     ListNode(int x) : val(x), next(NULL) {}
 *  * };
 *  */
//Solution 1: O(n*k*k)
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0)
            return NULL;
        if (lists.size() == 1)
            return lists[0];
        int n = lists.size();
        ListNode head(0);
        ListNode *p, *l1, *l2;
        p = &head;
        l1 = lists[0];
        for (int i = 1; i < n; ++i) {
            l2 = lists[i];
            while (l1 && l2) {
                if (l1->val < l2->val) {
                    p->next = l1;
                    l1 = l1->next;
                } else {
                    p->next = l2;
                    l2 = l2->next;
                }
                p = p->next;
            }
            p->next = !l1? l2 : l1;
            p = &head;
            l1 = p->next;
        }
        return head.next;
    }
};

//Solution 2: priority queue, O(n*k*log(k))
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0)
            return NULL;
        if (lists.size() == 1)
            return lists[0];
        int n = lists.size();
        ListNode head(0);
        ListNode *p = &head;
        multimap<int, ListNode*> mulmap;
        multimap<int, ListNode*>::iterator it ;
        for (int i = 0; i < n; ++i) {
            if (lists[i])
                mulmap.insert(pair<int, ListNode*>(lists[i]->val, lists[i]));
        }
        while (!mulmap.empty()) {
            it = mulmap.begin();
            p->next = it->second;
            p = p->next;
            if (it->second->next)
                mulmap.insert(pair<int, ListNode*>(it->second->next->val, it->second->next));

            mulmap.erase(it);
        }
        return head.next;
    }
};
