public class Solution
{
    public int[][] GenerateMatrix(int n)
    {
        var matrix = new int[n][];
        for (int i = 0; i < n; i++)
            matrix[i] = new int[n];

        var steps = new[] { 1, n, -1, -n };
        int step = 0;
        int curr = n;
        int twice = 0;
        int pos = 0;
        int num = 1;

        while (curr > 0)
        {
            for (int i = 0; i < curr; i++)
            {
                matrix[pos / n][pos % n] = num++;
                pos += steps[(i == curr - 1 ? ++step : step) % 4];
            }

            curr -= ++twice % 2;
        }

        return matrix;
    }
}