public class Solution {
    public bool IsPalindrome(int x) {
        string str = Convert.ToString(x);
        int frontIndex = 0;
        int backIndex = str.Length - 1;

        while (true)
        {
            if (frontIndex >= backIndex)
            {
                return true;
            }
            else if(str[frontIndex] == str[backIndex])
            {
                frontIndex++;
                backIndex--;
                continue;
            }
            else
            {
                return false;
            }
        }
    }
}