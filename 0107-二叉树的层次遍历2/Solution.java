
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Stack<List<Integer>> res = new Stack<>();
        Stack<List<Integer>> result = new Stack<>();
        helper(res, root);
        while(!res.empty()){
            result.add(res.pop());
        }
        return result;
    }

    private void helper(Stack<List<Integer>> res, TreeNode root){
        if(root == null){
            return;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
            List<Integer> currlevel = new ArrayList<>();
            int num = queue.size();
            for (int i = 0; i < num; i++) {
                TreeNode currnode = queue.poll();
                currlevel.add(currnode.val);
                if(currnode.left != null){ queue.add(currnode.left); }
                if(currnode.right != null){ queue.add(currnode.right); }
            }
            res.add(currlevel);
        }

    }
}