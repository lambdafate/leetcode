class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        if (dungeon == null || dungeon.length == 0 || dungeon[0].length == 0) {
            return 1;
        }
        int row = dungeon.length - 1, clo = dungeon[0].length - 1;
        int[][] dp = new int[row + 1][clo + 1];
        for (int i = row; i >= 0; i--) {
            for (int j = clo; j >= 0; j--) {
                if (i == row && j == clo) {
                    dp[i][j] = Math.max(1, 1 - dungeon[i][j]);
                } else if (i == row) {
                    dp[i][j] = Math.max(1, dp[i][j + 1] - dungeon[i][j]);
                } else if (j == clo) {
                    dp[i][j] = Math.max(1, dp[i + 1][j] - dungeon[i][j]);
                } else {
                    dp[i][j] = Math.max(1, Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);
                }
            }
        }
        return dp[0][0];
    }
}