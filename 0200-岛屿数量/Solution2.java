import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        int num = 0;
        LinkedList<List<Integer>> queue = new LinkedList<>(); 
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '0') {
                    continue;
                }
                num++;
                List<Integer> temp = new ArrayList<>();
                temp.add(i); temp.add(j);
                queue.offer(temp);
                while(!queue.isEmpty()){
                    List<Integer> curr = queue.poll();
                    int row = curr.get(0), clo = curr.get(1);
                    if(grid[row][clo] == '0'){ continue; }
                    grid[row][clo] = '0';
                    if(row>=1){
                        List<Integer> up = new ArrayList<>();
                        up.add(row-1); up.add(clo);
                        queue.offer(up);
                    }
                    if(row<(grid.length-1)){
                        List<Integer> down = new ArrayList<>();
                        down.add(row+1); down.add(clo);
                        queue.offer(down);
                    }
                    if(clo>=1){
                        List<Integer> left = new ArrayList<>();
                        left.add(row); left.add(clo-1);
                        queue.offer(left);
                    }
                    if(clo<(grid[0].length-1)){
                        List<Integer> right = new ArrayList<>();
                        right.add(row); right.add(clo+1);
                        queue.offer(right);
                    }
                }

            }
        }
        return num;
    }

}