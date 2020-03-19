class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums == null || nums.length == 0){ return null; }
        TreeNode root = helper(nums, 0, nums.length-1);
        return root;
    }

    private TreeNode helper(int[] nums, int index1, int index2){
        int res = index2 - index1;
        if(res < 0){
            return null;
        }else if(res == 0){
            return new TreeNode(nums[index1]);
        }

        int index = (index1+index2)/2;
        TreeNode root = new TreeNode(nums[index]);
        root.left = helper(nums, index1, index-1);
        root .right = helper(nums, index+1, index2);
        return root;
    }
}