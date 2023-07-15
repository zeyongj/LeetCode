import java.math.BigDecimal;
import java.math.BigInteger;

public class Solution {
        public boolean isNumber(String s) {
    	s = s.trim();
    	if(s.length() == 0) {
    		return false;
    	}
    	boolean result = true;
        try{
        	new BigDecimal(s);
        } catch(Exception e) {
        	result = false;
        }
        if(s.contains("e")) {
        	int firstIndex = s.indexOf("e");
        	int lastIndex = s.lastIndexOf("e");
        	if(lastIndex != firstIndex) {
        		return false;
        	}
        	try{
        		new BigDecimal(s.substring(0, firstIndex));
        		new BigInteger(s.substring(firstIndex + 1));
        		result = true;
        	} catch(Exception e) {
            	result = false;
            }
        }
        return result;
    }
}