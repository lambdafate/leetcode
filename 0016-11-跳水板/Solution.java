class Solution {
    public int[] divingBoard(int shorter, int longer, int k) {
        if(k == 0){
            return new int[]{};
        }
        if(shorter == longer){
            return new int[]{shorter*k};
        }
        int[] res = new int[k+1];
        for (int i = 0; i <= k; i++) {
            res[i] = i*longer + shorter*(k-i);
        }
        return res;
    }
}