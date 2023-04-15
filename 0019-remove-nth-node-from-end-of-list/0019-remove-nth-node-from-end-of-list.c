/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* dummy = (struct ListNode*) malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;
    struct ListNode* first = dummy;
    struct ListNode* second = dummy;

    // Move first pointer n nodes ahead in the linked list
    for (int i = 0; i < n + 1; i++) {
        first = first->next;
    }

    // Move first to the end, maintaining the gap
    while (first != NULL) {
        first = first->next;
        second = second->next;
    }

    // Skip the desired node
    struct ListNode* nodeToRemove = second->next;
    second->next = second->next->next;

    // Free the removed node memory
    free(nodeToRemove);

    // Return the new head node
    struct ListNode* newHead = dummy->next;
    free(dummy);
    return newHead;
}