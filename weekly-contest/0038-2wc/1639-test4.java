import java.util.AbstractMap;
import java.util.HashMap;


/*
    执行时间大概在python的一半左右
*/
class Solution {
    private HashMap<AbstractMap.SimpleEntry<Character, Integer>, Integer> cache = new HashMap<>();

    public int numWays(String[] words, String target) {
        if(target == null || target.length() == 0 || words == null || words.length == 0){
            return 0;
        }
        long dp[][] = new long[target.length()][words[0].length()];
        for (int i = 0; i < dp[0].length; i++) {
            dp[0][i] = Count(words, i, target.charAt(0));
            if(i > 0){
                dp[0][i] += dp[0][i-1];
            }
        }
        for (int i = 1; i < dp.length; i++) {
            for (int j = 1; j < dp[0].length; j++) {
                int count = Count(words, j, target.charAt(i));

                // 这里使用if可以通过测试, 如果不用的话TLE
                if(count == 0){
                    dp[i][j] = dp[i][j-1];
                }else {
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] * count;
                }
                dp[i][j] = dp[i][j] % 1000000007;
            }
        }

        return (int)dp[dp.length-1][dp[0].length-1];
    }

    private int Count(String[] words, int i, char c){
        AbstractMap.SimpleEntry<Character, Integer> key = new AbstractMap.SimpleEntry<>(c, i);
        if(cache.containsKey(key)) {
            return cache.get(key);
        }
        int count = 0;
        for (String word : words) {
            if(word.charAt(i) == c){
                count += 1;
            }
        }
        cache.put(key, count);
        return count;
    }

    public static void main(String[] args) {

    }
}