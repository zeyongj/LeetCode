public class Solution {
    public long TotalCost(int[] c, int k, int can)
    {
        long ans = 0;
        if (c.Length == 1)
            return c[0];

        PriorityQueue<int,int> l = new();
        PriorityQueue<int,int> r = new();
        int left = 0, right = c.Length - 1;

        for (int i = 1; i <= can; i++)
        {
            if (i - 1 >= c.Length - i)
                break;

            l.Enqueue(c[i - 1], c[i - 1]);
            left = i;
            r.Enqueue(c[c.Length - i], c[c.Length - i]);
            right = c.Length - i - 1;
        }

        bool f = true;
        while (k > 0)
        {
            if (left > right)
                f = false;

            int a = l.Count>0 ? l.Peek() : int.MaxValue;
            int b = r.Count>0 ? r.Peek() : int.MaxValue;

            if (a <= b)
            {
                ans += a;
                l.Dequeue();
                if (f)
                    l.Enqueue(c[left],c[left]);
                if (f)
                    left++;
            }
            else
            {
                ans += b;
                r.Dequeue();
                if (f)
                    r.Enqueue(c[right],c[right]);
                if (f)
                    right--;
            }

            k--;
        }

        return ans;
    }
}