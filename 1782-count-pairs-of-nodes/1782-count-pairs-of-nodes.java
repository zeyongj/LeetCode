class Solution {
    public int[] countPairs(int n, int[][] edges, int[] qs) {
        int[] cnt = new int[n + 1], sorted_cnt = new int[n + 1], res = new int[qs.length];
        HashMap<Integer, Integer>[] shared = new HashMap[n + 1];
        for (var e : edges) {
            sorted_cnt[e[0]] = cnt[e[0]] = cnt[e[0]] + 1;
            sorted_cnt[e[1]] = cnt[e[1]] = cnt[e[1]] + 1;
            int n1 = Math.min(e[0], e[1]), n2 = Math.max(e[0], e[1]);
            shared[n1] = shared[n1] == null ? new HashMap() : shared[n1];
            shared[n1].put(n2, shared[n1].getOrDefault(n2, 0) + 1);
        }
        Arrays.sort(sorted_cnt);
        for (int q = 0; q < qs.length; ++q) {
            for (int i = 1, j = n; i < j; )
                if (qs[q] < sorted_cnt[i] + sorted_cnt[j])
                    res[q] += (j--) - i;
                else
                    ++i;
            for (int i = 1; i <= n; ++i)
                if (shared[i] != null)
                    for (var p : shared[i].entrySet()) {
                        int j =  p.getKey(), sh_cnt = p.getValue();
                        if (qs[q] < cnt[i] + cnt[j] && qs[q] + sh_cnt >= cnt[i] + cnt[j])
                            --res[q]; 
                    }
        }
        return res;
    }
}