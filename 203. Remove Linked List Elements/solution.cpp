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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode dummy{0};
        dummy.next = head;
        ListNode* curr = &dummy;
        while (curr) {
        ListNode* next = curr->next;
        while (next && next->val == val) 
            next = next->next;
        curr->next = next;
        curr = next;
        }
        return dummy.next;
    }
};
