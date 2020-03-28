import java.util.ArrayList;
import java.util.LinkedList;
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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null){ return res; }
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()){
            int num = queue.size();
            if(num == 0){ return res;}
            res.add(queue.peekLast().val);
            for (int i = 0; i < num; i++) {
                TreeNode curr = queue.poll();
                if(curr.left != null){ queue.offer(curr.left); }
                if(curr.right != null){ queue.offer(curr.right); }
            }
        }
        return res;
    }
}