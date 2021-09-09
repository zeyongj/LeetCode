/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* cursor = head;
        ListNode* temp;
        while(cursor != NULL)
        {
            temp = cursor->next;
            cursor->next = prev;
            prev = cursor;
            cursor = temp;
        }
        return prev;
}
};
