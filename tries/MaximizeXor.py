class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            p = p.setdefault(cur, {})
                
    def query(self, num):
        if not self.root: 
            return -1
        p, ans = self.root, 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p:
                p = p[1 - cur]
                ans |= (1 << i)
            else:
                p = p[cur]
        return ans

class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        ''' 
        LeetCode 1707
        '''
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        ans = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            ans[i] = trie.query(x)
        return ans

solution = Solution()
print(solution.maximizeXor([0,1,2,3,4], [[3,1],[1,3],[5,6]]))