public class Solution {
    public int LargestAltitude(int[] gain) {
        int altitude = 0;
        int maxAltitude = 0;
        int len = gain.Length;
        
        for (int i = 0; i < len; i++) {
            altitude += gain[i];
            maxAltitude = Math.Max(maxAltitude, altitude);
        }
        
        return maxAltitude;                
    }
}