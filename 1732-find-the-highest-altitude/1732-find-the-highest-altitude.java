class Solution {
    public int largestAltitude(int[] gain) {
        int altitude = 0;
        int maxAltitude = 0;
        int len = gain.length;
        
        for (int i = 0; i < len; i++) {
            altitude += gain[i];
            maxAltitude = Math.max(maxAltitude, altitude);
        }
        
        return maxAltitude;        
    }
}