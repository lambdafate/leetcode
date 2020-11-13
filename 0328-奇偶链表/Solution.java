//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode oddTail = head;
        ListNode evenTail = head.next;
        ListNode work = head.next.next;
        boolean odd = true;
        while (work != null) {
            if (odd) {
                ListNode tmp = work;
                evenTail.next = tmp.next;
                work = tmp.next;
                tmp.next = oddTail.next;
                oddTail.next = tmp;
                oddTail = tmp;
            } else {
                evenTail = work;
                work = work.next;
            }
            odd = !odd;
        }
        return head;
    }
}