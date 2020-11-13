import java.util.ArrayList;

class Solution {
    public int[] sortArrayByParityII(int[] A) {
        if (A == null || A.length == 0) {
            return A;
        }
        ArrayList<Integer> odd = new ArrayList<>();
        ArrayList<Integer> even = new ArrayList<>();
        for (int i = 0; i < A.length; i++) {
            if (A[i] % 2 == 0) {
                even.add(A[i]);
            } else {
                odd.add(A[i]);
            }
        }
        for (int i = 0, j = 0, k = 0; i < A.length; i++) {
            if (i % 2 == 0) {
                A[i] = even.get(j);
                j++;
            } else {
                A[i] = odd.get(k);
                k++;
            }
        }
        return A;
    }
}