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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null){ return res; }
        if(root.val == sum && root.left == null && root.right == null){ List<Integer> temp=new ArrayList<>(); temp.add(sum); res.add(temp); return res;}
        if(root.val != sum && root.left == null && root.right == null){ return res; }
        int newsum = sum - root.val;
        var left = pathSum(root.left, newsum); 
        var right = pathSum(root.right, newsum);
        for (int i = 0; i < left.size(); i++) {
            var curr = left.get(i);
            curr.add(0, root.val);
            res.add(curr);            
        }
        for (int i = 0; i < right.size(); i++) {
            var curr = right.get(i);
            curr.add(0, root.val);
            res.add(curr);
        }
        return res;
    }
}