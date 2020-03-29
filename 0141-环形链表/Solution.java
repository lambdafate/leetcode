class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow=head, fast=head;
        if(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        while(fast != null && fast.next != null){
            if(fast == slow || fast.next == slow){
                return true;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return false;
    }
}