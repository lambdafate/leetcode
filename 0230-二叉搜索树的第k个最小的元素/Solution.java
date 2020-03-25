import java.util.ArrayList;
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
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        helper(root, res);
        return res.get(k-1);

    }

    private void helper(TreeNode root, List<Integer> res){
        if(root == null){ return; }
        helper(root.left, res);
        res.add(root.val);
        helper(root.right, res);
    }

    private void helper2(TreeNode root, List<Integer> res){
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root.left;
        stack.push(root);
        while(!stack.empty() || curr != null){
            while(curr != null){
                 stack.push(curr);
                 curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
    }
}