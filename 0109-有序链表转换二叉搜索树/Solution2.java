import java.awt.List;
import java.util.ArrayList;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) {
            return null;
        }
        List<Integer> lists = new ArrayList<>();
        while(head != null){ lists.add(head.val); head=head.next; }

        return helper(lists, 0, lists.size()-1);
    }

    private TreeNode helper(List<Integer> lists, int index1, int index2){
        if(index2 < index1){ return null; }
        if(index2 == index1){ return new TreeNode(lists.get(index1)); }
        int mid = index1 + (index2-index1)/2;
        TreeNode res = new TreeNode(lists.get(mid));
        res.left = helper(lists, index1, mid-1);
        res.right = helper(lists, mid+1, index2);
        return res;
    }
}