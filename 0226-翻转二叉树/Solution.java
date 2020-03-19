class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null){ return null; }
        TreeNode newleft = invertTree(root.right);
        TreeNode neeright = invertTree(root.left);
        root.left = newleft;
        root.right = newright;
        return root;
    }
}