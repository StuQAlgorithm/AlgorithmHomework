#include <stdio.h>
using namespace std;

/*Definition for singly-linked list.*/
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if ((l1 == NULL) && (l2 == NULL))
            return NULL;
        if (l1 == NULL)
            return l2;
        if (l2 == NULL)
            return l1;

        int sum, carry = 0;
        ListNode *pre_l1, *result;
        result = l1;
        while ((l1 != NULL) && (l2 != NULL)) {
            sum = l1->val + l2->val + carry;
            carry = sum / 10; 
            l1->val = sum % 10;
            pre_l1 = l1; 
            l1 = l1->next;
            l2 = l2->next;
        }

        if (l1 == NULL) {
            l1 = pre_l1;
            l1->next = l2; 
            l1 = l2;
        }

        while (l1 != NULL) {
            sum = l1->val + carry;
            carry = sum / 10;
            l1->val = sum % 10;
            pre_l1 = l1;
            l1 = l1->next;
        }

        if (carry > 0) {
            struct ListNode *last_node = new struct ListNode(carry);
            pre_l1->next = last_node;
        }
        return result;
    }
};

int main()
{
    struct ListNode *test = new ListNode(0);
    test->val = 1;
    test->next = NULL;

    return 0;
}
