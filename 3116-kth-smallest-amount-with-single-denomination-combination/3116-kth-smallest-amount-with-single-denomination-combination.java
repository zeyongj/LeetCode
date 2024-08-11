class Solution {
    public long gcd(long a, long b) {
        while (b > 0) {
            long c = a;
            a = b;
            b = c % b;
        }
        return a;
    }

    public long findKthSmallest(int[] coins, int k) {
        int n = coins.length;
        long[] LCM = new long[1 << n];
        for (int i = 0; i < n; i++) {
            LCM[1 << i] = coins[i];
        }

        LCM[0] = 1;
        for (int i = 1; i < 1 << n; i++) {
            if (LCM[i] == 0) {
                int q = i & i - 1;
                int r = i & -i;
                LCM[i] = LCM[q] / gcd(LCM[q], LCM[r]) * LCM[r];
            }
        }

        long low = 0, high = 100000000000000L;
        while (high - low > 1) {
            long h = (high + low) / 2;
            long cnt = 0;
            for (int i = 1; i < 1 << n; i++) {
                cnt += h / LCM[i] * (Integer.bitCount(i) % 2 == 0 ? -1 : 1);
            }
            if (cnt >= k) {
                high = h;
            } else {
                low = h;
            }
        }
        return high;
    }
}