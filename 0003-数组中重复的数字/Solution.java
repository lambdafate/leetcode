import java.util.HashMap;

class Solution {
    public int findRepeatNumber(int[] nums) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        HashMap<Integer, Integer> helper = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            if(helper.containsKey(nums[i])){
                return nums[i];
            }
            helper.put(nums[i], 1);
        }
        return -1;
    }
}