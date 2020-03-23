class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }
        long target = x;
        long res = x;
        while(res > target/res){
            res = (res + target/res) / 2;
        }
        return (int)res;
    }
}