class Solution {
    public String convertToTitle(int columnNumber) {
        String s = "";
        while(columnNumber != 0){
            int y = columnNumber%26;
            columnNumber = columnNumber/26;
            if (y == 0) {
                s = String.valueOf((char) ('Z')) + s;
                if (columnNumber == 1)
                    break;
                columnNumber--;
            }
            else
                s = String.valueOf((char)(y-1+'A')) + s;
        }

        return s;
    }
}