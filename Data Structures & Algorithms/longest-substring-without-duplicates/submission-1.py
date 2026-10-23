class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cm = 0
        n = len(s)
        l, r = 0, 0
        visited = {}
        while r < n:
            if s[r] in visited:
                cm = max(cm, r - l)
                l = max(l,visited[s[r]] + 1 )
                visited[s[r]] = r

               
                
            else:
                visited[s[r]] = r
            
   
            r += 1

        return max(cm, r - l)
        