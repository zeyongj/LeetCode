/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        int l1Length = 0,
            l2Length = 0;
        
        ListNode tempNode = null,
                 templ1Head = new ListNode(-1),
                 templ2Head = new ListNode(-1);
        
        templ1Head.next = l1;
        templ2Head.next = l2;
        
        tempNode = l1;
        while (tempNode != null)
        {
            l1Length++;
            tempNode = tempNode.next;
        }
        
        tempNode = l2;
        while (tempNode != null)
        {
            l2Length++;
            tempNode = tempNode.next;
        }
        
        while (l1Length > l2Length)
        {
            tempNode = templ2Head.next;
            templ2Head.next = new ListNode(0);
            templ2Head.next.next = tempNode;
            l1Length--;
        }
        
        while (l1Length < l2Length)
        {
            tempNode = templ1Head.next;
            templ1Head.next = new ListNode(0);
            templ1Head.next.next = tempNode;
            l2Length--;
        }
        
        if (AddSingleNumber(templ1Head.next, templ2Head.next) == 1)
        {
            templ1Head.val = 1;
            return templ1Head;
        }
        else
            return templ1Head.next;
    }
    
    private int AddSingleNumber(ListNode node1, ListNode node2)
    {
        int temp = 0;
        
        if (node1.next == null && node2.next == null)
            temp = node1.val + node2.val;
        else
            temp = node1.val + node2.val + AddSingleNumber(node1.next, node2.next);
            
        if (temp >= 10)
        {
            node1.val = temp % 10;
            return 1;
        }
        else
        {
            node1.val = temp;
            return 0;
        }
    }
}