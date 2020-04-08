"""
Given an array of integers that is already
sorted in ascending order, find two numbers
such that they add up to a specific target number.

The function twoSum should return indices of 
the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) 
are not zero-based.
You may assume that each input would have exactly 
one solution and you may not use the same element twice.
"""

a = HashTable([3,3,2,2,2,0,0,1,1] )


class HashTable:
    def __init__(self,l):
        self.keys = set(l)
        self.dicts = {k:[] for k in self.keys }
        for i,v in enumerate(l):
            self.dicts[v].append(i)
    def __getitem__(self,key):
        return self.dicts[key] if key in self.keys else None
    def __str__(self):
        return  "{\n%s\n}"% (["%s:%s"%(k,str(v)) for k,v in self.dicts.items()])
    
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = HashTable(numbers)
        for i in ht.keys:
            if target-i in ht.keys:
                if (target -i) == i :
                    if len(ht[i]) > 1:
                        return [ht[i][0] + 1, ht[i][1] + 1]
                    else: pass
                else:
                    return [ht[i][0] + 1 ,ht[target-i][0] + 1] if i <=  target -i else  \
                    [ht[target-i][0] + 1,ht[i][0] + 1]