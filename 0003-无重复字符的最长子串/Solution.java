import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s == null || s.length() == 0){
            return 0;
        }
        int res=0, i=0, j=0;
        HashMap<Character, Integer> helper = new HashMap<>();
        while(j < s.length()){
            if(helper.containsKey(s.charAt(j)) && helper.get(s.charAt(j))>=i){
                i = helper.get(s.charAt(j)) + 1;
            }
            helper.put(s.charAt(j), j);
            j++;
            res = Math.max(res, j-i);
        }
        return res;
    }
}