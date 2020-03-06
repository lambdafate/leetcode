class Solution {
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length < 2){
            return 0;
        }
        // 谷底, 即买入的最低价
        int minprice = prices[0];
        int maxvalue = 0;
        // 遍历每一天价格的时候，
        // 要么prices[i]小于minprice, 则更新minprice
        // 要么prices[i]大于minprice, 则选择更新maxvalue 
        for(int i=1; i<prices.length; i++){
            if(prices[i] < minprice){
                minprice = prices[i];
            }else if(prices[i]-minprice > maxvalue){
                maxvalue = prices[i]-minprice;
            }
        }
        return maxvalue;
    }
}