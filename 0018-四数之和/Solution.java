import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if(nums == null ||nums.length<4){
            return res;
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-3; i++) {
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            for (int j = i+1; j < nums.length-2; j++) {
                if(j>i+1 && nums[j]==nums[j-1]){
                    continue;
                }
                int left =j+1, right = nums.length-1;
                while(left < right){
                    if(left>j+1 && nums[left]==nums[left-1]){ left++; continue;}
                    if(right<nums.length-1 && nums[right]==nums[right+1]){ right--; continue;}
                    
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if(sum == target){
                        List<Integer> temp = new ArrayList<>();
                        temp.add(nums[i]); temp.add(nums[j]); 
                        temp.add(nums[left]); temp.add(nums[right]);
                        res.add(temp);
                        left++; right--;
                    }else if(sum < target){
                        left++;
                    }else{
                        right--;
                    }
                }
            }
        }
        return res;
    }
}