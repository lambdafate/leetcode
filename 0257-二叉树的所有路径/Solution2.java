import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    private List<String> res = new ArrayList<>();

    public List<String> binaryTreePaths(TreeNode root) {
        dfs(root, "");
        return res;
    }

    private void dfs(TreeNode root, String points){
        if(root == null){ return; }
        String npoints = points + root.val;
        if(root.left == null && root.right == null){
            res.add(npoints);
        }
        npoints += "->";
        dfs(root.left, npoints);
        dfs(root.right, npoints);
    }
}