public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if(n < 2){ return n;}
        int left=1, right=n;
        while(left<right){
            // 防止溢出
            int mid = left + (right - left) / 2;
            boolean check = isBadVersion(mid);
            if(check){
                right = mid;
            }else{
                left = mid+1;
            }
        }
        return right;
    }
}