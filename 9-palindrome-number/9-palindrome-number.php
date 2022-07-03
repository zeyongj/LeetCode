class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
		if ($x >= 0) {
			$arr = str_split($x);

			if ($arr == array_reverse($arr)) {
				return true;
			} else {
				return false;
			}
		} else {
			return false;
		}
	}
}