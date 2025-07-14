# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Data-Types/problem/find-union

class Solution:
    def Union(self, A, B):
        return A.union(B)
    

# alternatively without union()
class Solution:
    def Union(self, A, B):
        result = set()
        for item in A:
            result.add(item)
            # set itself takes care of duplicates, the set.add() automatically removes duplicates
        for item in B:
            result.add(item)
            # basically just push every elemnt from both sets to master result
        return result
        
# alternatively we could do
class Solution:
    def Union(self, A, B):
        result = set(A)
        result.update(B)
        # update() mutates result by adding elements of B
        # update is like the compressed version of the loop above specifiaclly
        """
        for item in B:
            result.add(item)
        """
        # .update() is just a built-in loop that adds elements from another iterable
        return result 