import java.util.ArrayList;

/**
 * Definition for singly-linked list. 
 * public class ListNode 
 * {    int val; 
 *      ListNode next; 
 *      ListNode(int x) { val = x; } 
 * }
 */
class Solution {
    public int[] reversePrint(ListNode head) {
        ArrayList<Integer> res = new ArrayList<>();
        ListNode fuck = head;
        while(fuck != null){
            res.add(fuck.val);
            fuck = fuck.next;
        }
        int i=0, j=res.size()-1;
        int[] fucktoo = new int[res.size()];
        while(i<=j){
            fucktoo[j] = res.get(i);
            fucktoo[i] = res.get(j);
            i++; j--;
        }
        return fucktoo;
    }
}