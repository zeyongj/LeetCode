/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* dummy = (struct ListNode*) malloc(sizeof(struct ListNode));
    dummy->val = -1;
    dummy->next = head;
    struct ListNode* prev = dummy;
    
    while (head && head->next) {
        struct ListNode* first_node = head;
        struct ListNode* second_node = head->next;

        // Swap the nodes
        prev->next = second_node;
        first_node->next = second_node->next;
        second_node->next = first_node;

        // Move to the next pair
        prev = first_node;
        head = first_node->next;
    }
    struct ListNode* new_head = dummy->next;
    free(dummy);
    return new_head;
}