#define MAX(a, b) ((a) > (b) ? (a) : (b))

int lengthOfLongestSubstring(char * s)
{
    int counts[512];
    int i, n = strlen(s), win_start = 0;
    int best = 0;
    
    memset(counts, 0, sizeof(int) * 512);

    for (i = 0; i < n; i++) {
        int c = s[i];
        if (counts[c] >= 1) {
            assert(counts[c] == 1);
            // need to move the window until removing the instance of c
            while (win_start < i) {
                int to_del = s[win_start];
                counts[to_del]--;
                win_start++;                
                if (counts[c] == 0)
                    break;
            }
        }
        counts[c]++;
        best = MAX(best, i - win_start + 1);
    }
    
    return best;
}