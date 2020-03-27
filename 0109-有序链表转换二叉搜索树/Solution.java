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
        if(head == null){ return null;}
        if(head.next == null){
            return new TreeNode(head.val);
        }
        ListNode slow=head, fast=head, prev = null;
        while(fast != null && fast.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;

        TreeNode res = new TreeNode(slow.val);
        res.left = sortedListToBST(head);
        res.right = sortedListToBST(slow.next);

        return res;
    }
}