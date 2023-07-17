/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
static int addTwoNumInt(struct ListNode* l1, struct ListNode* l2, int l2missing) {
	int carry, val;
	
	if (!l1)
		return 0;

	if (l2missing == 0) {
		carry = addTwoNumInt(l1->next, l2->next, 0);
		val = l1->val + l2->val + carry;
	} else {
		carry = addTwoNumInt(l1->next, l2, l2missing - 1);
		val = l1->val + carry;
	}
	l1->val = val % 10;
	return val / 10;
	
}

static int length(struct ListNode* l) {
    int len;
    for (len = 0; l; l = l->next) 
        len++;
    return len;
}

static void swap(struct ListNode** p1, struct ListNode** p2) {
    struct ListNode* tmp;
    tmp = *p1;
    *p1 = *p2;
    *p2 = tmp;
}

#define abs(a) ((a) > 0 ? (a) : -(a))

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
	int len1, len2, carry;
	struct ListNode* head;
	len1 = length(l1);
	len2 = length(l2);
	if (len1 < len2)
		swap(&l1, &l2);
	carry = addTwoNumInt(l1, l2, abs(len1 - len2));
	if (carry) {
		if ((head = malloc(sizeof(struct ListNode))) == NULL)
			return head;
		head->val = 1;
		head->next = l1;
		l1 = head;
	}
	return l1;
}