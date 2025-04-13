class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s1 = re.sub(r'[^a-zA-Z0-9]','',s).upper()
        process = ""
        first_group_length = len(s1) % k or k
        result = ""
        result += s1[:first_group_length] 
        for e in range(first_group_length, len(s1)):
            process += s1[e]
            if len(process) == k:
                result += "-"
                result += process
                process = ""
        return result