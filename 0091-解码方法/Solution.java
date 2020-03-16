class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0 || (s.length() >= 1 && s.charAt(0)=='0')){ return 0; }
        int[] dp = new int[s.length()];
        dp[0] = 1;
        if(s.length()>1){
            dp[1] = 0;
            if(s.charAt(1) != '0'){ dp[1] += 1;}
            if(fuck(s, 0, 1)){ dp[1] += 1; }
        }
        for (int i = 2; i < dp.length; i++) {
            if(s.charAt(i) == '0'){
                if(s.charAt(i - 1) > '0' && s.charAt(i - 1) < '3'){ 
                    dp[i] = dp[i - 2];
                }else{
                    dp[dp.length-1] = 0;
                    break;
                }
                
            }else if(fuck(s, i-1, i)){
                dp[i] = dp[i-2] + dp[i-1];
            }else{
                dp[i] = dp[i-1];
            }
            
        }
        return dp[dp.length-1] ;
    }

    private boolean fuck(String s, int index1, int index2){
        int fuck1 = s.charAt(index1) - '0';
        int fuck2 = s.charAt(index2) - '0';
        int res   = fuck1 * 10 + fuck2;
        return (res>0 && res<27 && fuck1 != 0);
    }
    
}