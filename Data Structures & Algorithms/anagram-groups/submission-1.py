class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        track key: frequency of each letter (o(26) for 26 letters) and value: group list

        if frequescy array in seen, add to group
        else add key value to seen 
        '''

        ans = {} # o(m) space
        for w in strs: # o(m) time
            track = [0]*26
            for i in w: # o(n) time
                track[ord(i) - 97] += 1
            track = tuple(track)
            if track in ans:
                ans[track].append(w)
            else:
                ans[track] = [w]
        return [ans[i] for i in ans]