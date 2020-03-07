class Solution {
    public int lengthOfLastWord(String s) {
        if(s == null || s.length() == 0){
            return 0;
        }
        int res = 0, index = s.length()-1;
        while(index >= 0){
            if(s.charAt(index) == ' '){
                if(res != 0){
                    break;
                }
            }else{
                res++;
            }
            index--;
        }
        return res;
        
    }
}