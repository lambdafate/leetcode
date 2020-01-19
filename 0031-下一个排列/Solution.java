class Solution {
    public void nextPermutation(int[] nums) {
        if(nums.length < 2){
            return;
        }
        for(int i=nums.length-2; i>=0; i--){
            if(nums[i] < nums[i+1]){
                int high = i + 1;
                //nums[i] 和  nums.length到i+1升序序列中第一个大于nums[i]的元素交换位置
                for(int j=nums.length-1; j >= high; j--){
                    if(nums[j] > nums[i]){
                        int temp = nums[j];
                        nums[j] = nums[i];
                        nums[i] = temp;
                        break;
                    }
                }
                // i+1到nums.length改为升序排列
                for(int j=nums.length-1; j>high; j--, high++){
                    int temp = nums[j];
                    nums[j] = nums[high];
                    nums[high] = temp;
                }

                return;
            }
        }

        for(int i=0, j=nums.length-1; i<j; j--, i++){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }

    public static void main(String[] args) {
        new Solution().nextPermutation(new int[]{1,3,2});
    }
}