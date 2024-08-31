class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ret = set()
        dic = collections.defaultdict(list)
        for i,item in enumerate(transactions):
            name, time, amount, city = item.split(",")
            dic[name].append((int(time),city,i))
            if int(amount) > 1000:
                ret.add(i)
        for k,v in dic.items():
            v.sort()
            vleng = len(v)
            for i in range(vleng):
                old = v[i]
                for j in range(i+1,vleng):
                    new = v[j]
                    diff = new[0]-old[0]
                    if diff <= 60:
                        if new[1] != old[1]:
                            ret.add(old[2])
                            ret.add(new[2])
                    else:
                        break
        return [transactions[x] for x in ret]