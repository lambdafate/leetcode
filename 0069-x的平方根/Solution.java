class Solution {
    public int mySqrt(int x) {
        if(x < 2){ return x;}
        int left=0, right=x;
        while(left <= right){
            int mid = (left + right)/2;
            if(mid == x/mid){ return mid;}
            if(mid < x/mid){
                left = mid+1;
            }else{
                right = mid-1;
            }
        }
        return (Math.pow(left,2)>x)?right: left;
    }
}