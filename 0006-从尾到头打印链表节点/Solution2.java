class Solution {
    public int[] reversePrint(ListNode head) {
        ListNode fuck = head;
        int num = 0;
        while (fuck != null) {
            num++;
            fuck = fuck.next;
        }
        fuck = head;
        int[] fucktoo = new int[num];
        while (fuck != null) {
            fucktoo[--num] = fuck.val;
            fuck = fuck.next;
        }
        return fucktoo;
    }
}