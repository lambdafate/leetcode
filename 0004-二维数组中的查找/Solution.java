class Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        // 这里除了要判断行的情况, 也要判断列的情况
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return false;
        }
        int row=matrix.length-1, clo=matrix[0].length-1;
        // 这里应该是row和clo的最小值
        int finish = row < clo? row:clo;
        for(int i=0; i<=finish; i++){
            if(target < matrix[i][i]){
                return false;
            }
            int left=i, right=clo;
            while(left <= right){
                int mid = (left + right) / 2;
                if(target > matrix[i][mid]){
                    left = mid + 1;
                }else if(target < matrix[i][mid]){
                    right = mid -1;
                }else{
                    return true;
                }
            }

            left=i; right = row;
            while(left <= right){
                int mid = (left + right) / 2;
                if (target > matrix[mid][i]) {
                    left = mid + 1;
                } else if (target < matrix[mid][i]) {
                    right = mid - 1;
                } else {
                    return true;
                }
            }
        }
        return false;
    }
}