class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = 0, right= nums.length - 1;
        int[] res = new int[]{-1, -1};       
        int mid;
        while(left <= right){
            mid = (left + right) / 2;
            if(nums[mid] == target){
                // find min index and max index
                int min = mid - 1, max = mid + 1;
                while(min >= 0 && nums[min] == target){ min--; };
                while(max < nums.length && nums[max] == target){ max++; };
                res[0] = min + 1;
                res[1] = max - 1;
                return res;

            }else if(nums[mid] < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return res;
    }
}