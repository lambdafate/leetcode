class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(k == 0 || head == null || head.next == null){
            return head;
        }
        ListNode work = head;
        int num = 0;
        while(work != null){ num++; work=work.next;}
        int step = k % num;
        if(step == 0){
            return head;
        }
        ListNode prev=head;
        work=prev.next;
        int steps = step;
        while(steps-- != 0){
            work = work.next;
        }
        while(work != null){
            prev = prev.next;
            work = work.next;
        }
        work = prev.next;
        prev.next = null;
        prev = work;
        while(work.next != null){
            work = work.next;
        }
        work.next = head;
        return prev;
    }
}