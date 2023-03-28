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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL) 
            return NULL;
        if (head->next == NULL) 
            return head;

        ListNode* old_tail = head;
        int n;
        for(n = 1; old_tail->next != NULL; n++)
            old_tail = old_tail->next;
        old_tail->next = head;

        ListNode* new_tail = head;
        for (int i = 0; i < n - k % n - 1; i++)
          new_tail = new_tail->next;
        ListNode* new_head = new_tail->next;

        new_tail->next = NULL;

        return new_head;
    }
};