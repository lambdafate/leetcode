import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if(nums == null || nums.length < 3){ return res; }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-2; i++) {
            if(i>0 && nums[i]==nums[i-1]){ continue; }

            int left=i+1, right=nums.length-1;
            while(left < right){
                if(left>i+1 && nums[left]==nums[left-1]){
                    left++;
                    continue;
                }
                if(right<nums.length-1 && nums[right]==nums[right+1]){
                    right--;
                    continue;
                }
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0){
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[i]); temp.add(nums[left]); temp.add(nums[right]);
                    res.add(temp);
                    left++; right--;
                }else if(sum < 0){
                    left++;
                }else{
                    right--;
                }
            }   
        }
        return res;
    }
}