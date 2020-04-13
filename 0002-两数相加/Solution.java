class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {   
        int fbi = 0;
        ListNode head = new ListNode(0);
        ListNode work = head;
        while(l1 != null || l2 != null || fbi == 1){
            if(l1 != null){
                fbi += l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                fbi += l2.val;
                l2 = l2.next;
            }
            work.next = new ListNode(fbi % 10);
            work = work.next;
            fbi = (fbi >= 10? 1: 0);
        }
        return head.next;
    }
}