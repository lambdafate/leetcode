import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        HashMap<Integer, Integer> helper = new HashMap<>();
        for (int i = 0; i < numbers.length; i++) {
            if(helper.containsKey(numbers[i])){
                res[0] = helper.get(numbers[i]);
                res[1] = i+1;
                break;
            }
            helper.put(target-numbers[i], i+1);
        }
        return res;
    }
}