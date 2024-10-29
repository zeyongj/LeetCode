class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        a=int(loginTime[0]+loginTime[1])*60+int(loginTime[3]+loginTime[4])
        b=int(logoutTime[0]+logoutTime[1])*60+int(logoutTime[3]+logoutTime[4])
        if (a>b):b+=24*60
        q, r = divmod(a, 15)
        a, b = q + int(r > 0), b // 15
        return max(0, b - a)