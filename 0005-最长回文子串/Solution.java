// 正序和反序看都一样即为回文串
class Solution {
    public String longestPalindrome(String s) {
        if(s == null || s.length() == 0){
            return "";
        }
        // dp[i][j]->代表i~j子串是否为回文串
        // dp[i][j]=dp[i+1][j-1] && Si==Sj
        boolean[][] dp = new boolean[s.length()][s.length()];
        int maxlength = 1;
        int index = 0;
        int templength = 0;
        for(int i=0; i<s.length(); i++){
            dp[i][i] = true;
        }
        for(int i=s.length()-2; i>=0; i--){
            for(int j=i+1; j<s.length(); j++){
                if(s.charAt(i) != s.charAt(j)){
                    dp[i][j] = false;
                    continue;
                }
                if(i+1 == j || dp[i+1][j-1]){
                    dp[i][j] = true;
                    templength = j-i+1;
                    if(templength > maxlength){
                        maxlength = templength;
                        index = i;
                    }
                }
            }
        }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        return s.substring(index, maxlength+index);
    }
}