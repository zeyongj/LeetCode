class Solution(object):
    def kthDistinct(self, arr, k):
        item_list=[]
        items_set=set()
        for i in arr:
            if i in item_list:
                items_set.add(i)
            else :
                item_list.append(i)
        for i in items_set:
            print(i)
            item_list.remove(i)
        counter = 1
        res = ""
        for key in item_list:
            if counter == k:
                res = key
            counter += 1
        return res