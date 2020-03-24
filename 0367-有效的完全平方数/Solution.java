class Solution {
    public boolean isPerfectSquare(int num) {
        if (num < 2) {
            return true;
        }
        int res = num;
        while (res > num / res) {
            res = (res + num / res) / 2;
        }
        return res * res == num;
    }
}