class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int ans=-1;
        int m=Integer.MAX_VALUE;
        for(int i=0;i<points.length;i++){
            if(points[i][0]==x || points[i][1]==y){
                int c=Math.min(points[i][0] , points[i][1]);
                if(x==points[i][0]){
                    if(m>Math.abs(points[i][1]-y)) {m=Math.abs(points[i][1]-y);
                    ans=i;}
                }
                else{
                    if(m>Math.abs(points[i][0]-x)) {m=Math.abs(points[i][0]-x);
                    ans=i;}
                }

            }
        }
        return ans;
    }
}