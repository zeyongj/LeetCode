class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int sum=numBottles;
        int x=numBottles;
        while(true){
            int y=x/numExchange;
            int z=x%numExchange;
            sum+=y;
            x=y+z;
            if(x<numExchange){
                break;
            }
        }
        return sum;
        
    }
}