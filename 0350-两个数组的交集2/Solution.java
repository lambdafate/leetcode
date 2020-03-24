import java.util.HashMap;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1 == null || nums1.length == 0) {
            return new int[0];
        }
        if (nums2 == null || nums2.length == 0) {
            return new int[0];
        }
        HashMap<Integer, Integer> helper = new HashMap<>();
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums1.length; i++) {
            if(helper.containsKey(nums1[i])){ 
                helper.put(nums1[i], helper.get(nums1[i])+1);
            }else{
                helper.put(nums1[i], 1);
            }
        }
        for (int i = 0; i < nums2.length; i++) {
            if (helper.containsKey(nums2[i]) && helper.get(nums2[i]) > 0) {
                res.add(nums2[i]);
                helper.put(nums2[i], helper.get(nums2[i])-1);
            }
        }
        int[] result = new int[res.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = res.get(i);
        }
        return result;
    }
}