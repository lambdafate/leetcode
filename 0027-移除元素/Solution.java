class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length < 1){
            return nums.length;
        }
        int j = -1;
        for(int i=0; i<nums.length; i++){
            if(nums[i] != val){
                nums[++j] = nums[i];
            }
        }
        return j+1;
    }
}