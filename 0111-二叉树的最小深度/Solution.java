class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public int minDepth(TreeNode root) {
        if(root == null){ return 0; }
        int leftdepth = minDepth(root.left);
        int rightdepth = minDepth(root.right);
        int res = 1;
        // if(leftdepth == 0){
        //     res += rightdepth;
        // }else if(rightdepth == 0){
        //     res += leftdepth;
        if(leftdepth == 0 || rightdepth == 0){
            res += Math.max(leftdepth, rightdepth);
        }else{
            res += Math.min(leftdepth, rightdepth);
        }
        return res;
    }
}