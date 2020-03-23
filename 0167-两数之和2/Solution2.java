class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        int left=0, right=numbers.length-1;
        while(true){
            int temp = numbers[left] + numbers[right];
            if(temp == target){ 
                break;
            }else if(temp < target){
                left++;
            }else{
                right--;
            }
        }
        res[0] = left+1;
        res[1] = right+1;
        return res;
    }
}