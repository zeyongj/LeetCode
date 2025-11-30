class Solution(object):
	def gcd(self, x, y):
		while y > 0:
			x, y = y, x % y
		return x

	def lcm(self, x, y):
		return x*y//self.gcd(x,y)

	def nthMagicalNumber(self, N, A, B):
		temp = self.lcm(A,B)
		seq = {}
		for i in range(1,temp//A+1):
			seq[i*A] = 1
		for i in range(1,temp//B+1):
			seq[i*B] = 1
		cand = sorted([key for key, value in seq.items()])
		ans = ((N-1)//len(cand))*cand[-1] + cand[N%len(cand)-1]
		return ans % (10**9+7)