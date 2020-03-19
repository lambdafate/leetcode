class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    // null, 0 --> false
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null){
            return false;
        }
        int newsum = sum - root.val;
        if(newsum == 0 && root.left == null && root.right == null){
            return true;
        }
        return hasPathSum(root.left, newsum) || hasPathSum(root.right, newsum);
    }
}