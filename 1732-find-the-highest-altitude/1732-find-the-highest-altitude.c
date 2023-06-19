int largestAltitude(int* gain, int gainSize){
    int altitude = 0;
    int maxAltitude = 0;
        
    for (int i = 0; i < gainSize; i++) {
        altitude += gain[i];
        maxAltitude = fmax(maxAltitude, altitude);
    }
        
    return maxAltitude;
}