import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public List<TreeNode> generateTrees(int n) {
        if(n <= 0){ return new ArrayList<TreeNode>(); }
        return helper(1, n);
    }

    private List<TreeNode> helper(int index1, int index2){
        List<TreeNode> res = new ArrayList<>();
        if(index2 < index1){  res.add(null); return res; }
        if(index1 == index2){ res.add(new TreeNode(index1)); return res; }

        for(int i=index1; i<=index2; i++){
            List<TreeNode> left = helper(index1, i-1);
            List<TreeNode> right = helper(i+1, index2);
            for (TreeNode treeleft : left) {
                for (TreeNode treeright : right) {
                    TreeNode root = new TreeNode(i);
                    root.left = treeleft;
                    root.right = treeright;
                    res.add(root);
                }
            }
        }
        return res;
    }
}