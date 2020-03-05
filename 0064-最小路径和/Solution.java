// 标准动态规划
class Solution {
    public int minPathSum(int[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0){
            return 0;
        }
        int row = grid.length;
        int clo = grid[0].length;
        int[][] dp = new int[row][clo];
        dp[0][0] = grid[0][0];
        for(int j=1; j<clo; j++){
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }
        for(int i=1; i<row; i++){
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }

        for(int i=1; i<row; i++){
            for(int j=1; j<clo; j++){
                if(dp[i][j-1] < dp[i-1][j]){
                    dp[i][j] = dp[i][j-1] + grid[i][j];
                }else{
                    dp[i][j] = dp[i-1][j] + grid[i][j];
                }
            }
        }
        return dp[row-1][clo-1];
    }   
}