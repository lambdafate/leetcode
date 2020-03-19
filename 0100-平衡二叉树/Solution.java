class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public boolean isBalanced(TreeNode root) {
        return helper(root)>=0;
    }

    private int helper(TreeNode root){
        if(root == null){ return 0; }
        int left = helper(root.left);
        if(left == -1){ return -1; }
        int right = helper(root.right);
        if(right == -1){ return -1; }
        if(Math.abs(left-right)<=1){
            return 1 + Math.max(left, right);  
        }
        return -1;
    }
}