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
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* prev = dummy;
        
        while (head && head->next){
            ListNode* first_node = head;
            ListNode* second_node = head->next;
            
            prev->next = second_node;
            first_node->next = second_node->next;
            second_node->next = first_node;
            
            prev = first_node;
            head = first_node->next;
        }
        return dummy->next;
    }
};