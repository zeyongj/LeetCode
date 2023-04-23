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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) {
            return head;
        }

        ListNode* dummy = new ListNode(0, head);
        ListNode* prev = dummy;
        ListNode* tail = dummy;
        ListNode* curr = head;

        int len = 0;
        while (curr) {
            len++;
            curr = curr->next;
        }

        while (len >= k) {
            curr = prev->next;
            tail = prev;
            for (int i = 0; i < k; ++i) {
                tail = tail->next;
            }
            ListNode* next_group_start = tail->next;
            tail->next = nullptr;

            prev->next = reverseList(curr);
            curr->next = next_group_start;
            prev = curr;

            len -= k;
        }

        return dummy->next;
    }

    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
};
