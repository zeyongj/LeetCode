#include <stddef.h>
#include <stdlib.h>

// Definition for singly-linked list.
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };

struct ListNode* reverse_list(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;

    while (curr) {
        struct ListNode* next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }

    return prev;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (!head || k == 1) {
        return head;
    }

    struct ListNode* dummy = (struct ListNode*) malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;
    struct ListNode* prev = dummy;
    struct ListNode* curr = head;
    struct ListNode* tail = dummy;

    int length = 0;
    while (curr) {
        length++;
        curr = curr->next;
    }

    while (length >= k) {
        curr = prev->next;
        tail = prev;
        for (int i = 0; i < k; ++i) {
            tail = tail->next;
        }
        struct ListNode* next_group_start = tail->next;
        tail->next = NULL;

        prev->next = reverse_list(curr);
        curr->next = next_group_start;
        prev = curr;

        length -= k;
    }

    return dummy->next;
}
