import java.util.HashMap;

class Solution {
    public int findPairs(int[] nums, int k) {
        if(k < 0){ return 0;}
        HashMap<Integer, Integer> each = new HashMap<>();
        HashMap<Integer, Integer> res = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if(each.containsKey(nums[i]+k)){
                res.put(nums[i]+k, 0);
            }
            if(each.containsKey(nums[i]-k)){
                res.put(nums[i], 0);
            }
            each.put(nums[i], 0);
        }
        return res.size();
    }
}