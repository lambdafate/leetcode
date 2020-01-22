import java.util.*;


class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private int[] candis;
    private int length;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        candis = candidates;
        length = candidates.length;

        if(length == 0){
            return res;
        }
        
        Arrays.sort(this.candis);
        Stack<Integer> path = new Stack<>();

        helper(0, target, path);
        return res;
    }


    private void helper(int start, int target, Stack<Integer> path){
        if(target == 0){
            this.res.add(new ArrayList<>(path));
            return;
        }

        for(int i=start; i<this.length; i++){
            int result = target - this.candis[i];
            if(result < 0){
                continue;
            }
            path.push(this.candis[i]);
            helper(i, result, path);
            path.pop();
        }
    }
}