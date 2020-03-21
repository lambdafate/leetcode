class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || postorder == null || inorder.length == 0 || postorder.length == 0) {
            return null;
        }
        return helper(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1);
    }

    private TreeNode helper(int[] inorder, int iindex0, int iindex1, int[] postorder, int pindex0, int pindex1){
        if(iindex1 < iindex0 || pindex1 < pindex0){ return null; }
        int rnum = postorder[pindex1];
        int i = iindex0;
        for (;i<=iindex1; i++) {
            if(inorder[i] == rnum){
                break;
            }
        }
        TreeNode root = new TreeNode(rnum);
        root.left = helper(inorder, iindex0, i-1, postorder, pindex0,  pindex0+i-iindex0-1);
        root.right = helper(inorder, i+1, iindex1, postorder, pindex0+i-iindex0, pindex1-1);
        return root;
    }
}