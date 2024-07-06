class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        // test if circle center is at radius distance, or less, from one of the corners :
        if(sqDist(xCenter, yCenter, x1, y1) <= radius*radius) return true;
        if(sqDist(xCenter, yCenter, x2, y2) <= radius*radius) return true;
        if(sqDist(xCenter, yCenter, x1, y2) <= radius*radius) return true;
        if(sqDist(xCenter, yCenter, x2, y1) <= radius*radius) return true;

        // test if circle center is at the top or bottom at less than radius
        if(xCenter >= x1 - radius && xCenter <= x2 + radius && yCenter >= y1 && yCenter <= y2) return true;


        // test if circle center is at the right or left at less than radius
        if(xCenter >= x1 && xCenter <= x2 && yCenter >= y1 - radius && yCenter <= y2 + radius) return true;

        return false;
    }

    int sqDist(int x1, int y1, int x2, int y2) {
        return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
    }
};