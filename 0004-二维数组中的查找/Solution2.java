// 从右上角看就是一颗二叉搜索树
class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        // 这里除了要判断行的情况, 也要判断列的情况
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int row = 0, clo = matrix[0].length - 1;
        while(row < matrix.length && clo >= 0){
            if(target == matrix[row][clo]){
                return true;
            }else if(target < matrix[row][clo]){
                clo--;
            }else{
                row++;
            }
        }
        return false;
    }
}