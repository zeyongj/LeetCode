import (
    "fmt"
)

func largestAltitude(gain []int) int {
    altitude := 0
    maxAltitude := 0
    
    for _, g := range gain {
        altitude += g
        if altitude > maxAltitude {
            maxAltitude = altitude
        }
    }
    
    return maxAltitude
}