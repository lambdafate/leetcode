import java.util.HashMap;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            
            for (int j = i + 1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target){
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }

    public int[] twoSum2(int[] nums, int target) {
        HashMap<Integer, Integer> helper = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if(helper.containsKey(nums[i])){
                return new int[]{helper.get(nums[i]), i};
            }
            helper.put(target - nums[i], i);
        }
        return null;
    }


    public static void main(String[] args){
        int[] nums = new int[]{2, 7, 11, 15};
        int target = 9;
        var res = new Solution().twoSum(nums, target);
        if(res == null){
            System.out.println("res == null");
        }else{
            System.out.println("[" + res[0] + ", " + res[1] + "]");
        }
    }
}