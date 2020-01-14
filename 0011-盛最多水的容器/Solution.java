class Solution {
    public int maxArea(int[] height) {
        int res = 0, temp = 0;
        for (int i = 0; i < height.length-1; i++) {
            for(int j = i+1; j<height.length; j++){
                temp = (j - i) * (height[i]<height[j]? height[i]: height[j]);
                res = temp > res? temp: res;
            }
        }
        return res;
    }
}