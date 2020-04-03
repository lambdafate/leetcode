class Solution {
    public void sortColors(int[] nums) {
        int num1 = 0;
        int num2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == 0){
                num1++;
            }else if(nums[i] == 1){
                num2++;
            }
        }
        int i;
        for (i = 0; i < num1; i++) {
            nums[i] = 0;
        }
        for (; i < num1+num2; i++) {
            nums[i] = 1;
        }
        for (; i < nums.length; i++) {
            nums[i] = 2;
        }
        
    }
}