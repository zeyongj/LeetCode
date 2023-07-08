class Solution {
    fun getPermutation(n: Int, k: Int): String {
        val s = MutableList<String>(n){it->(it+1).toString()}
        return permute(s, n, k-1)
    }
    fun permute(s: MutableList<String>, n: Int, k: Int): String{
        if(n==1){
            return s[0]
        }
        else{
            var l = getFactorial(n-1)
            return s.removeAt(k/l) + permute(s, n-1, k%l)
        }
    }
    fun getFactorial(n: Int): Int{
        return if(n==1) 1 else n*getFactorial(n-1)
    }
}