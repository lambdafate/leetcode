
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public void flatten(TreeNode root) {
        if(root == null){ return; }
        if(root.left != null){ flatten(root.left); }
        if(root.right != null){ flatten(root.right); }
        if(root.left != null){
            TreeNode curr = root.left;
            while(curr.right != null){ curr = curr.right; }
            curr.right = root.right;
            root.right = root.left;
            root.left = null;
        }
    }
}