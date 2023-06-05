public class Solution {
    private int size;
    private int count;

    public int totalNQueens(int n) {
        count = 0;
        size = (1 << n) - 1;
        solve(0, 0, 0);
        return count;
    }

    private void solve(int queens, int ld, int rd) {
        if (queens == size) {
            count++;
            return;
        }
        int pos = size & ~(queens | ld | rd);
        while (pos > 0) {
            int bit = pos & -pos;
            pos -= bit;
            solve(queens | bit, (ld | bit) << 1, (rd | bit) >> 1);
        }
    }
}
