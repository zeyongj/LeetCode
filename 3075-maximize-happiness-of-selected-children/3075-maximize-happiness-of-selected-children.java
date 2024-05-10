import java.util.Arrays;

class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);

        int i = 0;
        long res = 0;
        int n = happiness.length;

        while (k > 0 && i < n) {
            int index = n - 1 - i;
            int adjustedHappiness = Math.max(happiness[index] - i, 0);
            res += adjustedHappiness;
            i++;
            k--;
        }
        return res;
    }
}