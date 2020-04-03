class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode partition(ListNode head, int x) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode nhead = new ListNode(Integer.MIN_VALUE);
        nhead.next = head;
        ListNode small = nhead;
        ListNode big = nhead;
        while(small.next != null){
            if(small.next.val < x){
                small = small.next;
            }else{
                big = small.next;
                break;
            }
        }
        if(big == nhead){
            return head;
        }
        ListNode work = big.next;
        while(work != null){
            if(work.val >= x){
                big = work;
                work = work.next;
            }else{
                big.next = work.next;
                work.next = small.next;
                small.next = work;
                small = small.next;
                work = big.next;
            }
        }
        return nhead.next;
    }
}