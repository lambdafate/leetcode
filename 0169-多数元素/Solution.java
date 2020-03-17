import java.util.HashMap;
import java.util.Map;

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> res = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if(res.containsKey(nums[i])){
                res.replace(nums[i], res.get(nums[i])+1);
            }else{
                res.put(nums[i], 1);
            }
        }
        var iter = res.entrySet().iterator();
        int times = 0, result = 0;
        while(iter.hasNext()){
            var kv = (Map.Entry) iter.next();
            if((Integer)kv.getValue() > times){
                times  = (Integer)kv.getValue();
                result = (Integer)kv.getKey();
            }
            System.out.print((Integer) kv.getKey());
            System.out.print((Integer) kv.getValue());
            System.out.println("");
        }
        return result;
    }
}