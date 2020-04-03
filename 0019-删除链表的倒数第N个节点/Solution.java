class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode prev = head;
        ListNode fast = prev.next;
        while (n > 0 && fast != null) {
            fast = fast.next;
            n--;
        }
        if (n != 0) {
            return head.next;
        }
        while (fast != null) {
            prev = prev.next;
            fast = fast.next;
        }
        prev.next = prev.next.next;
        return head;
    }
}