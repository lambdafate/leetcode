class Solution {
    public int[] sortedSquares(int[] A) {
        int[] res = new int[A.length];
        int i=0, j=A.length-1;
        int index=A.length-1;
        while(i <= j){
            if(Math.abs(A[i]) < Math.abs(A[j])){
                res[index--] = A[j] * A[j];
                j--;
            }else{
                res[index--] = A[i] * A[i];
                i++;
            }
        }
        return res;
    }
}