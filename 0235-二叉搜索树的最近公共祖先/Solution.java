class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null){ return null; }
        if(root == p || root == q || (root.val>p.val && root.val<q.val) || (root.val>q.val && root.val<p.val)){
            return root;
        }
        if(root.val > p.val){
            return lowestCommonAncestor(root.left, p, q);
        }
        return lowestCommonAncestor(root.right, p, q);
    }
}