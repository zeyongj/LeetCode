public class Solution {
    public bool IsNumber(string s) {
        // Exponential could be upper or lower case E / e, so change all
        // characters to lower case. String is at least 1 character
        s = s.ToLower();
        bool isPeriod = false;
        bool isExpo = false;
        bool isNum = false;
        for(int i = 0; i < s.Length; i++)
        {
            // check each character of the string s.
            char checkChar = s[i];
            if(checkChar >= '0' && checkChar <= '9') isNum = true;           
                else if(checkChar == 'e')
                {
                    if(isExpo || !isNum)
                    {
                        return false;
                    }                
                isExpo = true;
                isNum= false;
            }
            else if(checkChar == '.')
            {
                if(isPeriod || isExpo) return false;                
                isPeriod = true;
            }
            else if(checkChar == '+' || checkChar == '-')
            {               
                if(i != 0 && s[i-1] != 'e') return false;               
            }
            else return false;           
        }        
        return isNum;
    }
}