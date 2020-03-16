class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if(triangle == null || triangle.size() == 0 || triangle.get(0).size() == 0){
            return 0;
        }
        int length = triangle.get(triangle.size()-1).size();
        int[][] dp = new int[length][length];
        dp[0][0] = triangle.get(0).get(0);
        for (int i = 1; i < length; i++) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = triangle.get(i).get(j);
                if(j == 0){
                    dp[i][j] += dp[i-1][0];
                }else if(j == i){
                    dp[i][j] += dp[i-1][j-1];
                }else{
                    dp[i][j] += Math.min(dp[i-1][j], dp[i-1][j-1]);
                }
            }
        }
        int res = Integer.MAX_VALUE;
        for(int i=0; i< length; i++){
            if(dp[length-1][i] < res){
                res = dp[length-1][i];
            }
        }
        return res;
    }
}