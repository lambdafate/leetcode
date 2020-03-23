class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public int sumNumbers(TreeNode root) {
        if(root == null){ return 0;}
        if(root.left == null && root.right == null){ return root.val; }
        return helper(root.left, root.val) + helper(root.right, root.val);
    }

    private int helper(TreeNode root, int sum){
        if(root == null){ return 0;}
        int nsum = sum*10 + root.val;
        if (root.left == null && root.right == null) {
            return nsum;
        }
        int lsum = helper(root.left, nsum);
        int rsum = helper(root.right, nsum);
        return lsum + rsum;
    }
}