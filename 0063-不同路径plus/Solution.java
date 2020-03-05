// 有障碍物的地方都不能到达, 即dp[i][j] = 0
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid == null ||obstacleGrid.length == 0 || obstacleGrid[0].length == 0){
            return 0;
        }
        int row = obstacleGrid.length;
        int clo = obstacleGrid[0].length;
        if(obstacleGrid[0][0] == 1 || obstacleGrid[row-1][clo-1] == 1){
            return 0;
        }
        int[][] dp = new int[row][clo];
        dp[0][0] = 1;
        for(int j=1; j<clo; j++){
            dp[0][j] = dp[0][j-1];
            if(obstacleGrid[0][j] == 1){
                dp[0][j] = 0;
            }
        }
        for(int i=1; i<row; i++){
            dp[i][0] = dp[i-1][0];
            if(obstacleGrid[i][0] == 1){
                dp[i][0] = 0;
            }
        }
        for(int i=1; i<row; i++){
            for(int j=1; j<clo; j++){
                if(obstacleGrid[i][j] == 1){
                    dp[i][j] = 0;
                }else{
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }

        return dp[row-1][clo-1];
    }
}