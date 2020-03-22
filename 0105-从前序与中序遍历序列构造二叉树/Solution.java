class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder == null || inorder == null || preorder.length == 0 || inorder.length ==0){
            return null;
        }
        return helper(preorder, 0, preorder.length-1, inorder, 0, inorder.length-1);

    }

    private TreeNode helper(int[] preorder, int pindex1, int pindex2, int[] inorder, int iindex1, int iindex2){
        if(pindex2 < pindex1 || iindex2 < iindex1){ return null; }
        int rnum = preorder[pindex1];
        int i;
        for (i = iindex1; i <= iindex2; i++) {
            if(inorder[i] == rnum){ break; }
        }
        TreeNode root = new TreeNode(rnum);
        root.left = helper(preorder, pindex1+1, pindex1+i-iindex1, inorder, iindex1, i-1);
        root.right = helper(preorder, pindex1+i-iindex1+1, pindex2, inorder, i+1, iindex2);
        return root;
    }
}