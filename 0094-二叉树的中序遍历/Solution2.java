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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null){ return res; }
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        //stack.push(curr);
        while(!stack.empty() || curr != null){
            while(curr.left != null){
                stack.push(curr);
                curr = curr.left;
            }
            res.add(curr.val);
            curr = curr.right;
            while(curr == null && !stack.empty()){
                curr = stack.pop();
                res.add(curr.val);
                curr = curr.right;
            }
        }
        return res;
    }
}