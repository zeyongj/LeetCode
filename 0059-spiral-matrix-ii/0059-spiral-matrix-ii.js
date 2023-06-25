public class Solution
{
    public int[][] GenerateMatrix(int n)
    {
        var matrix = new int[n][];
        for (var i = 0; i < n; i++)
            matrix[i] = new int[n];

        var steps = new[] { 1, n, -1, -n };
        var step = 0;
        var curr = n;
        var twice = 0;
        var pos = 0;
        var num = 1;

        while (curr > 0)
        {
            for (var i = 0; i < curr; i++)
            {
                matrix[pos / n][pos % n] = num++;
                pos += steps[(i == curr - 1 ? ++step : step) % 4];
            }

            curr -= ++twice % 2;
        }

        return matrix;
    }
}