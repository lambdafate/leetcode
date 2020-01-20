class Solution {
    public int search(int[] nums, int target) {
        if(nums.length < 1){
            return -1;
        }
        if(nums[0] == target){
            return 0;
        }else if(nums[0] < target){
            for(int i=1; i<nums.length && nums[i-1] <= nums[i]; i++){
                if(target == nums[i]){
                    return i;
                }
            }
        }else{
            int i = 1;
            while(i<nums.length && nums[i-1] <= nums[i]){ i++; }
            if(i < nums.length){
                for(; i<nums.length; i++){
                    if(target == nums[i]){
                        return i;
                    }
                }
            }
        }
        return -1;
    }
}