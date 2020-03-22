import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }

    TreeNode(int x, TreeNode left, TreeNode right) {
        val = x;
        this.left = left;
        this.right = right;
    }
}

class Solution2 {
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        List<Integer> res = new ArrayList<>();
        helper(root, res);
        if(res.size() < 2){ return true;}
        for(int i=1; i<res.size(); i++){
            if(res.get(i-1) >= res.get(i)){
                return false;
            }
        }
        return true;
    }

    private void helper(TreeNode root, List<Integer> res) {
        if(root == null){ return;}
        helper(root.left, res);
        res.add(root.val);
        helper(root.right, res);
    }

    public static void main(String[] args) {
        var tree5 = new TreeNode(5, new TreeNode(4), new TreeNode(6, null, new TreeNode(3)));
        var tree1 = new TreeNode(1, new TreeNode(0), new TreeNode(2));
        var demo = new TreeNode(3, tree1, tree5);
        var res = new Solution().isValidBST(demo);
        System.out.println(res);
    }
}