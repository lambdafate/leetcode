
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }

    TreeNode(int x, TreeNode left, TreeNode right){
        val = x;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean isValidBST(TreeNode root) {
        if(root == null){ return true; }
        return helper(root, root.val, 0);
    }

    private boolean helper(TreeNode root, int num, int flag){
        if(root == null){ return true; }
        if ((root.left != null && root.left.val >= root.val)) {
            return false;
        }
        if (root.right != null && root.right.val <= root.val) {
            return false;
        }
        if(flag == 1){
            if(root.left != null && root.left.val <= num){ return false; }
        }else if(flag == -1){
            if(root.right != null && root.right.val >= num){ return false; }
        }

        boolean lres = helper(root.left, root.val, -1);
        boolean rres = helper(root.right, root.val, 1);
        return  lres && rres;
    }

    public static void main(String[] args) {
        var tree5 = new TreeNode(5, new TreeNode(4), new TreeNode(6, null, new TreeNode(3)));
        var tree1 = new TreeNode(1, new TreeNode(0), new TreeNode(2));
        var demo = new TreeNode(3, tree1, tree5);
        var res = new Solution().isValidBST(demo);
        System.out.println(res);
    }
}