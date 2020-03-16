class Solution {
    public int minDistance(String word1, String word2) {
        if(word1.equals("")){ return word2.length(); }
        if(word2.equals("")){ return word1.length(); }

        int[][] dp = new int[word1.length()+1][word2.length()+1];
        dp[0][0]   = 0;
        for(int i=1; i<=word2.length(); i++){ dp[0][i] = i; }
        for(int i=1; i<=word1.length(); i++){ dp[i][0] = i; }
        
        for(int i=1; i<=word1.length(); i++){
            for(int j=1; j<=word2.length(); j++){
                int first = dp[i-1][j] + 1;
                int second = dp[i][j-1] + 1;
                int third = dp[i-1][j-1] + (word1.charAt(i-1)==word2.charAt(j-1) ? 0 : 1) ;
                dp[i][j] = Math.min(first, Math.min(second, third));
            }
        }

        // for (int i = 0; i < dp.length; i++) {
        //     for (int j = 0; j < dp[0].length; j++) {
        //         System.out.print(dp[i][j]+" ");
        //     }
        //     System.out.println("");
        // }
        return dp[word1.length()][word2.length()];
    }
}